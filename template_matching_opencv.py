import cv2 as cv
import numpy as np
img=cv.imread('chrisfoot.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
template=cv.imread('chris.jpeg',0)
chris=cv.imread('chris.jpeg')
w,h=template.shape[::-1]
res=cv.matchTemplate(gray,template,cv.TM_CCOEFF_NORMED)
print(res)
threshold=0.99;
loc=np.where(res>=threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0]+ w,pt[1]+h),(0,0,255),2)
cv.imshow('chris',img)
cv.imshow('chris face',chris)
cv.waitKey(0)
cv.destroyAllWindows()