import numpy as np

matrix_size=10
a=np.ones([matrix_size,matrix_size])

def slidingConvolution(x):

    patch_size=[3,3]
    counter =1

    for i in range(matrix_size):
        for j in range(matrix_size):
            a[i,j]=counter
            counter = counter +1

    inp1=int(input("Enter the Row number (1-8)"))
    inp2=int(input("Enter the Column number (1-8)"))

    if inp1>8 or inp2>8 :
        print("input Exceeds the number of patches")
        exit(0);

    i=inp1-1
    j=inp2-1

    output = np.zeros(patch_size)

    for m in range(patch_size[0]):
        for n in range(patch_size[1]):
            output[m,n] = a[i+m,j+n]

    print(output)

slidingConvolution(a)
