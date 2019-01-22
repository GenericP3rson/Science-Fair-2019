from PIL import Image
from PIL import ImageFilter
import math

# image = input("Which image would you like to use? ")
image = Image.open("images/numbers/0.1.png")
# print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
# print(image.convert("RGB"))
# print(list(image.getdata()))
RGBvalues = list(image.getdata())  # We have a list of the rgb values
# print(RGBvalues)
x = image.size[0]
y = image.size[1]
Rval = []
Gval = []
Bval = []
extra = 0
for i in range(x):
    Rhold = []
    Ghold = []
    Bhold = []
    for j in range(y):
        Rhold.append(image.getdata()[j+extra][0])
        Ghold.append(image.getdata()[j+extra][1])
        Bhold.append(image.getdata()[j+extra][2])
    Rval.append(Rhold)
    Gval.append(Ghold)
    Bval.append(Bhold)
    extra = extra + y
# print(Rval)
# print(len(Rval), len(Rval[0]), image.size)
grey = [((i[0]+i[1]+i[2])/3)/255 for i in image.getdata()]
print(grey)
''' Makes it grey '''
ideal = [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0,
1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 
1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0]

print(grey-ideal)