from PIL import Image
from PIL import ImageFilter
import math

if __name__ == "__main__":
    '''
    This basically just loads the image up
    '''
    image = input("Which image would you like to use? ")
    image = Image.open(image)
    print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
    print(image.convert("RGB"))
    # print(list(image.getdata())) 
    RGBvalues = list(image.getdata()) # We have a list of the rgb values
    x = image.size[0]
    y = image.size[1]
    '''
    Okay, do note that for RGBvalues, there CAN be a 4th value, known as RBGA, A being opacity....
    '''
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
    print(len(Rval), len(Rval[0]), image.size)

def find_max(arr):
    max = 0 # Because it is a range from 0-255, 0 should be fine for the minimum
    for i in arr:
        if i > max:
            max = i
    return max


def kernel(img, kernel_width=10, kernel_height=10, kernel_move_width=10, kernel_move_height=10):
    '''
    The idea behind this function is to take a kernel and do max pooling. 
    If we do do it with the tuple, we could find the maximum red value then find a threshold value.
    '''
    i = 0
    # kernel_width = 3
    # kernel_height = 3
    print(x, y)
    while i < x:
        j = 0
        while j < y:
            # So this will iterate over each set of the points we need. Next we'll have to get those values.
            pts = []
            for k in range(kernel_height):
                for l in range(kernel_width):
                    # So now we've managed to look at every pixel kernel_height by kernel_width at a time.
                    try:
                        pts.append(img[i+k][j+l])
                        # print(i+k, j+l)
                    except:
                        pass
            # print(find_max(pts))
            print(pts)
            j = j+kernel_move_width
        i = i+kernel_move_height  
kernel(Rval, 3, 3)


def max_pooling(img, kernel_width=10, kernel_height=10, kernel_move_width=10, kernel_move_height=10):
    '''
    The idea behind this function is to take a kernel and do max pooling. 
    If we do do it with the tuple, we could find the maximum red value then find a threshold value.
    '''
    i = 0
    # kernel_width = 3
    # kernel_height = 3
    print(x, y)
    while i < x:
        j = 0
        while j < y:
            # So this will iterate over each set of the points we need. Next we'll have to get those values.
            pts = []
            for k in range(kernel_height):
                for l in range(kernel_width):
                    # So now we've managed to look at every pixel kernel_height by kernel_width at a time.
                    try:
                        pts.append(img[i+k][j+l])
                        # print(i+k, j+l)
                    except:
                        pass
            print(find_max(pts))
            j = j+kernel_move_width
        i = i+kernel_move_height


max_pooling(Rval, 3, 3)

def find_circles():
    '''
    So for this one, we need to try to find circles, to identify things such as moles, pimples, etc.
    In short, there are a lots of different types of circles on the human body, so it's important to find them.
    What we're planning to do is to find just circles in black and white. After that, we can identify other things.
    '''
# Or I could just CNN everything?