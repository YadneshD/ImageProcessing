import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pout.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height = len(img)
width = len(img[0])
pixels = height*width
nk = np.zeros(256)
pdf = np.zeros(256)
cdf = np.zeros(256)
Skl_1 = np.zeros(256)
rounded_Sk = np.zeros(256)
new_grey_level_count = np.zeros(256)
new_image = np.zeros([height, width], np.uint8)
inbuilt_hist_img = cv2.equalizeHist(img)
inbuilt_hist, bins = np.histogram(img.flatten(),256,[0,256])
for i in range(height):
    for j in range(width):
        x = img[i][j]
        nk[x] += 1
for i in range(256):
    pdf[i] = nk[i]/pixels

summ = 0
for i in range(256):
    summ += pdf[i]
    cdf[i] = summ
for i in range(256):
    Skl_1[i] = cdf[i]*255
for i in range(256):
    rounded_Sk[i] = int(round(Skl_1[i]))
for i in range(height):
    for j in range(width):
        x = img[i][j]
        new_image[i][j] = np.uint8(rounded_Sk[x])
for i in range(256):
    x = int(rounded_Sk[i])
    new_grey_level_count[x] += nk[i]
x_axis = np.array([i for i in range(256)])
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.plot(x_axis, nk)
ax1.set_title("Histogram")
ax2.plot(x_axis, new_grey_level_count)
ax2.set_title("Equalized Histogram without using inbuilt functions")
plt.show()
#print(new_image)
#print(len(new_image), len(new_image[0]))
#print(type(new_image))
cv2.imshow("Original Image", img)
cv2.imshow("Manually Equalized Image", new_image)
cv2.imshow("Equalized Image using built-in function", inbuilt_hist_img)
cv2.waitKey()
