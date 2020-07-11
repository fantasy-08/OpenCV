import cv2
#i=cv2.imread(r'C:\Users\coolm\Desktop\some.jpg')
from pynput.mouse import Controller
ms=Controller()
cam=cv2.VideoCapture(1)
while True:
    r,i=cam.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    r,thresh=cv2.threshold(gray,70,255,1)
    cnt=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=cnt[0]
    l=len(contours)
    print('total number of touch',l)
    if(l==1):
        cv2.drawContours(i,contours[0],-1,(0,0,255),2)
        m=cv2.moments(contours[0])
        if(m['m00']!=0):
            cx=int(m['m10']/m['m00'])
            cy=int(m['m01']/m['m00'])
            print('centroid',cx,cy)
            ms.position=(cx,cy)
        a=cv2.contourArea(contours[0])
        print('area',a)
    cv2.imshow('img',thresh)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        break
cv2.destroyAllWindows()
