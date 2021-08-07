import cv2
import numpy as np

img = cv2.imread('football.jpg', 0)
height = len(img)
width = len(img[0])

new_img = []

for i in range(height):
    temp = []
    for j in range(width):
        temp.append(img[i][j])
        temp.append(img[i][j])
    new_img.append(temp)
    new_img.append(temp)

new_img = np.array(new_img)
cv2.imshow('Original Image', img)
cv2.imshow('Zoomed Image', new_img)
cv2.waitKey()