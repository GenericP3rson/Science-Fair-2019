import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import numpy as np

# all_pixels = all_pixels.reshape([-1, IMAGE_SIZE, IMAGE_SIZE, 3])
# test_pixels = all_pixels.reshape([-1, IMAGE_SIZE, IMAGE_SIZE, 3])

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

model.load('cancer.model')
print(model.predict(['''INSERT TEST DATA HERE'''])[0])