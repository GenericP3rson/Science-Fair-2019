from __future__ import division, print_function, absolute_import

import numpy as np
import tflearn

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

fin = open("writtendata.txt", "r")

data = []
ans = []
i = 0
for line in fin:
    if i % 2 == 0:
        data.append(line[:-1])
    else:
        ans.append(line[:-1]) # We're basically pushing it without the \n
        # print(len(line[:-1]))
    i+=1

data_new = [i.split() for i in data]

data_new = np.array(data_new)
ans = np.array(ans)

print(len(data_new[0]))







# # Building convolutional network
# network = input_data(shape=[None, 28, 28, 1], name='input')
# network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")
# network = max_pool_2d(network, 2)
# network = local_response_normalization(network)
# network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")
# network = max_pool_2d(network, 2)
# network = local_response_normalization(network)
# network = fully_connected(network, 128, activation='tanh')
# network = dropout(network, 0.8)
# network = fully_connected(network, 256, activation='tanh')
# network = dropout(network, 0.8)
# network = fully_connected(network, 10, activation='softmax')
# network = regression(network, optimizer='adam', learning_rate=0.01,
#                      loss='categorical_crossentropy', name='target')

# # Training
# model = tflearn.DNN(network, tensorboard_verbose=0)
# model.fit({'input': data_new}, {'target': ans}, n_epoch=20,
#           validation_set=({'input': data_new}, {'target': ans}),
#           snapshot_step=100, show_metric=True, run_id='convnet_mnist')


data_new = data_new.reshape([-1, 90, 64, 3])

# print(len(data_new[0]))

# Build neural network
net = tflearn.input_data(shape=[None, 90, 64, 3])
net = tflearn.fully_connected(net, 250)
net = tflearn.fully_connected(net, 250)
net = tflearn.fully_connected(net, 10, activation='softmax')
net = tflearn.regression(net)


# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
# for i in range(1000, 2000):
#     print("TRY #" + str(i))
#     try:
#         model.fit(data_new, ans, n_epoch=100, batch_size=i, show_metric=True)
#         break
#     except:
#         print("FAIL @" + str(i))
model.fit(data_new, ans, n_epoch=100, batch_size=10, show_metric=True)
