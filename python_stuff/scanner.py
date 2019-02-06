from PIL import Image
# from PIL import ImageFilter
import math


if __name__ == "__main__":
    '''
    This basically just loads the image up
    '''
    image = "ISIC_0024306.jpg"
    image = Image.open(image)
    print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
    # print(image.convert("RGB"))
    # print(list(image.getdata()))
    RGBvalues = list(x[0:3] for x in image.getdata())  # We have a list of the rgb values
    x = image.size[0]
    y = image.size[1]
    # print(RGBvalues)
    rows = []
    for i in range(0, len(RGBvalues), x):
        rows.append(RGBvalues[i:i+x])
    # print(rows)

for i in range(0, len(rows), 10):
    # stuff = [z for z in data[i]]
    print("OK")
    print(i)
    im = Image.new("RGB", (150, 10))
    q = [x for x in rows[i:i+11]]
    print(q)
    # im.putdata([x for x in rows[i:i+11]])
    # im.save("pix" + str(i) + ".png")
