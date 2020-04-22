import numpy as np
import cv2 as cv
cap = cv.VideoCapture('walk.avi')
#kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    #fgmask=cv.morphologyEx(fgmask,cv.MORPH_OPEN,kernel)
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
