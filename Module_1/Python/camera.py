import RPi.GPIO as GPIO
import time
import io
import threading
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
 
class Camera(object):
    thread = None
    thread2 = None
    frame = None
    firstcheck = 0
    recordc = 0
    userinput = 0 # start application than
    recordingStart =0;
    def initialize(self):
        if Camera.thread is None:
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            while self.frame is None:
                time.sleep(0)

    def get_frame(self,check):
        Camera.last_access = time.time()
        if self.firstcheck == 0:
            self.initialize()
        return self.frame

    def startdetect(self):
        if Camera.thread2 is None: 
            Camera.thread2 = threading.Thread(target=self._detectloop)
            Camera.thread2.start()
    
    @classmethod
    def _detectloop(cls):
        while True:
            print("dddd")
            time.sleep(4)
            #TODO Write Detecting code
            #detecting condition satisfied
            if()
                #detected && already user Entered
                if(cls.firstcheck == 1):
                    cls.recordingStart =1
                #dectectd && Nobody entered
                else:
                
        
    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.hflip = False
            camera.vflip = False
            point = 0
            checkstate =0
            startrecord = 1
            # TODO // Declear detecting value
            while True:
                foo = None
                #camera.start_preview()
                if cls.firstcheck == 0:
                    time.sleep(2)
                    stream = io.BytesIO()
                    cls.firstcheck = 1 # Enter first user input
                for foo in camera.capture_continuous(stream, 'jpeg',
                                                     use_video_port=True):

                    stream.seek(0)
                    cls.frame = stream.read()
                    stream.seek(0)
                    stream.truncate()
                   
                    
                    if cls.recordingStart == 1:
                        camera.stop_preview()
                        checkstate = 1 # 
                        break
                    if time.time() - cls.last_access > 10:
                        break
                    
                time.sleep(4)
                if checkstate == 0:
                    cls.firstcheck = 0
                    break

                if checkstate == 1:
                    cls.recordc = cls.recordc + 1
                    point2 = 0
                    camera.start_preview()
                    camera.start_recording('/home/pi/Desktop/video%s.h264' % cls.recordc)
                    

                    while True:
                        point2 = point2 + 10
                        time.sleep(1)
                        if point2 > 100:
                            checkstate = 0
                            camera.stop_recording()
                            camera.stop_preview()
                            break
                    
                
        cls.thread = None
