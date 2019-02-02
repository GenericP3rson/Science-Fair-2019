# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T#datasetForm:tabView:metadataMapTab
# from tflearn.data_utils import load_csv
import numpy as np
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import pandas as pd
from PIL import Image

# data, labels = load_csv('harvard/HAM10000_metadata.csv', target_column=2, categorical_labels=True, n_classes=2)
# So the labels must be an integer. I can either edit the file or read my data in a different way?

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
dataset = pd.read_csv("harvard/HAM10000_metadata.csv") # Opens the dataset
# print(stuff.loc[0]["image_id"])
# Two ways to access: stuff.loc[][] or stuff.iloc[][]
# print(np.asarray(stuff.loc[:, "image_id"]))
limit = 25
lim = 50
image_list = list(dataset.loc[:, "image_id"])[0:limit] # Images in a list
# image_array = np.asarray(dataset.loc[:, "image_id"]) # Images in a numpy array
# These both have the data (I'm not sure how I what to store it)
def convert(labels):
    '''
    This should convert the labels into a format we can use (as in, it'll make integers).
    '''
    '''
    KEY:
    0 Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec), 
    1 basal cell carcinoma (bcc), 
    2 benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl), 
    3 dermatofibroma (df), 
    4 melanoma (mel), 
    5 melanocytic nevi (nv),
    6 vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc).
    '''
    key = [
        ["akiec", [1, 0, 0, 0, 0, 0, 0]], 
        ["bcc", [0, 1, 0, 0, 0, 0, 0]], 
        ["bkl", [0, 0, 1, 0, 0, 0, 0]], 
        ["df", [0, 0, 0, 1, 0, 0, 0]], 
        ["mel", [0, 0, 0, 0, 1, 0, 0]], 
        ["nv", [0, 0, 0, 0, 0, 1, 0]], 
        ["vasc", [0, 0, 0, 0, 0, 0, 1]]
        ]  # This is the key
    # labels = list(dataset.loc[:, "dx"])
    # print(labels)
    index = 0
    for lab in labels: # This is where the converting happens
        for disease in key:
            if lab == disease[0]:
                labels[index] = disease[1]
                break
        index+=1
    # print(labels)
    labels = np.asarray(labels) # Changes it to array
    labels.resize(len(labels), 7) # Makes it 2d
    # print(labels)
    return labels
labels = convert(list(dataset.loc[:, "dx"])[0:limit]) # Inserts the dx column to be converted
print(labels)
test_labels = convert(list(dataset.loc[:, "dx"])[limit+1:lim])

# So I have all the labels in the correct format, now all I have to do is load up the images and put them in the correct format

# ALL IMAGES ARE (600, 450)
fout = open("cancer_photos.txt", "w")
all_pixels = []
for image_name in image_list:
    image = Image.open("harvard/full_set/" + image_name + ".jpg")
    # print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
    # print(image.convert("RGB"))
    # print(list(image.getdata()))
    RGBvalues = list(i[0:3] for i in image.getdata())  # We have a list of the rgb values
    # print(RGBvalues)
    # print(np.asarray(RGBvalues))
    fout.write(' '.join(' '.join(str(j) for j in i) for i in RGBvalues))
    fout.write("\n")
    all_pixels.append(np.asarray(RGBvalues))
    # x = image.size[0]
    # y = image.size[1]
all_pixels = np.asarray(all_pixels)
all_pixels.resize(len(image_list), 600, 450, 3)
print(all_pixels)

all_pixels = all_pixels.reshape([-1, 600, 450, 3])

net = input_data(shape=[None, 600, 450, 3], name='input')

net = conv_2d(net, 100, 2, activation='relu')
net = max_pool_2d(net, 10)

net = conv_2d(net, 200, 2, activation='relu')
net = max_pool_2d(net, 10)

net = fully_connected(net, 1000, activation='relu')
net = dropout(net, 0.65)

net = fully_connected(net, 7, activation='softmax')
net = regression(net, optimizer='adam', learning_rate=0.01,
                     loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(net)

# Run this to train the data
model.fit({'input': all_pixels}, {'targets': labels}, n_epoch=10, 
          snapshot_step=500, show_metric=True, run_id='cancer')

model.save("cancer.model")

# Run this to check the data
# model.load('tfl.model')
# print(np.round(model.predict([test_x[10]])[0]))
# print(test_y[10])
