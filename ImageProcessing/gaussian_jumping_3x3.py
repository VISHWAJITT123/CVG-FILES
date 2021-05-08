import cv2
import numpy as np

I = cv2.imread('image.png', 0)

def gaussianJumping(I):

    patch = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    patch = np.array(patch)
    patch_size = [3, 3]
    size_I = I.shape

    upper_limit_x = size_I[0] // patch_size[0]
    upper_limit_y = size_I[1] // patch_size[1]

    output_matrix = np.zeros([upper_limit_x, upper_limit_y])

    for i in range(0, upper_limit_x):
        for j in range(0, upper_limit_y):
            output = np.zeros(patch_size)
            for m in range(patch_size[0]):
                for n in range(patch_size[1]):
                    output[m, n] = I[i * 3 + m, j * 3 + n]

            temp = np.sum(patch * output)
            temp = temp / 16
            output_matrix[i, j] = temp

    output_matrix = np.uint8(output_matrix)
    cv2.imwrite('gaussian_jumping.png', output_matrix)

gaussianJumping(I)
