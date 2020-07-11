import cv2
import numpy as np
draw=True
mode=True
ix,iy=-1,-1
def draw_circle(event,x,y,flag,param):
    global ix,iy,draw,mode
    if event==cv2.EVENT_LBUTTONDOWN:
        draw=1
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if draw==True:
            if mode==True:
                cv2.rectangle(i,(ix,iy),(x,y),(255,0,0),-1)
            else:
                cv2.circle(i,(ix,iy),5,255,-1)
    elif event==cv2.EVENT_LBUTTONUP:
        draw=0
        if mode==True:
            cv2.rectangle(i,(ix,iy),(x,y),(255,0,0),-1)
        else:
            cv2.circle(i,(ix,iy),5,255,-1)
i=np.uint8(np.zeros([500,500,3]))
cv2.setMouseCallback('i',draw_circle)
while True:
    cv2.imshow('i',i)
    k=cv2.waitKey(2)
    if k==27:
        break
    if k==ord('m'):
        mode= not mode
cv2.destroyAllWindows()
            
            
