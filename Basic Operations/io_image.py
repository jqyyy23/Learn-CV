import cv2
import os

#read image
image_path = os.path.join('.','plane.jpg')

img = cv2.imread(image_path)

#write image
cv2.imwrite(os.path.join(".", 'plane_out.jpg'), img) 

#visualize image
cv2.imshow('image', img)
cv2.waitKey(0) #wait till a key is pressed
