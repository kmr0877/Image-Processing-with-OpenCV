# import cv2
# #import cv
# import numpy as np
# import matplotlib.pyplot as plt
# img = cv2.imread('s1.jpg')
# img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
# #img1 = cv2.imread('images.jpg',cv2.IMREAD_UNCHANGED)
# #add = img + img1

# #COLOR
# #UNCHANGED

# #plt.imshow(img,cmap = 'gray', interpolation = 'bicubic')
# #plt.show()
# #plt.plot([50,100],[80,100], 'c', linewidth = 5)
# #img[100:150, 100:150] = [255,255,255]
# cv2.imshow('Figure',img)
import cv2
import os
import sys
import numpy as np
import sys

def removeBorder(img):
    return img[30:len(img)-20 , 30 : len(img[0]) - 20]

def reconstruct(img):
    img2 = np.zeros((len(img) / 3 , len(img[0]) , 3), np.uint8)
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            img2[i][j][0] = img[i + (2 * len(img2))][j]
            img2[i][j][1] = img[i + len(img2) + 4][j]
            img2[i][j][2] = img[i + 4][j]
    return img2

if len(sys.argv) < 2:
    print("Not Enough Argument")
    sys.exit(0)

img = cv2.imread(sys.argv[1],0)
while True:
    img2 = reconstruct(img)
    img2 = removeBorder(img2)
    cv2.imshow('Processed Image' ,img2)
    k = cv2.waitKey(0)
    if k == ord('q') or k == ord('Q'):
        break
cv2.destroyAllWindows()
