# '''
# WARNING: I DID TAKE THIS CODE
# '''


import numpy as np
import cv2
from sklearn.cluster import KMeans
from collections import Counter
import imutils as mu
import pprint
from matplotlib import pyplot as plt


def extractSkin(image):
    # Taking a copy of the image
    img = image.copy()
    # Converting from BGR Colours Space to HSV
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    '''
    Parameters of HSV: Hue (the colour), saturation and value (how vivd/ Black and White it is)
    '''

    # Defining HSV Threadholds
    lower_threshold = np.array([0, 48, 80], dtype=np.uint8) # These make a numpy array of the values
    upper_threshold = np.array([20, 255, 255], dtype=np.uint8)

    # # Single Channel mask,denoting presence of colours in the about threshold
    skinMask = cv2.inRange(img, lower_threshold, upper_threshold)

    # print(skinMask)

    # # Cleaning up mask using Gaussian Filter
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)

    # # Extracting skin from the threshold mask
    skin = cv2.bitwise_and(img, img, mask=skinMask)

    # # Return the Skin image
    return cv2.cvtColor(skin, cv2.COLOR_HSV2BGR)
    # return 0

def compare(li1, li2): 
    return Counter(li1) == Counter(li2)

def removeBlack(estimator_labels, estimator_cluster):

    # Check for black
    hasBlack = False

    # Get the total number of occurance for each color
    bow = Counter(estimator_labels)
    # print(occurance_counter)
    # print(bow)

    #   # Loop through the most common occuring color
    for x in bow.most_common(len(estimator_cluster)):

        # Quick List comprehension to convert each of RBG Numbers to int
        color = [int(i) for i in estimator_cluster[x[0]].tolist()]

        # Check if the color is [0,0,0] that if it is black
        if compare(color, [0, 0, 0]):
            # delete the occurance
            del bow[x[0]]
            # remove the cluster
            hasBlack = True
            estimator_cluster = np.delete(estimator_cluster, x[0], 0)
            break

    return (bow, estimator_cluster, hasBlack)
    '''
    ENDED HERE
    '''
    # return (0, 0, 0)


def getColorInformation(estimator_labels, estimator_cluster, hasThresholding=False):

    # Variable to keep count of the occurance of each color predicted
    occurance_counter = None

    # Output list variable to return
    colorInformation = []

    #Check for Black
    hasBlack = False

    # If a mask has be applied, remove the black
    if hasThresholding == True:

        (occurance, cluster, black) = removeBlack(
            estimator_labels, estimator_cluster)
        occurance_counter = occurance # The counter of how common everything is
        estimator_cluster = cluster # A 2d array of RGB values
        hasBlack = black # Where there is black or not (True)
    print(occurance_counter)
    print(estimator_cluster)
#   else:
#     occurance_counter = Counter(estimator_labels)
    # print(occu)
    # Get the total sum of all the predicted occurances
    totalOccurance = sum(occurance_counter.values()) 

    print(totalOccurance)

#   # Loop through all the predicted colors
    for x in occurance_counter.most_common(len(estimator_cluster)): # So it looks at the list in order from most to least common
        print(x)
        index = (int(x[0])) - 1 # This is its number

        # # Quick fix for index out of bound when there is no threshold
        # index = (index-1) if ((hasThresholding & hasBlack) & (int(index) != 0)) else index

        # Converts colour from a np array to a list
        color = estimator_cluster[index].tolist()
        print(color)

        # Get the percentage of each color
        color_percentage = (x[1]/totalOccurance) # %

        # #make the dictionay of the information
        colorInfo = {"cluster_index": index, "color": color, "color_percentage": color_percentage}

        # # Add the dictionary to the list
        colorInformation.append(colorInfo)

    print(colorInformation)
    return colorInformation


def extractDominantColor(image, number_of_colors=5, hasThresholding=False):

    # Quick Fix Increase cluster counter to neglect the black, or not skin
    if hasThresholding == True:
        number_of_colors += 1

    # Taking Copy of the image
    img = image.copy()

    # Convert Image into RGB Colour Space
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # print(img.shape)

    # This compresses the image into the dimensions, but then with the 3 RGB values
    img = img.reshape((img.shape[0]*img.shape[1]), 3)

    # print(img.shape)

    # #Initiate KMeans Object
    estimator = KMeans(n_clusters=number_of_colors, random_state=0)
    '''
    So, here's what happens: it changes the labels to be a number 0-num. 
    The cluster_centers_ is the average of these
    '''

    # print(estimator)

    # # Fit the imageL:: THIS DOES THE MAJIC
    estimator.fit(img)
    # for i in img:
    #     print(i)
    # print(estimator)
    # print(estimator.labels_)
    # for i in estimator.cluster_centers_:
    #     print(i)
    # # Get Colour Information
    colorInformation = getColorInformation(
        estimator.labels_, estimator.cluster_centers_, hasThresholding)
    return colorInformation


def plotColorBar(colorInformation): # Just a visual
    #Create a 500x100 black image
    color_bar = np.zeros((100, 500, 3), dtype="uint8")

    top_x = 0
    for x in colorInformation:
        bottom_x = top_x + (x["color_percentage"] * color_bar.shape[1])

        color = tuple(map(int, (x['color'])))

        cv2.rectangle(color_bar, (int(top_x), 0),
                    (int(bottom_x), color_bar.shape[0]), color, -1)
        top_x = bottom_x
    return color_bar


def prety_print_data(color_info): # Function for making it look nice???
    for x in color_info:
        print(pprint.pformat(x))
        print()


# '''
# Skin Image Primary : https://raw.githubusercontent.com/octalpixel/Skin-Extraction-from-Image-and-Finding-Dominant-Color/master/82764696-open-palm-hand-gesture-of-male-hand_image_from_123rf.com.jpg
# Skin Image One     : https://raw.githubusercontent.com/octalpixel/Skin-Extraction-from-Image-and-Finding-Dominant-Color/master/skin.jpg
# Skin Image Two     : https://raw.githubusercontent.com/octalpixel/Skin-Extraction-from-Image-and-Finding-Dominant-Color/master/skin_2.jpg
# Skin Image Three   : https://raw.githubusercontent.com/octalpixel/Skin-Extraction-from-Image-and-Finding-Dominant-Color/master/Human-Hands-Front-Back-Image-From-Wikipedia.jpg

# '''


# Get Image from URL. If you want to upload an image file and use that comment the below code and replace with  image=cv2.imread("FILE_NAME")
image = input("Write the image's path: ")
image = cv2.imread(image) # This opens the image in the form of a numpy array 

image = mu.resize(image, width=250)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show() # Changes it to RGB and displays the original image


# # Apply Skin Mask
skin = extractSkin(image)

plt.imshow(cv2.cvtColor(skin, cv2.COLOR_BGR2RGB))
plt.show()


# # Find the dominant color. Default is 1 , pass the parameter 'number_of_colors=N' where N is the specified number of colors
dominantColors = extractDominantColor(skin, hasThresholding=True)


# #Show in the dominant color information
print("Color Information")
prety_print_data(dominantColors) # It just makes it look fancier


# #Show in the dominant color as bar
print("Color Bar")
colour_bar = plotColorBar(dominantColors)
plt.axis("off")
plt.imshow(colour_bar)
plt.show()
