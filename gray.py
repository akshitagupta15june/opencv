import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('Akshita_pic.jpg',1)

plt.imshow(img[:,:,1], cmap='gray',interpolation=None)
plt.show()