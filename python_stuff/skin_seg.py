import numpy as np
import tflearn as tfl
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import pandas as pd
from PIL import Image
import random
import os
p = "Face_Dataset/Pratheepan_Dataset/FacePhoto"
for i in os.listdir(p):
    # if (i != ".DS_Store")

inp, outp, test_x, test_y = [[0], [0], [0], [0]]



# 1) INPUT PIXELS
# 2) INPUT PIXEL LABELS
# 3) NN
width = 100 # I don't know for now
height = 100  # I don't know for now
net = input_data(shape=[None, width, height, 3], name="input")
net = fully_connected(net, 1048, activation="relu")
net = dropout(net, 0.5)
net = fully_connected(net, 500, activation="relu")
net = dropout(net, 0.5)
net = fully_connected(net, 1048, activation="relu")
net = dropout(net, 0.5)
net = fully_connected(net, width*height, activation="softmax")
net = regression(net, optimizer="adam", learning_rate=0.001, loss="categorical_crossentropy", name="output")
mod = tfl.DNN(net)
mod.fit({"input": inp}, {"output": outp}, validation_set=({"input": test_x}, {"output": test_y}), 
        n_epoch=100, show_metric=True, run_id="skin_seg", snapshot_step=5000)
mod.save("sem_seg_skin.model")

mod.load("sem_seg_skin.model")
print("Now for the testing")
print(mod.predict([test_x[0]])[0])
print(test_y[0])
print(mod.predict([test_x[1]])[0])
print(test_y[1])
print(mod.predict([test_x[2]])[0])
print(test_y[2])
