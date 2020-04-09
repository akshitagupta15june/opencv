import cv2
import numpy as np
img1=np.zeros((249,203,3),np.uint8)
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread("korean.jpeg")

bitnot=cv2.bitwise_not(img2,img1)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bitand",bitnot)
cv2.waitKey(0)
cv2.destroyAllWindows()