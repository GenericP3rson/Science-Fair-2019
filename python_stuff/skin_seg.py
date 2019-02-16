# skin_seg.py
import numpy as np
import tflearn as tfl
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import pandas as pd
from PIL import Image
import random
import os
# p = "Face_Dataset/Pratheepan_Dataset/FacePhoto"

inp = []  # The actual
outp = []  # The Black and White
test_x = []  # Actual image
test_y = []  # B and W
# image_x =
# image_y =


def unpack(p, sing=False):
        '''
        Given a folder, this will return a numpy array of the images broken into a list of tuples with RGB values.
        It is reshaped and everything; idealy formatted!
        '''
        if (sing):
                print("Opening labels...")
        else:
                print("Opening images...")
        ans = []
        num_of_pics = 0
        for i in os.listdir(p):
                if (i != ".DS_Store"):
                        image = Image.open(p + "/" + i)
                        x = image.size[0]
                        y = image.size[1]
                        # print(x,y)
                        if (sing):
                                w = (np.asarray(
                                    list(j[0]/255 for j in image.getdata())))
                                w.reshape([x, y, 1])
                                ans.append(w)
                        else:
                                w = np.asarray(
                                    list((j[0]/255, j[1]/255, j[2]/255) for j in image.getdata()))
                                w.reshape([x, y, 3])
                                ans.append(w)
                        num_of_pics += 1
                        print(str(num_of_pics) + "/" + str(len(os.listdir(p))))
        ans = np.array(ans)
        if (sing):
                ans.resize([num_of_pics, 750*500])
        else:
                ans.resize([num_of_pics, 750, 500, 3])
        return ans

# print(outp)


# 1) INPUT PIXELS
# outp = unpack("Face_Dataset/Pratheepan_Dataset/FacePhoto")
inp = unpack("Face_Dataset.1/FacePhoto/Real")

# 2) INPUT PIXEL LABELS
# inp = unpack("Face_Dataset/Ground_Truth/GroundT_FacePhoto", True)
outp = unpack("Face_Dataset.1/FacePhoto/BW", True)

print(outp)

# 3) NN
width = 750
height = 500
inp = inp.reshape([-1, width, height, 3])
net = input_data(shape=[None, width, height, 3], name="input")
net = fully_connected(net, 1048, activation="relu")
net = dropout(net, 0.5)
net = fully_connected(net, 500, activation="relu")
net = dropout(net, 0.5)
net = fully_connected(net, 1048, activation="relu")
net = dropout(net, 0.5)
net = fully_connected(net, width*height, activation="softmax")
net = regression(net, optimizer="adam", learning_rate=0.001,
                 loss="categorical_crossentropy", name="output")
mod = tfl.DNN(net)
# mod.fit({"input": inp}, {"output": outp}, validation_set=({"input": test_x}, {"output": test_y}),
#         n_epoch=100, show_metric=True, run_id="skin_seg", snapshot_step=5000)
mod.fit({"input": inp}, {"output": outp}, n_epoch=100,
        show_metric=True, run_id="skin_seg", snapshot_step=5000)
mod.save("sem_seg_skin.model")

mod.load("sem_seg_skin.model")
print("Now for the testing")
print(mod.predict([test_x[0]])[0])
print(test_y[0])
print(mod.predict([test_x[1]])[0])
print(test_y[1])
print(mod.predict([test_x[2]])[0])
print(test_y[2])
