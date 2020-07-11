# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:09:49 2019

@author: Eshaan
"""
from pynput.mouse import Controller,Button
ms=Controller()
'''SKIN COLOR DETECTOR'''
import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img=cv2.medianBlur(img,15)
    l_range=np.array([0,30,60])
    u_range=np.array([20,150,225])
    mask=cv2.inRange(img,l_range,u_range)
    res=cv2.bitwise_and(img,img,mask=mask)
    contour=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt=contour[0]
    l=len(cnt)
    
    if cnt>0:
        area=[]
        for i in range(l):
            aaa=cv2.contourArea(cnt[i])
            area.append(aaa)
        maxx=max(area)
        max_index=area.index(maxx)
        m=cv2.moments(cnt[max_index])
        if m['m00']!=0 :
            cx=(m['m10']/m['m00'])*3
            cy=(m['m01']/m['m00'])*2.25
            ms.position=(cx,cy)
        
        
    cv2.imshow('mask',mask)

    k=cv2.waitKey(2)
    if k==27:
        break
cam.release()
cv2.destroyAllWindows()
