import numpy as np 
import cv2
import imutils as mu
from matplotlib import pyplot as plt


def extractSkin(image):
    im = image.copy() # Duplicates
    im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV) # Convertion
    '''
    Parameters of HSV: Hue (the colour), saturation and value (how vivd/ Black and White it is)
    '''
    l = np.array([0, 48, 80], dtype=np.uint8)
    u = np.array([20, 255, 255], dtype=np.uint8)

    sk = cv2.inRange(im, l, u) # Makes w/b numpy array

    print(sk)

    mask = cv2.GaussianBlur(sk, (2, 2), 0) # This connects parts

    mask = cv2.bitwise_and(im, im, mask=sk)

    skin = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

    # cv2.imwrite("target.png", mask)
    plt.imshow(cv2.cvtColor(skin, cv2.COLOR_BGR2RGB))


    plt.show()

    # # Extracting skin from the threshold mask
    # skin = cv2.bitwise_and(img, img, mask=skinMask)

    # # Return the Skin image
    # return cv2.cvtColor(skin, cv2.COLOR_HSV2BGR)
    # print(cv2.cvtColor(mask, cv2.COLOR_BGR2HSV))  # Convertion)
    return 0


im = input("Write the image's path: ")
im = cv2.imread(im)


im = mu.resize(im, width=250)

skin = extractSkin(im)
