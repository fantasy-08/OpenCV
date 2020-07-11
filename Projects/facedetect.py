import cv2
cam=cv2.VideoCapture()
fd=cv2.CascadeClassifier(r'D:\A\opencv-master\opencv-master\data\haarcascades')
while True:
    r,i=cam.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(gray,1.3,3)
    print(face)
    print("number of detected faces are",len(face))
    for (x,y,w,h) in face:
        cv2.rectangle(i,(x,y),(x+w,w+h),(0,0,255),2)
    cv2.imshow('image',i)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        break
cv2.destroyAllWindows()
    

