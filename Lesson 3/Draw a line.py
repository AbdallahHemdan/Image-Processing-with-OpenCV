import cv2 
import numpy as np 

img  = cv2.imread('watch.jpg',1)

#cv2.line( img , start_point , end_point , Color , Width_of_line_by_pixels)
cv2.line(img,(0,0),(150,150),(255,255,255),15)

cv2.imshow(" Line on Image " , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
