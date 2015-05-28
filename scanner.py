__author__ = 'Yan'

from pytesser import *
from PIL import Image

# read the test image file and use OCR to get its content
def imageReader():
    image = Image.open('phototest.tif')
    content = image_to_string(image)
    return content
