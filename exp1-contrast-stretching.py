import cv2
import numpy as np

original_img = cv2.imread('onion.png')
original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
height = len(original_img)
width = len(original_img[0])
new_img = np.zeros([height, width], np.uint8)
print("Enter R1 and R2")
r1, r2 = list(map(float, input().split()))
print("Enter alpha, beta, gamma, v and w")
alpha, beta, gamma,v ,w = list(map(float, input().split()))

for i in range(height):
    for j in range(width):
        if original_img[i][j] < r1:
            new_img[i][j] = int(alpha*original_img[i][j])
        elif original_img[i][j] > r2:
            new_img[i][j] = int(gamma*(original_img[i][j] - r2) + w)
        else:
            new_img[i][j] = int(beta*(original_img[i][j] - r1) + v)

cv2.imshow('Original Image', original_img)
cv2.imshow('Contrast Stretched Image', new_img)
cv2.waitKey()
