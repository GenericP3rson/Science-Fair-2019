import tensorflow as tf 
import numpy as np 

# Random points
datax = np.float32(np.random.rand(2, 100))
datay = np.dot([0.1, 0.2], datax) * 0.3
# So w1 is 0.1, w2 is 0.2, and bias is 0.3

b = tf.Variable(tf.zeros(1))
w = tf.Variable(tf.random_uniform([1, 2], -1, 1))
y = tf.matmul(w, datax) + b # This mulitplies the x and w and then add the bias
# print (b, w, y)

loss = tf.reduce_mean(tf.square(y - datay))
op = tf.train.GradientDescentOptimizer(0.5)
train = op.minimize(loss)

init = tf.global_variables_initializer()

se = tf.Session()
se.run(init)

for i in range(0, 200):
    se.run(train)
    if i % 20 == 0:
        print (i, se.run(w), se.run(b))