import cv2
cam=cv2.VideoCapture()
first_frame=None
while True:
    bb,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_delta=cv2.threshold(frame_delta,30,255,cv2.THRESH_BINARY)
    thresh_delta=cv2.dilate(thresh_frame,None, iterations = 2)
    (_,cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        if contourArea(cnt)<1000:
            continue
        (x,y,h,w)=cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('img',img)
    k=waitKey(2)
    if k==ord('q'):
        break
cv2.destroyAllWindows()
