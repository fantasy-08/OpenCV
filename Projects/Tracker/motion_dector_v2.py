import cv2
import numpy as np
import random
from pynput.mouse import Controller,Button
ms=Controller()
cam=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Users\Eshaan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
while True:
    r,i=cam.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(gray,1.3,7)
    otp=random.randrange(1000,9999)
    z=0
    if len(face)>0:
        print('Person detected')
        print('your OTP is ',otp)
        totp=int(input('Please enter OTP to proceed '))
        
        if totp==otp:
            cv2.imshow('image',i)
            
            z=1
    cv2.imshow('image',i)
    k=cv2.waitKey(5)
    if(k==27):
        cv2.destroyAllWindows()
    if z==1:
        break

#FACE DETECTED AND OTP GENERATED AND VERIFIED
while True:
    r,i=cam.read()
    k=i[:,:,1]
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    g=cv2.subtract(k,j)
    g=cv2.multiply(g,3)
    r,g=cv2.threshold(g,40,255,0)
    cont=cv2.findContours(g,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt=cont[0]
    L=len(cnt)
    if L>0:
        c=[]
        for i in range(0,L):
            a=cv2.contourArea(cnt[i])
            c.append(a)
        mx=max(c)
        ll=c.index(mx)
        m=cv2.moments(cnt[ll])
        if m['m00']!=0 :
            cx=(m['m10']/m['m00'])*3
            cy=(m['m01']/m['m00'])*2.25
            ms.position=(cx,cy)
            a=cv2.contourArea(cnt[0])
        nl=[]
        for i in range(0,L):
            x=cv2.contourArea(cnt[i])
            nl.append(x)

        mz=max(nl)
        nl.remove(mz)
        try:
            mzz=max(nl)
            lll=nl.index(mzz)
            if mzz>4000 and mzz<6000:
                ms.click(Button.left)
            nl.remove(mzz)
            try:
                mzzz=max(nl)
                llll=nl.index(mzzz)
                if mzzz>4000 and mzzz<6000:
                    ms.click(Button.right)
            except ValueError:
                pass
            
        except ValueError:
            pass
        
    cv2.imshow('image',r)
    k=cv2.waitKey(5)
    if k==27:
        break






cv2.destroyAllWindows()
