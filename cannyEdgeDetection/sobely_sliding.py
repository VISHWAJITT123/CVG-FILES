import cv2
import numpy as np

I = cv2.imread('image.png',0)

def sobelySliding(I):

    size_I = I.shape
    patch_size = [3,3]
    patch = [[-1,-2,-1],[0,0,0],[1,2,1]]
    patch = np.array(patch)

    output_matrix = np.ones([size_I[0]-2, size_I[1]-2])
    for i in range(0, size_I[0]-2):
        for j in range(0, size_I[1]-2):
            output = np.ones(patch_size)
            for m in range(patch_size[0]):
                for n in range(patch_size[1]):
                    output[m, n] = I[i+m, j+n]

            temp = np.sum(patch * output)
            temp = temp/8
            output_matrix[i, j] = temp

    #output_matrix = np.uint8(output_matrix)

    return output_matrix

S = sobelySliding(I)

S= np.uint8(S)
cv2.imwrite('sobely_sliding.png', S)