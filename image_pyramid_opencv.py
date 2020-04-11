import cv2
import numpy as np
img =cv2.imread('korean.jpeg')
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

layer=gp[5]
cv2.imshow("Upper level Gaussian pyramid",layer)
lp=[layer]
for i in range(5,0,-1):
    size = (gp[i - 1].shape[1], gp[i - 1].shape[0])
    gaussian_extend = cv2.pyrUp(gp[i], dstsize=size)
    laplacian=cv2.subtract(gp[i-1],gaussian_extend)
    cv2.imshow(str(i),laplacian)
cv2.imshow(' original image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()