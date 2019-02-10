from PIL import Image
# from PIL import ImageFilter
import math


if __name__ == "__main__":
    '''
    This basically just loads the image up
    '''
    image = input("Which image do you want? ")
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
    print(len(rows[0]))

left_right = 50
# j = 50
# for j in range(left_right, 151, left_right):
# # im.putdata(rows[i] for i in range(10))
# x = 0

def scanner(dimx = 150, dimy = 150, xmove = 100, ymove = 100):
    q = 0
    # move = 100
    for le in range(0, len(rows)-dimy, ymove):
        for x in range(0, len(rows[0]) - dimx, xmove):
            im = Image.new("RGB", (dimx, dimy))
            total = []
            for i in range(le, le+dimy):
                total += rows[i][x:x+dimx]
                # print(i, x, x+150)
            im.putdata(total)
            im.save("test"+str(q)+".png")
            q += 1
scanner(150, 150, 50, 50)

'''
# Final!
q = 0
move = 100
for le in range(0, len(rows)-150, move):
    for x in range(0, len(rows[0]) - 150, move):
        im = Image.new("RGB", (150, 150))
        total = []
        for i in range(le, le+150):
            total += rows[i][x:x+150]
            print(i, x, x+150)
        im.putdata(total)
        im.save("test"+str(q)+".png")
        q += 1
'''

'''
# Yay! This actually works for going left to right!
q = 0
for x in range(0, len(rows[0]) - 150, 150):
    im = Image.new("RGB", (150, 150))
    total = []
    for i in range(150):
        total += rows[i][x:x+150]
    im.putdata(total)
    im.save("test"+str(q)+".png")
    q+=1
'''

'''
# This Stuff Works
total = []
for i in range(150):
    total += rows[i][:150]
    # print(i, j-left_right, j)
im.putdata(total)
im.save("test"+str(j)+".png")
'''
    # print(j-left_right, j)
# for i in range(0, len(rows), 10):
#     # stuff = [z for z in data[i]]
#     # print("OK")
#     # print(i)
#     im = Image.new("RGB", (150, 10))
#     q = [x for x in rows[i:i+11]]
#     # print(q)
#     im.putdata([x for x in rows[i:i+11]])
#     im.save("pix" + str(i) + ".png")
