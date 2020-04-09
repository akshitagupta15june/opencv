import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('jiminaah.jpeg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
two_dimen=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5));
golur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bilateral_filter=cv2.bilateralFilter(img,9,75,75)
titles=['image','2d','blur','Gblur','median','bilateral_filter']
images=[img,two_dimen,blur,golur,median,bilateral_filter]
for i in range(6):
    plt.subplot(2,3 ,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()