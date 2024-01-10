import cv2 
import numpy as np 
path =cv2.imread("C:\\Users\\abhis\\Pictures\\Purple_flower_(4764445139).jpg")
image = cv2.imread(path)  
  
# Window name in which image is displayed  
window_name = 'Image'
  
# Creating kernel 
kernel = np.ones((6, 6), np.uint8) 
  
# Using cv2.erode() method  
image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)  
  
# Displaying the image  
cv2.imshow(window_name, image) 
