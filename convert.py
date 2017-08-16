import sys
import cv2
import numpy as np

if len(sys.argv) < 2:
    print "Not Enough Argument"
    sys.exit(0)

img = cv2.imread(sys.argv[1])

img2 = np.zeros((len(img)*3,len(img[0]),1),np.uint8)

k=0
for i in range(len(img)):
    for j in range(len(img2[0])):
        img2[k][j] = img[i][j][0]
    k += 1

for i in range(len(img)):
    for j in range(len(img2[0])):
        img2[k][j] = img[i][j][1]
    k += 1
for i in range(len(img)):
    for j in range(len(img2[0])):
        img2[k][j] = img[i][j][2]
    k += 1
cv2.imwrite('con_'+sys.argv[1],img2)
