import cv2
import random

I=cv2.imread('image.png', 0)

def salt_pepper(I):
    size_I = I.shape
    for x in range(100000):
        k=random.randint(0,size_I[0]-1)
        l=random.randint(0,size_I[1]-1)
        I[k,l] = random.randint(0,1)*255
    cv2.imwrite('salt_pepper.png',I)

salt_pepper(I)
