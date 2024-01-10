import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("C:\\Users\\abhis\\Pictures\\Purple_flower_(4764445139).jpg")
RGB_img=cv.cvtcolor(img,CV.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.waitforbuttonpress()
plt.close()
