import cv2
import numpy as np

def gradient(Gx,Gy):

    Gxy = cv2.bitwise_or(Gx,Gy)
    #Gxy = np.uint8(Gxy)

    return Gxy

Gx = cv2.imread('imagex.png', 0)
Gy = cv2.imread('imagey.png', 0)

G = gradient(Gx,Gy)
#print(G)
cv2.imwrite('gradient.png', G)
