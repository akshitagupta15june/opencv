import cv2 as cv
import numpy as np
img=cv.imread('sudoku.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges=cv.Canny(gray,50,150,apertureSize=3)
cv.imshow('canny',edges)
lines=cv.HoughLines(edges,1,np.pi/100,200)
for lin in lines or []:
    rho,theta=lin[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv.lin(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow('image',img)
k=cv.waitKey(0)
cv.destroyAllWindows()
