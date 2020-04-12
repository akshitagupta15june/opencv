import cv2 as cv
import numpy as np
cap=cv.VideoCapture('walk.avi')
ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    diff=cv.absdiff(frame1,frame2)
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    _,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dilted=cv.dilate(thresh,None,iterations=3)
    contour,_=cv.findContours(dilted,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(frame1,contour,-1,(0,255,0),2)
    for cont in contour:
        (x,y,w,h)=cv.boundingRect(cont)
        if cv.contourArea(cont)<200:
            continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,255),2)
        cv.putText(frame1,"status: {}".format('movement'),(10,20),cv.FONT_HERSHEY_SIMPLEX,1,(250,22,204),3)

    cv.imshow('feed',frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv.waitKey(40)==27:
        break
cv.destroyAllWindows()
cap.release()