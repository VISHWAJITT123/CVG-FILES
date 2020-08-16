import cv2
import numpy as np

I = cv2.imread('image.png',0)

def avgSliding(I):

    patch = [[1,1,1],[1,1,1],[1,1,1]]
    patch = np.array(patch)
    patch_size = [3,3]
    size_I = I.shape
    print(size_I)

    output_matrix = np.zeros([size_I[0]-2, size_I[1]-2])

    for i in range(0,size_I[0]-2):
        for j in range(0,size_I[1]-2):
            output = np.zeros(patch_size)
            for m in range(patch_size[0]):
                for n in range(patch_size[1]):
                    output[m,n] = I[i+m,j+n]

            temp = np.sum(output*patch)
            temp=temp/9
            output_matrix[i,j] = temp

    output_matrix = np.uint8(output_matrix)

    cv2.imwrite('averaging_output.png',output_matrix)

avgSliding(I)
