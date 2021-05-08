import cv2
import numpy as np

I = cv2.imread('image.png',0)

def sobelyJumping(I):

    size_I = I.shape
    patch_size = [3,3]
    patch = [[-1,0,1],[-2,0,2],[-1,0,1]]
    patch = np.transpose(patch)
    patch = np.array(patch)

    upper_limit_x = size_I[0]//patch_size[0]
    upper_limit_y = size_I[1]//patch_size[1]

    output_matrix = np.ones([upper_limit_x,upper_limit_y])

    for i in range(0,upper_limit_x):
        for j in range(0,upper_limit_y):
            output = np.ones(patch_size)
            for m in range(patch_size[0]):
                for n in range(patch_size[1]):
                    output[m,n]=I[i*3+m,j*3+n]

            temp = np.sum(patch * output)
            temp = temp/8
            output_matrix[i,j] = temp

    output_matrix = np.uint8(output_matrix)
    cv2.imwrite('sobely_jumping.png',output_matrix)

sobelyJumping(I)
