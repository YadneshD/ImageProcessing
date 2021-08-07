import cv2
import numpy as np

oi = np.zeros([200, 200], np.uint8)
for i in range(200):
    for j in range(200):
        if i == j :
            oi[i][j] = 255
        elif i <= 5:
            oi[i][j] = 255
        elif j <= 5:
            oi[i][j] = 255
  
structuring_elem = np.ones([3,3], np.uint8)
def masker(mask):
    global oi
    height = len(oi)
    width = len(oi[0])
    dilated_img = np.zeros([height, width], np.uint8)
    eroded_img = np.zeros([height, width], np.uint8)
    for i in range(1,height-1):
        for j in range(1,width-1):
            dilate = max([oi[i-1][j-1]*mask[0][0], oi[i-1][j]*mask[0][1], oi[i-1][j+1]*mask[0][2], oi[i][j-1]*mask[1][0], oi[i][j]*mask[1][1], oi[i][j+1]*mask[1][2], oi[i+1][j-1]*mask[2][0], oi[i+1][j]*mask[2][1], oi[i+1][j+1]*mask[2][2]])            
            erode = min([oi[i-1][j-1]*mask[0][0], oi[i-1][j]*mask[0][1], oi[i-1][j+1]*mask[0][2], oi[i][j-1]*mask[1][0], oi[i][j]*mask[1][1], oi[i][j+1]*mask[1][2], oi[i+1][j-1]*mask[2][0], oi[i+1][j]*mask[2][1], oi[i+1][j+1]*mask[2][2]])            
            dilated_img[i][j] = dilate
            eroded_img[i][j] = erode
            
    return dilated_img, eroded_img
    
dilated_img, eroded_img = masker(structuring_elem)
img_erosion = cv2.erode(oi, structuring_elem)
img_dilation = cv2.dilate(oi, structuring_elem)
cv2.imshow('Original Image', oi)
cv2.imshow('Dilated Image without using Inbuilt function', dilated_img)
cv2.imshow('Eroded Image  without using Inbuilt function', eroded_img)
cv2.imshow('iDilated Image using Inbuilt function', img_dilation)
cv2.imshow('iEroded Image using Inbuilt function', img_erosion)
cv2.waitKey()
