import cv2
from picamera import PiCamera
from time import sleep
import final
camera=PiCamera()
camera.start_preview()
if __name__=='__main__':
    
    
    camera.capture('img2.jpg')
    c=1
    while True:
        if(c==1):
            camera.capture('img1.jpg')
            final.fun(c)
        else:
            camera.capture('img2.jpg')
            final.fun(c)
        c=(c%2)+1
        #sleep(1)
camera.stop_preview()
