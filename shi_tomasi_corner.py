import numpy as np
import cv2 as cv
img=cv.imread('shapes.png')
cv.imshow('img',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corner=cv.goodFeaturesToTrack(gray,100,0.01,10)
corner=np.int0(corner)
for i in corner:
    x,y=i.ravel()
    cv.circle(img,(x,y),3,255,-1)
cv.imshow('dst',img)
if cv.waitKey(0) & 0xFF==27:
    cv.destroyAllWindows()
