## Aims and Objective
Sergei  Prokudin Gorsky(1863-1944)  was  a  Russian  photographer  and  chemist  whose 
collection of colour photographs is the oldest surviving to this date. 
He used a camera that took a sequence of three black and white exposures using blue, red and green filters. By projecting 
the three images using colored light it was then possible to recover the original colours. See herefor more details. At the beginning of the 20th century, Prokudin-Gorsky embarked on a many year project to systematically document the life of the Russian Empire by means of the new  colour  imaging  technology.  He  then  took  many  of  the  resulting  negatives  with  him  on 
emigration following the revolution of 1917 and they were eventually purchased and digitizedby the US Library of Congress. 
The  objective  of  this  task  is  to  produce  high  quality  colour  reconstructions  from Prokudin-Gorsky's negatives using simple image processing techniques. 

## _TASK_1_
A program that takes any one of these files as an input and produces a corresponding colour image as output. To do this you should divide the original image into three parts and then align the second and third channels to the first, displaying the 
resulting offsets for each channel. 
A  simple  way  to  perform  the  alignment  is  by  searching  through  all  possible  offsets  in  some suitable  range  (e.g.  20  pixels  for  low  resolution  images)  and  computing  for  each  a  score measuring the quality of the match. Three suitable metrics include sum of squared differences (SSD), sum of absolute differences (SAD) and the normalizedcross correlation (NCC). 

## _TASK_2_
Searching  through  all  offsets  can  become  computationally  expensive  for  large  resolution images. To speed up the search procedure you can use a so - called image pyramid. An image pyramid  is  essentially  the  image  at  multiple  scales,  with scales  varying  by  a  factor  of  two. Alignment  can  then  be  done  sequentially,  starting  with  the  highest  level  and  incrementally updating your estimates as you go down the pyramid. 
## _TASK_3_
Try  to  improve  the  visual  quality  of  the  results  of  the  basic  algorithm.  Some  possibilities include colour and contrast adjustments, using a more sophisticated alignment procedure and automatically removing borders.One possible method I implemented is mean filter to improvise the obtained image in task_1 and task_2.Several other techniques availbe and can be used to enhance the quality of the image.

## _Implementation and Design_ : 
The entire implementation is implemented using python programming language and works for versions 2.7+ which also requires opencv and numpy libraries installed.

## _Software_
Download OpenCV and read guided tutorial: http://opencv.org/

## _Format for Testing_ : 
The following commands allows the user to test the implementation.
# python imageprocessing.py IMAGE_FILE_NAME
## _Sample Interaction_ :
python imageprocessing.py devillers.jpg 



## Sample Image before Processing

## Image after processing pixel by pixel


## Image after processing using pyramids


