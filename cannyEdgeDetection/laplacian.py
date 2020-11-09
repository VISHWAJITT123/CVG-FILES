import numpy as np
import cv2

def laplacian(I):
    patch = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    patch = np.array(patch)
    patch_size = [3, 3]
    size_I = I.shape

    output_matrix = np.ones([size_I[0], size_I[1]])

    for i in range(0, size_I[0]-2):
        for j in range(0, size_I[1]-2):
            output = np.zeros(patch_size)
            for m in range(patch_size[0]):
                for n in range(patch_size[1]):
                    output[m, n] = I[i+m, j+n]

            temp = np.sum(output * patch)
            output_matrix[i, j] = temp

    output_matrix = np.uint8(output_matrix)
    return output_matrix

I = cv2.imread('imagexy.png', 0)
#print(I)

output_matrix = laplacian(I)
print(output_matrix)

cv2.imwrite('laplacian.png', output_matrix)
