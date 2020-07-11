import cv2,random,time,sys
import numpy as np
i=np.uint8(np.zeros([300,300]))
x,y,xx,yy=random.randrange(100,200),random.randrange(100,200),random.randrange(100,200),random.randrange(100,200)
i[x:x+5,y:y+5]=255
i[xx:xx+2,yy:yy+2]=255
score=0
z=random.randrange(1,5)
ii=0.07
i[0:300,0:3]=255
i[0:300,296:300]=255
i[296:300,0:300]=255
i[0:3,0:300]=255
while True:
    cv2.imshow('img',i)
    if z==1:#right
        i[x:x+5,y:y+5]=0
        i[x:x+5,y+1:y+6]=255
        
    
        cv2.imshow('img',i)
        y+=1
    
        time.sleep(ii)
        if xx>=x and xx-x<=5 and yy>=y and yy-y<=5:
            i[xx:xx+3,yy:yy+3]=0
            xx,yy=random.randrange(100,200),random.randrange(100,200)
            i[xx:xx+2,yy:yy+2]=255
            cv2.imshow('img',i)
            if ii>=0 and ii-0.02>=0:
                ii-=0.02
            score+=5
            
    k=cv2.waitKey(1)
    if k==27:
        break
    if x==0 or x==300 or y==0 or y==300:
        
        print('GAME OVER !!!')
        print('your score is = ',score)
        break
    if z==2:#left
        i[x:x+5,y:y+5]=0
        i[x:x+5,y:y+4]=255
    
        cv2.imshow('img',i)
        y-=1
        if xx>=x and xx-x<=5 and yy>=y and yy-y<=5:
            i[xx:xx+3,yy:yy+3]=0
            xx,yy=random.randrange(100,200),random.randrange(100,200)
            i[xx:xx+2,yy:yy+2]=255
            cv2.imshow('img',i)
            
            if ii>=0 and ii-0.02>=0:
                ii-=0.02
            score+=5
    
        time.sleep(ii)
    if z==3:#up
        if xx>=x and xx-x<=5 and yy>=y and yy-y<=5:
            i[xx:xx+3,yy:yy+3]=0
            xx,yy=random.randrange(100,200),random.randrange(100,200)
            i[xx:xx+2,yy:yy+2]=255
            cv2.imshow('img',i)
            if ii>=0 and ii-0.02>=0:
                ii-=0.02
            score+=5
        i[x:x+5,y:y+5]=0
        i[x:x+4,y:y+5]=255
    
        cv2.imshow('img',i)
        x-=1

    
        time.sleep(ii)
        
    if z==4:#down
        i[x:x+5,y:y+5]=0
        i[x+1:x+6,y:y+5]=255
    
        cv2.imshow('img',i)
        x+=1
        time.sleep(ii)
        if xx>=x and xx-x<=5 and yy>=y and yy-y<=5:
            i[xx:xx+3,yy:yy+3]=0
            xx,yy=random.randrange(100,200),random.randrange(100,200)
            i[xx:xx+3,yy:yy+3]=255
            cv2.imshow('img',i)
            if ii>=0 and ii-0.02>=0:
                ii-=0.02
            score+=5
    if k==ord('w'):
        z=3
    elif k==ord('s'):
        z=4
    elif k==ord('d'):
        z=1
    elif k==ord('a'):
        z=2
    cv2.imshow('img',i)
    
    
        
cv2.distroyAllWindows(0)

