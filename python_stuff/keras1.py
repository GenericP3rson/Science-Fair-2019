# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from PIL import Image
import random
import os

# data, labels = load_csv('harvard/HAM10000_metadata.csv', target_column=2, categorical_labels=True, n_classes=2)
# So the labels must be an integer. I can either edit the file or read my data in a different way?

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html


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
    print("Processing the labels...")
    key = [
        ["akiec", [1, 0, 0, 0, 0, 0, 0, 0]],
        ["bcc", [0, 1, 0, 0, 0, 0, 0, 0]],
        ["bkl", [0, 0, 1, 0, 0, 0, 0, 0]],
        ["df", [0, 0, 0, 1, 0, 0, 0, 0]],
        ["mel", [0, 0, 0, 0, 1, 0, 0, 0]],
        ["nv", [0, 0, 0, 0, 0, 1, 0, 0]],
        ["vasc", [0, 0, 0, 0, 0, 0, 1, 0]],
        ["skin", [0, 0, 0, 0, 0, 0, 0, 1]]
    ]  # This is the key
    # labels = list(dataset.loc[:, "dx"])
    # print(labels)
    index = 0
    for lab in labels:  # This is where the converting happens
        for disease in key:
            if lab == disease[0]:
                labels[index] = disease[1]
                break
        index += 1
    # print(labels)
    labels = np.asarray(labels)  # Changes it to array
    labels.resize(len(labels), 8)  # Makes it 2d
    print(labels)
    return labels


# labels = convert(labels)  # Inserts the dx column to be converted
# # print(labels)
# test_labels = convert(test_labels)

# So I have all the labels in the correct format, now all I have to do is load up the images and put them in the correct format


# def convert_data(image_list):
#     '''
#     This converts the image names (in a list) to an array of pixels.
#     This also writes everything to "cancer_photos.txt" 'cause why not?
#     '''
#     print("Processing the data...")
#     # ALL IMAGES ARE (600, 450)
#     # fout = open("cancer_photos.txt", "w")
#     all_pixels = []
#     tot = len(image_list)
#     i = 1
#     for image_name in image_list:
#         image = Image.open("harvard/mini_set/" + image_name + ".jpg")
#         # print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
#         # print(image.convert("RGB"))
#         # print(list(image.getdata()))
#         # We have a list of the rgb values
#         RGBvalues = list((i[0]/255, i[1]/255, i[2]/255)
#                          for i in image.getdata())
#         # print(RGBvalues)
#         # print(np.asarray(RGBvalues))
#         # fout.write(' '.join(' '.join(str(j) for j in i) for i in RGBvalues))
#         # fout.write("\n")
#         all_pixels.append(np.asarray(RGBvalues))
#         x = image.size[0]
#         y = image.size[1]
#         print(str(i) + "/" + str(tot))
#         i += 1
#     all_pixels = np.asarray(all_pixels)
#     all_pixels.resize(len(image_list), x, y, 3)
#     print(all_pixels)
#     return all_pixels


def open_and_random(dataset):
    '''
    This will open a CSV, split it into two sections, mix it, then turn it back into a DataFrame.
    '''
    print("Opening Dataset...")
    dataset = pd.read_csv(dataset)  # Opens the dataset
    dataset = [dataset.iloc[i] for i in range(len(dataset))]
    # print(dataset)
    # random.shuffle(dataset)  # Shuffles the dataset
    canc = [
        ["akiec", [], [[1], [0], [0], [0], [0], [0], [0], [0]]],
        ["bcc", [], [[0], [1], [0], [0], [0], [0], [0], [0]]],
        ["bkl", [], [[0], [0], [1], [0], [0], [0], [0], [0]]],
        ["df", [], [[0], [0], [0], [1], [0], [0], [0], [0]]],
        ["mel", [], [[0], [0], [0], [0], [1], [0], [0], [0]]],
        ["nv", [], [[0], [0], [0], [0], [0], [1], [0], [0]]],
        ["vasc", [], [[0], [0], [0], [0], [0], [0], [1], [0]]],
        ["skin", [], [[0], [0], [0], [0], [0], [0], [0], [1]]]
    ]  # This is the key
    # canc = [["akiec", []], ["bcc", []], ["bkl", []], [
    # "df", []], ["mel", []], ["nv", []], ["vasc", []]]
    for row in dataset:  # Looks at each point in dataset
        for dis in canc:  # Looks at each disease in the cancer
            # If the row's cancer is the cancer in the dataset, append to canc.
            if (row[2] == dis[0]):
                # Just adding the image and cancer, 'cause that's all we need
                dis[1].append([row[1], dis[2]])
                break
    print(canc)
    # Now that they are separated, we should partition the data.
    all_test = []
    all_train = []
    for data in canc:
        l = round(len(data[1])/2)
        train_data = data[1][:l]  # Splits the two roughly in half
        test_data = data[1][l:]
        data.append(train_data)
        data.append(test_data)  # Adds it into the canc list
        all_test += test_data
        all_train += train_data
    print(canc)
    print(len(canc[0]))
    random.shuffle(all_test)
    random.shuffle(all_train)  # Mixing the two datasets
    test_data = [i[0] for i in all_test]  # Adds all the testing data
    test_labels = [i[1] for i in all_test]  # Adds all the labels
    train_data = [i[0] for i in all_train]
    train_labels = [i[1] for i in all_train]
    traindf = pd.DataFrame({"image_id": train_data})
    traindf["dx"] = train_labels
    testdf = pd.DataFrame({"image_id": test_data})
    testdf["dx"] = test_labels
    # print(testdf, traindf)
    return [traindf, testdf]


