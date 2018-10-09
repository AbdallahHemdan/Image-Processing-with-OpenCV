import numpy as np 
import cv2 

img = cv2.imread("watch.jpg",1)

# cv2.rectangle(img,top_left_point , bottom_right_point , Color , Width_of_line )
# Note if you put  Width_of_line = -1 it wil fill the rectangle
cv2.rectangle(img,(15,25),(200,150),(255,0,0),5)

cv2.imshow("Rectangle on image" ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()

