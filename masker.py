import cv2
import numpy as np

oi = cv2.imread('coins.png')
oi = cv2.cvtColor(oi, cv2.COLOR_BGR2GRAY)
def masker(mask):
    print(mask)
    global oi
    height = len(oi)
    width = len(oi[0])
    new_img = np.zeros([height, width], np.uint8)
    for i in range(1,height-1):
        for j in range(1,width-1):
            #print(oi[i-1][j-1], "*" , mask[0][0], '\n' , oi[i-1][j], "*" , mask[0][1],  '\n' , oi[i-1][j+1], "*" , mask[0][2], '\n' , oi[i][j-1], "*" , mask[1][0], '\n' , oi[i][j], "*" , mask[1][1], '\n' , oi[i][j+1], "*" , mask[1][2], '\n' , oi[i+1][j-1], "*" , mask[2][0], '\n' , oi[i+1][j], "*" , mask[2][1], '\n' , oi[i+1][j+1], "*" , mask[2][2])
            summ = sum([oi[i-1][j-1]*mask[0][0], oi[i-1][j]*mask[0][1], oi[i-1][j+1]*mask[0][2], oi[i][j-1]*mask[1][0], oi[i][j]*mask[1][1], oi[i][j+1]*mask[1][2], oi[i+1][j-1]*mask[2][0], oi[i+1][j]*mask[2][1], oi[i+1][j+1]*mask[2][2]])            
            #x = [[oi[i-1][j-1], oi[i-1][j], oi[i-1][j+1]], [oi[i][j-1], oi[i][j], oi[i][j+1]], [oi[i+1][j-1], oi[i+1][j], oi[i+1][j+1]]]
            #x = np.array(x)
            #summ = sum(sum(x*mask))
            if summ >= 127:
                new_img[i][j] = 255
            else:
                new_img[i][j] = 0
    cv2.imshow('MaskedOP', new_img)
    cv2.imshow('Original_img', oi)
    cv2.waitKey()

masker(np.array([[-1, -1, -1], [0,0,0], [1,1,1]]))
masker(np.array([[-1, 0, 1], [-1,0,1], [-1,0,1]]))
masker(np.array([[-2, -1, 0], [-1, 0, 1], [0,1,2]]))

