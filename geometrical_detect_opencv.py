import numpy as np
import cv2 as cv
img=cv.imread('shaping.png')
img=cv.resize(img,(400,520))
imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thresh=cv.threshold(imgray,240,255,cv.THRESH_BINARY)
contours,_=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
for con in contours:
    approx=cv.approxPolyDP(con,0.01*cv.arcLength(con,True),True)
    cv.drawContours(img,[approx],0,(0,0,0),5)
    x=approx.ravel()[0]-5
    y=approx.ravel()[1]-6
    if len(approx)==3:
        cv.putText(img,'Triangle',(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==4:
        x1,y1,w,h=cv.boundingRect(approx)
        aspectratio=float(w)/h
        print(aspectratio)
        if aspectratio>=0.95 and aspectratio<=1.05:
            cv.putText(img, 'Square', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img,'Rectangle',(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==8:
        cv.putText(img,'Octagon',(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==5:
        cv.putText(img,'Pentangle',(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else:
        cv.putText(img,'Circle',(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))


cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()