from pygame import mixer
import cv2,time,random
mixer.init()
mixer.music.load(r'cartoon.mp3')
cam=cv2.videoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Users\Eshaan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
while True:
    r,i=cam.read()
    g=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(g,1.3,7)
    r,j=cam.read()
    gg=cv2.cvtColor(j,cv2.COLOR_BGR2GRAY)
    k=j[:,:,1]
    gg=cv2.subtract(gg,k)
    gg=cv2.multiply(gg,3)
    cont=cv2.findContours(gg,RETR_TREE,CHAIN_APPROX_SIMPLE)
    cnt=cont[0]
    b=[]
    for i in cnt:
        c=cv2.contourArea(cnt[i])
        b.append(c)
    L=len(face)
    mx=max(b)
    nx=b.index(mx)
    if L>0:
        mixer.music.play()
        ii=0.1
        if mx>4000:
            mixer.music.set_volume(0.5+i)
            time.sleep(1)
            if i<0.5:
                i+=0.1
        if mx>2000 and mx<4000:
            mixer.music.set_volume(0.5+i)
            time.sleep(1)
            if i>=0.0:
                i-=0.1
    else:
        mixer.music.pause()
    kk=cv2.waitKey(5)
    if kk==27:
        break
destroyAllWindows()
