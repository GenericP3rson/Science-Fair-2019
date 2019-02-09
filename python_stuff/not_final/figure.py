'''
This should read the data and then put into a neural network.
This is the BIG BOY!!!
This only searches for structures.
'''

import numpy
import tflearn.datasets.mnist as mnist
from tflearn.layers.estimator import regression
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
import tflearn

fin = open("writtendata.txt", "r")
fin1 = open("writtenanswers.txt", "r")

datax = numpy.array([line[:-1].split() for line in fin])
datay = numpy.array([line[:-1].split() for line in fin1])
print(len(datax[0]))

# X, Y, test_x, test_y = mnist.load_data(one_hot=True)
# print(X)

X = datax.reshape([-1, 30, 30, 1])
print(X)
# test_x = test_x.reshape([-1, 28, 28, 1])

convnet = input_data(shape=[None, 30, 30, 1], name='input')
convnet = conv_2d(convnet, 32, 2, activation='relu')
convnet = max_pool_2d(convnet, 2)
convnet = conv_2d(convnet, 64, 2, activation='relu')
convnet = max_pool_2d(convnet, 2)
convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)
convnet = fully_connected(convnet, 1, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=0.01,
                     loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet)

# Run this to train the data
model.fit({'input': X}, {'targets': datay}, n_epoch=10,
          snapshot_step=500, show_metric=True, run_id='neural net')

model.save("tfl.model")

'''
# Run this to check the data
model.load('tfl.model')
print(numpy.round(model.predict([test_x[10]])[0]))
print(test_y[10])
'''