from PIL import Image

fout = open("writtendata.txt", "w")
# num = 0
# num2 = 1
for j in range(10):
    for i in range(9):
        print(j, i+1)
        image = Image.open("numbers/" + str(j) + "." + str(i+1) + ".png")
        RGBvalues = list(image.getdata()) # Gets the data
        # fout.write('; '.join(', '.join(str(i) for i in e) for e in RGBvalues))
        # fout.write(": " + str(j) + "\n")
        RGBvalues = [e[0:3] for e in RGBvalues]
        fout.write(' '.join(' '.join(str(i) for i in e) for e in RGBvalues))
        fout.write("\n" + str(j) + "\n")
# print(image.convert("RGB"))
# print(list(image.getdata()))
# RGBvalues = list(image.getdata())  # We have a list of the rgb values
# x = image.size[0]
# y = image.size[1]
# print(RGBvalues)
