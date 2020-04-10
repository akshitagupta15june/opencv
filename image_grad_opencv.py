import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('jiminaah.jpeg',0)
lap=cv.Laplacian(img,cv.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX=cv.Sobel(img,cv.CV_64F,1,0)
sobelY=cv.Sobel(img,cv.CV_64F,0,1)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))
sobelcombine=cv.bitwise_or(sobelX,sobelY)
canny=cv.Canny(img,100,200,)
titles=['image','laplacian','SobelX','Sobely','sobelcombine','canny']
images=[img,lap,sobelX,sobelY,sobelcombine,canny]
for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()