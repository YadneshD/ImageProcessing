import cv2
import numpy as np

original_img = cv2.imread('cameraman.tif')
original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
height = len(original_img)
width = len(original_img[0])
new_img = np.zeros([height, width], np.uint8)
for i in range(height):
    for j in range(width):
        new_img[i][j] = 255 - original_img[i][j]

cv2.imshow('Negative Image', new_img)
cv2.waitKey()
        