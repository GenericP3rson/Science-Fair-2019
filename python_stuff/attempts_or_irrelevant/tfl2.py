'''
For whatever reason, this fails to work. It trains the first time around,
but it does several trainings of the network with different Run ids.
'''

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tflearn.datasets.mnist as mnist

X, Y, test_x, test_y = mnist.load_data(one_hot=True)
# Loading in that data!

X = X.reshape([-1, 28, 28, 1])
test_x = test_x.reshape([-1, 28, 28, 1])
# Reshape everything!

net = input_data(shape=[None,28,28,1], name="input")
# Input has the same parameters

net = conv_2d(net, 32, 2, activation = "relu")
net = max_pool_2d(net, 2)

net = conv_2d(net, 64, 2, activation="relu")
net = max_pool_2d(net, 2)

net = fully_connected(net, 1024, activation="relu")
net = dropout(net, 0.8)

net = fully_connected(net, 10, activation="softmax")
net = regression(net, optimizer="adam", learning_rate=0.01, loss="categorical_crossentropy", name="targets")

model = tflearn.DNN(net)

model.fit({'input': X}, {'targets': Y}, n_epoch=2,
          validation_set=({'input': test_x}, {'targets': test_y}),
          snapshot_step=500, show_metric=True, run_id='mnist')
model.fit(X, Y)
# For some reason, this fails to terminate

# model.save('tflearncnn.model')

# model.load('tflearncnn.model')