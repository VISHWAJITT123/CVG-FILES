import cv2
import numpy as np

I = cv2.imread('imagel.png', 0)

def hysteresis1(I):

    size_I = I.shape
    ht=150
    lt=50


    for i in range(0,size_I[0]-2):
        for j in range(0, size_I[1]-2):
            if I[i,j] >ht:
                I[i,j] = 255
            elif I[i,j] <lt:
                I[i,j] = 0
            else:
                if I[i-1,j-1]>ht or I[i-1,j]>ht or I[i-1,j+1]>ht or I[i,j-1]>ht or I[i,j+1]>ht or I[i+1,j-1]>ht or I[i+1,j]>ht or I[i+1,j+1]>ht:
                    I[i,j] = 255


    return  I

I = hysteresis1(I)
cv2.imwrite('hysteresis1.png', I)