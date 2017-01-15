import cv2
import numpy


#import original image

originalImg = cv2.imread('/home/suyash/Downloads/rsz_12exam_help6-page-001.jpg',cv2.IMREAD_GRAYSCALE)

resizedImg = cv2.resize(originalImg, (0,0), fx=0.5, fy=0.5)

cv2.imshow('original',resizedImg)
cv2.waitKey(0)

#applying edge detection
edged = cv2.Canny(resizedImg.copy(), 30, 200)

cv2.imshow('edged',edged)
cv2.waitKey(0)


#finding contours edged image
contours,hierarchy = cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

#drawing contours on image
cv2.drawContours(resizedImg,contours, -1, (0,255,0), 3)

cv2.imshow('contours',resizedImg)
cv2.waitKey(0)