__author__ = 'Yan'

import numpy as np
import cv2

# camera number 0 is the integrated web cam on my macbook
cameraPort = 0

# number of frames to throw away while the camera adjusts to light levels
rampFrames = 30

# now we can initialize the camera capture object with the cv2.VideoCapture class
# all it needs is the index to a camera port.
currCamera = cv2.VideoCapture(cameraPort)

# captures a single image from the camera and returns it in PIL format
def takeImage():
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = currCamera.read()
    return im

# ramp the camera then these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(rampFrames):
    temp = takeImage()
    print("Taking image...")

# take the actual image we want to keep
cameraCapture = takeImage()
file = "/Users/Yan/Desktop/testImage.png"

# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, cameraCapture)

# release the camera, otherwise you won't be able to create a new
# capture object as long as the script exits
del(currCamera)
