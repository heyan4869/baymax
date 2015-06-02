import numpy as np
import cv2

img = cv2.imread('cc.jpg',0)
cv2.imshow('cc',img)
cv2.waitKey(0)
cv2.destroyAllWindows()