import cv2
import numpy as np
import math

I = cv2.imread('highway_image.png', 0)
I1 = cv2.Canny(I, 100, 150)
cv2.imwrite('cannyEdge_image.png', I1)

size_I = I.shape
max_size = int(math.sqrt((size_I[0]**2)+(size_I[1]**2)))
A = np.zeros([max_size, 180])
pi = np.pi

for i in range(size_I[0]):
    for j in range(size_I[1]):
        if(I1[i,j] == 255):
            for theta in range(180):
                rho = abs(int((i*(math.cos(theta*180/pi)))+(j*(math.sin(theta*180/pi)))))
                A[rho,theta] = A[rho,theta] + 1

for i in range(size_I[0]):
    for j in range(size_I[1]):
        if(I1[i,j] == 255):
            for theta in range(180):
                rho = abs(int((i*(math.cos(theta*180/pi)))+(j*(math.sin(theta*180/pi)))))
                if A[rho,theta] > 200 :
                    I[i, j] = 255

for i in range(size_I[0]):
    for j in range(size_I[1]):
        if I[i,j] == 255:
            I[i,j] = 255
        else:
            I[i,j] = 0


cv2.imwrite('houghTransform_image.png', I)