train, test = open_and_random("harvard/HAM10000_metadata.csv")


def add_skin(p):
    '''
    This should add the skin.
    '''
    img_names = []
    for i in os.listdir(p):
        if (i != ".DS_Store"):
            img_names.append(i)
    random.shuffle(img_names)
    x = round((len(os.listdir(p))-1)/2)  # -- because of .DS_Store
    train_x = img_names[:x]
    test_x = img_names[x:]
    train_y = [[[0], [0], [0], [0], [0], [0], [0], [1]] for i in train_x]
    test_y = [[[0], [0], [0], [0], [0], [0], [0], [1]] for i in test_x]
    return [train_x, test_x, train_y, test_y]


trx, tx, tray, ty = add_skin("SKIN")
# dataset = open_and_random("harvard/HAM10000_metadata.csv")
# print(stuff.loc[0]["image_id"])
# Two ways to access: stuff.loc[][] or stuff.iloc[][]
# print(np.asarray(stuff.loc[:, "image_id"]))
# data_limit_low = 0
# data_limit_mid1 = 10000
# data_limit_mid2 = 10000
# data_limit_hi = 10015
# data = list(dataset.loc[:, "image_id"])  # Images in a list
image_list = list(train.loc[:, "image_id"]) + trx
test_images = list(test.loc[:, "image_id"]) + tx
# all_labels = list(dataset.loc[:, "dx"])
labels = list(train.loc[:, "dx"]) + tray
test_labels = list(test.loc[:, "dx"]) + ty

ok = len(labels)

print(labels)

labels = np.asarray(labels)

print(labels)

# labels.reshape(ok, 8, 1)

# print(labels)

# image_array = np.asarray(dataset.loc[:, "image_id"]) # Images in a numpy array
# These both have the data (I'm not sure how I what to store it)


# def convert(labels):
#     '''
#     This should convert the labels into a format we can use (as in, it'll make integers).
#     '''
#     '''
#     KEY:
#     0 Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec),
#     1 basal cell carcinoma (bcc),
#     2 benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl),
#     3 dermatofibroma (df),
#     4 melanoma (mel),
#     5 melanocytic nevi (nv),
#     6 vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc).
#     '''
#     print("Processing the labels...")
#     key = [
#         ["akiec", [1, 0, 0, 0, 0, 0, 0, 0]],
#         ["bcc", [0, 1, 0, 0, 0, 0, 0, 0]],
#         ["bkl", [0, 0, 1, 0, 0, 0, 0, 0]],
#         ["df", [0, 0, 0, 1, 0, 0, 0, 0]],
#         ["mel", [0, 0, 0, 0, 1, 0, 0, 0]],
#         ["nv", [0, 0, 0, 0, 0, 1, 0, 0]],
#         ["vasc", [0, 0, 0, 0, 0, 0, 1, 0]],
#         ["skin", [0, 0, 0, 0, 0, 0, 0, 1]]
#     ]  # This is the key
#     # labels = list(dataset.loc[:, "dx"])
#     # print(labels)
#     index = 0
#     for lab in labels:  # This is where the converting happens
#         for disease in key:
#             if lab == disease[0]:
#                 labels[index] = disease[1]
#                 break
#         index += 1
#     # print(labels)
#     labels = np.asarray(labels)  # Changes it to array
#     labels.resize(len(labels), 8)  # Makes it 2d
#     print(labels)
#     return labels


# labels = convert(labels)  # Inserts the dx column to be converted
# print(labels)
# test_labels = convert(test_labels)

# So I have all the labels in the correct format, now all I have to do is load up the images and put them in the correct format


def convert_data(image_list):
    '''
    This converts the image names (in a list) to an array of pixels.
    This also writes everything to "cancer_photos.txt" 'cause why not?
    '''
    print("Processing the data...")
    # ALL IMAGES ARE (600, 450)
    # fout = open("cancer_photos.txt", "w")
    all_pixels = []
    tot = len(image_list)
    i = 1
    for image_name in image_list:
        image = Image.open("harvard/mini_set/" + image_name + ".jpg")
        # print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        # print(image.convert("RGB"))
        # print(list(image.getdata()))
        # We have a list of the rgb values
        RGBvalues = list((i[0]/255, i[1]/255, i[2]/255)
                         for i in image.getdata())
        # print(RGBvalues)
        # print(np.asarray(RGBvalues))
        # fout.write(' '.join(' '.join(str(j) for j in i) for i in RGBvalues))
        # fout.write("\n")
        all_pixels.append(np.asarray(RGBvalues))
        x = image.size[0]
        y = image.size[1]
        print(str(i) + "/" + str(tot))
        i += 1
    all_pixels = np.asarray(all_pixels)
    all_pixels.resize((len(image_list), x, y, 3))
    print(all_pixels)
    print(all_pixels.shape())
    return all_pixels


all_pixels = convert_data(image_list)
test_pixel = convert_data(test_images)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(50, 50, 3)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(8, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# print(all_pixels.shape())
print(labels.shape())
model.fit(all_pixels, labels, epochs=2)
model.save("trained_NN/keras/cancer.h5")
model = model.to_json()
model.save("trained_NN/keras/cancer.json")

# test_loss, test_acc = model.evaluate(test_images, test_labels)

# print('Test accuracy:', test_acc)
