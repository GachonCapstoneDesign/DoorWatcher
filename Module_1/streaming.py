import RPi.GPIO as GPIO
import time
import io
import threading
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
 
class Streaming(object):
    thread = None
    thread2 =None
    frame = None
    last_access = None
    state = 1

    #def initCam(self,cam):
        #Streaming.camera = cam

    def initialize(self):
        if Streaming.thread is None:
            Streaming.setstate()
            time.sleep(1)
            Streaming.thread = threading.Thread(target=self._thread)
            Streaming.thread.start()
            while self.frame is None:
                time.sleep(0)

    def get_frame(self,check):
        Streaming.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def getstate(self):
        return self.state

    @classmethod
    def setstate(self):
        self.state = 0
    
    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as cc:
            cc.resolution = (320, 240)
            cc.hflip = True
            cc.vflip = True
            time.sleep(2)

            stream = io.BytesIO()
            stream.truncate()
            for foo in cc.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                stream.seek(0)
                cls.frame = stream.read()

                stream.seek(0)
                stream.truncate()

                if time.time() - cls.last_access > 1:
                    stream.truncate()
                    cls.state =1
                    break
                
        cls.thread = None
        time.sleep(4)
