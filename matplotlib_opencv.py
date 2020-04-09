import cv2 as cv
from matplotlib import  pyplot as plt
img=cv.imread('Akshita_pic.jpg',-1)
cv.imshow('image',img)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()