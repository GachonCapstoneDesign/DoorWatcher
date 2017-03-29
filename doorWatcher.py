# import the necessary packages
from tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import warnings
import datetime
import imutils
import json
import time
import cv2
import urllib2
from flask import Flask, render_template, Response,session, request
import threading
import streaming

app = Flask(__name__)
thread = None
thread2 = None
myCamera = None
camera = None
current = 1

@app.route('/')
def index():
    return render_template('index.html')

def gen(incamera):
    while True:
        frame = incamera.get_frame(0)
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(myCamera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
        
def opencv2start(arg):
    global myCamera
    while True:
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-c", "--conf", required=True,
        help="path to the JSON configuration file")
        args = vars(ap.parse_args())

        #count for detecting suspected person
        count = 0
        detected = 0
        isSend = 0

        # filter warnings, load the configuration and initialize the Dropbox
        # client
        warnings.filterwarnings("ignore")
        conf = json.load(open(args["conf"]))
        client = None

        # initialize the camera and grab a reference to the raw camera capture
        #camera = PiCamera()
        camera.resolution = tuple(conf["resolution"])
        camera.framerate = conf["fps"]
        rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))
 
        # allow the camera to warmup, then initialize the average frame, last
        # uploaded timestamp, and frame motion counter
        print "[INFO] warming up..."
        time.sleep(conf["camera_warmup_time"])
        lastUploaded = datetime.datetime.now()

        #initiallize the first frame in the video stream
        firstFrame = None

        if myCamera.getstate() == 0:
            rawCapture.truncate(0)
            break
        # capture frames from the camera
        for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image and initialize
            # the timestamp and occupied/unoccupied text

            if myCamera.getstate() == 0:
                rawCapture.truncate(0)
                camera.close()
                break
        
            frame = f.array
            timestamp = datetime.datetime.now()
            text = "Unoccupied"
            if detected is 1:
                count = count + 3.3
                if count > 100 and isSend == 0:
                    #send push message
                    urllib2.urlopen("http://pesang72.cafe24.com/push/GCMSender.php").read()
                    isSend = 1
 
            # resize the frame, convert it to grayscale, and blur it
            pipframe = imutils.resize(frame, width=500)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
            if firstFrame is None:
                firstFrame = gray
                rawCapture.truncate(0)
                continue
 
            # accumulate the weighted average between the current frame and
            # previous frames, then compute the difference between the current
            # frame and running average

            frameDelta = cv2.absdiff(firstFrame,gray)

            # threshold the delta image, dilate the thresholded image to fill
            # in holes, then find contours on thresholded image
            thresh = cv2.threshold(frameDelta, conf["delta_thresh"], 255,
	    cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            im2, cnts, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	    cv2.CHAIN_APPROX_SIMPLE)
 
            # loop over the contours
            for c in cnts:
                # if the contour is too small, Signore it
                if cv2.contourArea(c) < conf["min_area"]:
		    continue
 
                # compute the bounding box for the contour, draw it on the frame,
                # and update the text
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Occupied " + str(count)
                detected = 1
 
            # draw the text and timestamp on the frame
            ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
            cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
	    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
	    0.35, (0, 0, 255), 1)
            if text == "Unoccupied":
                count = 0
                isSend = 0

            # check to see if the frames should be displayed to screen
            if conf["show_video"]:
                # display
                cv2.imshow("DoorWatcher Suspected Person Detection", frame)
                cv2.imshow("thresh", thresh)
                key = cv2.waitKey(1) & 0xFF
 
                # if the `q` key is pressed, break from the lop
                if key == ord("q"):
                    break
                time.sleep(0.1)
 
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)

if __name__ == '__main__':
    #initialize camera
    camera = PiCamera()
    myCamera = streaming.Streaming()
    #app.thread =threading.Thread(target=startprogram, args=())
    #app.thread.start()
    thread2 =threading.Thread(target=opencv2start, args=(0,))
    thread2.start()
    app.run(host='0.0.0.0', debug=False, threaded=True)
    while True:
        current = myCamera.getstate()
        print(current)
