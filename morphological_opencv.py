import cv2 as cv
import numpy as np
from matplotlib import  pyplot as plt
img=cv.imread('balls.jpeg',0)
_,mask=cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernel=np.ones((5,5),np.uint8)
dilation=cv.dilate(mask,kernel,iterations=2)
erosion=cv.erode(mask,kernel,iterations=1)
opening=cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
closing=cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
mg=cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernel)
cross=cv.morphologyEx(mask,cv.MORPH_CROSS,kernel)
titles=['image','mask','dilation','erosion','opening','closing','morph_gradient','cross']
images=[img,mask,dilation,erosion,opening,closing,mg,cross]

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
