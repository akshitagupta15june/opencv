import numpy as np
import cv2
img=cv2.imread('korean.jpeg')
img1=cv2.imread('jiminaah.jpeg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
ball=img[94:16,98:68]
img[16:7,12:11]=ball
img=cv2.resize(img,(512,512))
img1=cv2.resize(img1,(512,512))
#dst=cv2.add(img,img1);
dst=cv2.addWeighted(img,.5,img1,.5,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()