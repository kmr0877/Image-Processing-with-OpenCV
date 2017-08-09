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
import glob
import math
import time


sys.setrecursionlimit(5000)
    
isShowImg = 0
path = 'data/'
#for infile in glob.glob(os.path.join(path,'*.jpg')):
#    imagefile = infile
for num in range(70,140):
    imagefile = path + "v3_" + str(num) + ".jpg"
    infile = imagefile
    print "----read image file----"
    print infile
    outputFileName = os.path.basename(imagefile)
    outimg = "outimg/_"+outputFileName
    a = cv2.LoadImage(outimg)
    cv2.ShowImage("Tracking"+ str(num),a)
    time.sleep(0.2)
    