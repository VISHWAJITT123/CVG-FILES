import cv2
import numpy as np

I = cv2.imread('salt_pepper.png',0)

def medianFilterJumping(I):

    size_I = I.shape
    patch_size=[3,3]

    output_matrix = np.ones([size_I[0]-2,size_I[1]-2])

    for i in range(0,size_I[0]-3):
        for j in range(0,size_I[1]-3):
            output = np.zeros(patch_size)
            for m in range(patch_size[0]):
                for n in range(patch_size[1]):
                    output[m,n]= I[i+m,j+n]

            temp = np.median(output)
            output_matrix[i+1,j+1]= temp

    output_matrix = np.uint8(output_matrix)
    cv2.imwrite('median_filter_sliding.png',output_matrix)

medianFilterJumping(I)