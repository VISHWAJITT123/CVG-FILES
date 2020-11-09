import cv2
import numpy as np
import copy

def hysteresis(I):

    patch_size = [3, 3]
    size_I = I.shape
    I1 = copy.deepcopy(I)

    for i in range(0, size_I[0]-(patch_size[0]-1)):
        for j in range(0, size_I[1]-(patch_size[1]-1)):
            output = np.ones(patch_size)
            for m in range(0, patch_size[0]):
                for n in range(0, patch_size[1]):
                    output[m,n] = I[i+m, j+n]

            s = np.max(output)

            for m in range(0, patch_size[0]):
                for n in range(0, patch_size[1]):

                    if output[i+m, j+n] > 150:
                        output[i+m, j+n] = 255

                    elif output[i+m, j+n] < 100:
                        output[i+m, j+n] = 0

                    else:
                        if s > 150:
                            output[i+m, j+n] = 255
                        else:
                            output[i+m, j+n] = 0


            I1[i+m, j+n] = output[i+m, j+n]

    return I1


I = cv2.imread('imagel.png', 0)

H = hysteresis(I)
print(H)

cv2.imwrite('hysteresis.png', H)