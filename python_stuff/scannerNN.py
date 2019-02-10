# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T#datasetForm:tabView:metadataMapTab
# from tflearn.data_utils import load_csv
import numpy as np
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import pandas as pd
from PIL import Image
import random

# data, labels = load_csv('harvard/HAM10000_metadata.csv', target_column=2, categorical_labels=True, n_classes=2)
# So the labels must be an integer. I can either edit the file or read my data in a different way?

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html


# def open_and_random(dataset):
#     '''
#     This will open a CSV, mix it, then turn it back into a DataFrame.
#     '''
#     dataset = pd.read_csv(dataset)  # Opens the dataset
#     dataset = [dataset.iloc[i] for i in range(len(dataset))]
#     random.shuffle(dataset)  # Shuffles the dataset
#     al = []
#     for row in range(len(dataset[0])):
#         mini = []
#         for i in dataset:
#             mini.append(i[row])
#         al.append(mini)
#     df = pd.DataFrame({"image_id": al[1]})
#     df["dx"] = al[2]
#     print(df)
#     return df


# dataset = open_and_random("harvard/HAM10000_metadata.csv")
# # print(stuff.loc[0]["image_id"])
# # Two ways to access: stuff.loc[][] or stuff.iloc[][]
# # print(np.asarray(stuff.loc[:, "image_id"]))
# data_limit_low = 0
# data_limit_mid1 = 10000
# data_limit_mid2 = 10000
# data_limit_hi = 10015
# data = list(dataset.loc[:, "image_id"])  # Images in a list
# image_list = data[data_limit_low:data_limit_mid1]
# test_images = data[data_limit_mid2:data_limit_hi]
# all_labels = list(dataset.loc[:, "dx"])
# labels = all_labels[data_limit_low:data_limit_mid1]
# test_labels = all_labels[data_limit_mid2:data_limit_hi]


# # image_array = np.asarray(dataset.loc[:, "image_id"]) # Images in a numpy array
# # These both have the data (I'm not sure how I what to store it)
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
#     key = [
#         ["akiec", [1, 0, 0, 0, 0, 0, 0]],
#         ["bcc", [0, 1, 0, 0, 0, 0, 0]],
#         ["bkl", [0, 0, 1, 0, 0, 0, 0]],
#         ["df", [0, 0, 0, 1, 0, 0, 0]],
#         ["mel", [0, 0, 0, 0, 1, 0, 0]],
#         ["nv", [0, 0, 0, 0, 0, 1, 0]],
#         ["vasc", [0, 0, 0, 0, 0, 0, 1]]
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
#     labels.resize(len(labels), 7)  # Makes it 2d
#     print(labels)
#     return labels


# labels = convert(labels)  # Inserts the dx column to be converted
# # print(labels)
# test_labels = convert(test_labels)

# # So I have all the labels in the correct format, now all I have to do is load up the images and put them in the correct format


# def convert_data(image_list):
#     '''
#     This converts the image names (in a list) to an array of pixels.
#     This also writes everything to "cancer_photos.txt" 'cause why not?
#     '''
#     # ALL IMAGES ARE (600, 450)
#     # fout = open("cancer_photos.txt", "w")
#     all_pixels = []
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
#     all_pixels = np.asarray(all_pixels)
#     all_pixels.resize(len(image_list), x, y, 3)
#     print(all_pixels)
#     return all_pixels


# all_pixels = convert_data(image_list)
# test_pixel = convert_data(test_images)


# all_pixels = all_pixels.reshape([-1, 150, 150, 3])


net = input_data(shape=[None, 150, 150, 3], name='input')

net = conv_2d(net, 50, 2, activation='relu')
net = max_pool_2d(net, 10)

net = conv_2d(net, 200, 2, activation='relu')
net = max_pool_2d(net, 10)

net = fully_connected(net, 500, activation='relu')
net = dropout(net, 0.75)

net = fully_connected(net, 7, activation='softmax')
net = regression(net, optimizer='adam', learning_rate=0.001,
                 loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(net)

'''
# Run this to train the data
model.fit({'input': all_pixels}, {'targets': labels}, n_epoch=100, validation_set=({'input': test_pixel}, {'targets': test_labels}),
          snapshot_step=500, show_metric=True, run_id='cancer')
model.save("cancer.model")
'''

# Run this to check the data
model.load('cancer.model')

if __name__ == "__main__":
    '''
    This basically just loads the image up
    '''
    image = input("Which image do you want? ")
    image = Image.open(image)
    print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
    print("Thank you. Please wait; this might take a while...")
    # print(image.convert("RGB"))
    # print(list(image.getdata()))
    # We have a list of the rgb values
    RGBvalues = list(x[0:3] for x in image.getdata())
    x = image.size[0]
    y = image.size[1]
    # print(RGBvalues)
    rows = []
    for i in range(0, len(RGBvalues), x):
        rows.append(RGBvalues[i:i+x])
    # print(len(rows[0]))

left_right = 50
# j = 50
# for j in range(left_right, 151, left_right):
# # im.putdata(rows[i] for i in range(10))
# x = 0


def scanner(dimx=150, dimy=150, xmove=100, ymove=100):
    q = 0
    # move = 100
    everything = []
    for le in range(0, len(rows)-dimy, ymove):
        for x in range(0, len(rows[0]) - dimx, xmove):
            # im = Image.new("RGB", (dimx, dimy))
            total = []
            for i in range(le, le+dimy):
                total += rows[i][x:x+dimx]
                # print(i, x, x+150)
            # im.putdata(total)
            everything.append(total)
            # im.save("test"+str(q)+".png") 
            q += 1
    return everything


ans = scanner(150, 150, 50, 50)

values = [list(model.predict([np.asarray(i).reshape(150, 150, 3)])[0]) for i in ans]
print(values)
