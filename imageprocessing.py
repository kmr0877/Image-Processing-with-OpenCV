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
import numpy as np
import sys

def removeBorder(img):
    return img[30:len(img)-20 , 30 : len(img[0]) - 20]

def getColor(blue,green,red,level):
    img2 = np.zeros((len(red) , len(red[0]) , 3), np.uint8)
    for i in range(len(img2)):
        for j in range(len(img2[0])):
            img2[i][j][0] = blue[i][j]/(level + 1)
            img2[i][j][1] = green[i][j]/(level + 1)
            img2[i][j][2] = red[i][j]/(level + 1)
    return img2

def getAllFilters(img):
    filters = []
    for k in range(3):
        img2 = np.zeros((len(img) / 3, len(img[0]) - 20, 1), np.uint8)
        for i in range(len(img2)):
            for j in range(len(img2[0])):
                if k == 0:
                    img2[i][j] = img[i + (2 * len(img2))][j]
                if k == 1:
                    img2[i][j] = img[i + len(img2)][j]
                if k == 2:
                    img2[i][j] = img[i][j]
        filters.append(img2)
    return filters

def getAllPyramids(img , level):
    G = img.copy()
    gpA = [G]
    for i in xrange(level):
        G = cv2.pyrDown(G)
        gpA.append(G)
    return gpA

def reconstruct(colorPyramid,level):
    im = colorPyramid[level]
    for i in range(len(colorPyramid) - 2, -1, -1):
        im = cv2.pyrUp(im)
        im = cv2.resize(im, (colorPyramid[i].shape[1], colorPyramid[i].shape[0]))
        im = cv2.add(im, colorPyramid[i])
    return im

level = 4
if len(sys.argv) < 2:
    print("Not Enough Argument")
    sys.exit(0)

img = cv2.imread(sys.argv[1],0)
filters = getAllFilters(img)
pyramids = []
for filter in filters:
    pyramids.append(getAllPyramids(filter,level))
colorPyramid = []
for i in range(len(pyramids[0])):
    colorPyramid.append(getColor(pyramids[2][i],pyramids[1][i],pyramids[0][i],level))

im = reconstruct(colorPyramid,level)

im = removeBorder(im)

cv2.imshow('Image',im)
k = cv2.waitKey(0)
if k == ord('q') or k == ord('Q'):
    cv2.destroyAllWindows()
