# 抓圖
try:
    from urllib import urlretrieve
except ImportError:
    from urllib.request import urlretrieve
# OCR
import cv2
import numpy as np
from PIL import Image,ImageEnhance
import pytesseract

########################
#                      #
#      以下為開始處      #
#                      #
########################
imgURL = 'https://queryweb.tscc.com.tw/tra_web/vimg.aspx'
imgFile = 'pic.png'
urlretrieve(imgURL, imgFile)

#Color Selection
#im = cv2.imread('pic.png')
## Convert BGR to HSV
#hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
## define range of blue color in HSV
#lower_blue = np.array([110,50,50])
#upper_blue = np.array([130,255,255])
## Threshold the HSV image to get only blue colors
#mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
#res_blue = cv2.bitwise_and(im,im, mask= mask_blue)
#cv2.imshow('Yeeeeee', mask_blue)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imshow('Yeeeeee',hsv)
#cv2.imshow('Yeeeeee',mask_blue)
#cv2.imwrite('new.png',res_blue)


#以灰階開黨
im = cv2.imread('pic.png', 0)

#Enhance
retval, im = cv2.threshold(im, 1, 255, cv2.THRESH_BINARY_INV)

for i in range(len(im)):
  for j in range(len(im[i])):
    if im[i][j] == 255:
      count = 0 
      for k in range(-5, 3):
        for l in range(-5, 1):
          try:
            if im[i + k][j + l] == 255:
              count += 1
          except IndexError:
            pass
      # 這裡 threshold 設 4，當周遭小於 4 個點的話視為雜點
      if count <= 2:
        im[i][j] = 0

#去雜質
im = cv2.dilate(im, (2, 2), iterations=2)
#im = cv2.erode(im, (2, 2), iterations=1)

#Spilt

#pic output
cv2.imshow('Yeeeeee',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('new.png',im)

#辨識結果
print(pytesseract.image_to_string(Image.open('new.png')))