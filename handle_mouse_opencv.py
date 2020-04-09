import numpy as np
import cv2
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)
def click_event(event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
       print(x,' ,',y)
       font=cv2.FONT_HERSHEY_SIMPLEX
       strXY=str(x)+','+str(y)
       cv2.putText(img,strXY,(x,y),font,0.5,(255,255,0),2)
       cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ',' + str(green)+','+str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 0), 2)
        cv2.imshow('image', img)
img=cv2.imread('korean.jpeg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
