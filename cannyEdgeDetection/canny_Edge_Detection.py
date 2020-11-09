import cv2
import sobelx_sliding as sx
import sobely_sliding as sy
import gradient as g
import laplacian as lp
import hysteresis1 as h

I = cv2.imread('testing_image.png',0)  # original image
size_I = I.shape
patch_size = [3, 3]

Gx = sx.sobelxSliding(I)                    # Sobel x filter
cv2.imwrite('imagex.png', Gx)
#print(Gx)

Gy = sy.sobelySliding(I)                    # Sobel y filter
cv2.imwrite('imagey.png', Gy)
#print(Gy)

Gxy = g.gradient(Gx, Gy)                    # Gradient image
cv2.imwrite('imagexy.png', Gxy)
#print(Gxy)

L = lp.laplacian(Gxy)                       # Laplacian
cv2.imwrite('imagel.png', L)

H = h.hysteresis1(L)                        # Hysteresis
cv2.imwrite('canny_image.png', H)
