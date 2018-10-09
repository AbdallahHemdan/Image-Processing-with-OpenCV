
import numpy as np 
import cv2 

img = cv2.imread("watch.jpg",1)
#cv2.circle(img,center_point,Raidus,Color,Width_of_line)
#Note if you put  Width_of_line = -1 it wil fill the circle
cv2.circle(img,(100,63),55,(0,0,255),-1)

cv2.imshow()
cv2.waitKey(0)
cv2.destroyAllWindows()


