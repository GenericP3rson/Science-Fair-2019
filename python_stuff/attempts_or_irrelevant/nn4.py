import numpy as np 

def sigmoid(x, d = False):
    if (d == True):
        return (x*(1-x))
    return 1/(1+np.exp(-x))

x = np.array([[0,0,1], 
[0,1,1],
[1,0,1],
[1,1,1]])
y = np.array([[0], 
[1], 
[1], 
[0]]) 
# A Matrix

# Seed, which is apparently good for debugging

np.random.seed(1) # Starts at one!

# Create the weights!

# Synapses

syn0 = 2*np.random.random((3, 4)) - 1
# A 3 by 4 matrix of weights. One is the bias
syn1 = 2*np.random.random((4, 1)) - 1
# A 4 by 1 matrix
print (syn0, syn1)

# Train???

for j in range(60000):
    # Layers
    l0 = x # Input Layer
    l1 = sigmoid(np.dot(l0, syn0))
    l2 = sigmoid(np.dot(l1, syn1))
    # Makes the layers

    # Now Backpropogation
    l2_error = y - l2 # Oh, vector subtraction, how I love thee!
    if (j % 10000 == 0):
        # print(error)
        print("Error: " + str(np.mean(np.abs(l2_error))))
        # print(syn1)
        # print(w0)
    l2_change = l2_error*sigmoid(l2, d=True)
    l1_error = l2_change.dot(syn1.T)
    l1_change = l1_error * sigmoid(l1, d=True)
    syn1 += l1.T.dot(l2_change)
    syn0 += l0.T.dot(l1_change)
print(l2)
# q = np.random.random((3, 4))
# print(q) # This returns a constant random value
# print(q.T) # It flips the dimnesions and adjusts.
