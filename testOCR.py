from pytesser import *
from PIL import Image

# read the 
# image = Image.open('fnord.tif')
image = Image.open('phototest.tif')
print image_to_string(image)

