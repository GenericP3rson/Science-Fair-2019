import os
from PIL import Image 

for i in os.listdir("harvard/mini_set"):
    if (Image.open(i).size != 200*200):
        print(i)