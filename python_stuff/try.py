from PIL import Image
from PIL import ImageFilter
import math


image = Image.open('blue.jpg')
print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
print(image.convert("RGB"))
print(str(image.getdata()))