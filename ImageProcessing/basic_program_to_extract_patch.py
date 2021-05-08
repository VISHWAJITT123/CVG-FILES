import numpy as np

A = np.ones([10, 10])

def basicExtractionOfPatch(A):

    counter = 1

    for i in range(10):
        for j in range(10):
            A[i, j] = counter
            counter = counter+1

    print(A)
    patch_size = [3, 3]
    size_A = A.shape

    upper_limit_x = size_A[0]//patch_size[0]
    upper_limit_y = size_A[1]//patch_size[1]

    inp1 = int(input("Enter Row number (0-2)"))
    inp2 = int(input("Enter Column number (0-2)"))

    if inp1>2 or inp2>2:
        print("the number exceeds the number of patch")
        exit(0)

    output = np.zeros(patch_size)

    for k in range(patch_size[0]):
        for m in range(patch_size[1]):
            output[k, m] = A[inp1*patch_size[0]+k, inp2*patch_size[1]+m]



    print(output)

basicExtractionOfPatch(A)
