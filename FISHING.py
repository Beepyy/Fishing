import numpy as np
import cv2,os,pyautogui,time,sys,keyboard,random
from PIL import Image, ImageGrab
green=np.array((0, 100, 100))
high_green=np.array((21, 255, 182))

def z():    
    while True:
        time.sleep(random.uniform(1.0,2.2))
        pyautogui.keyDown("-")                                                #0
        pyautogui.keyUp("-")                                                  #0
        on=False
        timee=time.time()
        while not on and time.time()<=timee+21:
        img=cv2.imread('321.jpg')                                             #1        
            img=np.array(ImageGrab.grab())
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)        
            img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            mask=cv2.inRange(img_hsv,green,high_green)
            q,b,c,d=268,394,616,1339                                          #2 
            kas=mask[q:b,c:d]
            coord=cv2.findNonZero(mask)
            uh=cv2.Canny(img,100,200)
            a=np.mean(uh)
            print('0',a)
            #lst=[]!!!
            for i in coord:
                if i[0][1]>q and i[0][1]<b and i[0][0]>c and i[0][0]<d:
                    print('NASHOLS9')
                    global zx,zy
                    zx,zy=i[0][0],i[0][1]
                    #pyautogui.click(i[0][0],i[0][1])
                    global x,xx,y,yy
                    x,xx,y,yy=i[0][0]-20,i[0][0]+30,i[0][1]-15,i[0][1]+20
                    photo=img[y:yy,x:xx]
                    on=detected(photo)
                    
                    break



def detected(photo):
    while True:
        img=np.array(ImageGrab.grab())
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        photou=img[y:yy,x:xx]
        res=cv2.matchTemplate(photo,photou,cv2.TM_CCOEFF_NORMED)
        print('1',np.mean(res))
        #cv2.imshow('pew',photou)
        if res<0.5:
            time.sleep(random.uniform(0.2,1.5))
            pyautogui.keyDown('Shift')
            pyautogui.click(zx,zy,button='right')
            pyautogui.keyUp('Shift')
            time.sleep(0.5)
            pyautogui.click(zx,zy)
            return True
            break
if __name__=='__main__':
    z()
