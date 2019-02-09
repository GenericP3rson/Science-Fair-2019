'''
This will gather the pixel information from each image in a folder.
'''

from PIL import Image
import os

fout = open("writtendata.txt", "w")
fout1 = open("writtenanswers.txt", "w")
# num = 0
# num2 = 1
# for j in range(10):
#     for i in range(9):
#         print(j, i+1)
#         image = Image.open("numbers/" + str(j) + "." + str(i+1) + ".png")
#         RGBvalues = list(image.getdata())  # Gets the data
#         # fout.write('; '.join(', '.join(str(i) for i in e) for e in RGBvalues))
#         # fout.write(": " + str(j) + "\n")
#         RGBvalues = [e[0:3] for e in RGBvalues]
#         fout.write(' '.join(' '.join(str(i) for i in e) for e in RGBvalues))
#         fout.write("\n" + str(j) + "\n")
path = "data/melanoma"
i = 0
for filename in os.listdir(path): # This looks at all the images with melanomas
    if (i):
        image = Image.open(path + "/" + filename)
        RGBvalues = list(image.getdata()) # Gets the data
        RGBvalues = [(e[0]+e[1]+e[2])/3 for e in RGBvalues] # Makes it grey
        # print(RGBvalues)
        fout.write(' '.join(str(i) for i in RGBvalues))
        fout.write("\n")
        fout1.write("1\n")
    i+=1
good_path = "data/skin"
i = 0
for filename in os.listdir(good_path): # This looks at all the normal-skinned things.
    if (i):
        image = Image.open(good_path + "/" + filename)
        RGBvalues = list(image.getdata())  # Gets the data
        RGBvalues = [(e[0]+e[1]+e[2])/3 for e in RGBvalues]  # Makes it grey
        # print(RGBvalues)
        fout.write(' '.join(str(i) for i in RGBvalues))
        fout.write("\n")
        fout1.write("0\n")
    i += 1
# print(image.convert("RGB"))
# print(list(image.getdata()))
# RGBvalues = list(image.getdata())  # We have a list of the rgb values
# x = image.size[0]
# y = image.size[1]
# print(RGBvalues)
