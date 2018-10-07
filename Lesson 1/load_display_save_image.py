#import the packages
import numpy as np
import cv2
	
#Read the image 	
img = cv2.imread('messi5.jpg',0)
#Show the image 
cv2.imshow('image',img)

k = cv2.waitKey(0)

# Wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()
# Wait for 's' key to save and exit    
elif k == ord('s'):
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
