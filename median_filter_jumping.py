import cv2
import numpy as np

I = cv2.imread('salt_pepper.png',0)

def medianFilterJumping(I):

    size_I = I.shape
    patch_size=[3,3]

    upper_limit_x = size_I[0] // patch_size[0]
    upper_limit_y = size_I[1] // patch_size[1]

    output_matrix = np.ones([upper_limit_x,upper_limit_y])

    for i in range(0,upper_limit_x-3):
        for j in range(0,upper_limit_y-3):
            output = np.zeros(patch_size)
            for m in range(patch_size[0]):
                for n in range(patch_size[1]):
                    output[m,n]= I[i*patch_size[0]+m,j*patch_size[1]+n]

            temp = np.median(output)
            output_matrix[i+1,j+1] = temp

    output_matrix = np.uint8(output_matrix)
    cv2.imwrite('median_filter_jumping.png', output_matrix)

medianFilterJumping(I)