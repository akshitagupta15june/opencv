import numpy as np
import cv2 as cv
def nothing(x):
    print(x)

cv.namedWindow('image')
cv.createTrackbar('CF','image',0,255,nothing)

switch='color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)
while(1):
    img=cv.imread('korean.jpeg')
    pos=cv.getTrackbarPos('CF','image')
    font=cv.FONT_HERSHEY_COMPLEX_SMALL
    cv.putText(img,str(pos),(50,150),font,4,(0,0,255))
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    s=cv.getTrackbarPos(switch,'image')


    if s==0:
        pass
    else:
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    cv.imshow('image',img)


cv.destroyAllWindows()