import cv2 
import numpy as np 


img = np.zeros((500,500,3),np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText( img , "OpenCv" , (100,500) , font , 4 , (255,255,255) , 2 , cv2.LINE_AA )


cv2.imshow("Write on image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
