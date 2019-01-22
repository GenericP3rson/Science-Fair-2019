import numpy as np
import random
sizes = (2, 2, 2)
num_layers = len(sizes)
biases = [np.random.randn(y,1) for y in sizes[1:]] 
weights = [np.random.randn(x, y) for x, y in zip(sizes[1:], sizes[:-1])]
# The [1:] is obviously just taking a part of what we need.
# print(biases)
# print(np.random.randn(10, 1))
# Okay, so this makes a 10 arrays with 1 element!
print(weights)


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))


def cost_derivative(output_activations, y):
        """Return the vector of partial derivatives ` partial C_x `
        `partial a for the output activations."""
        return 2*(output_activations-y)

def backprop(x, y):
    """Return a tuple ``(nabla_b, nabla_w)`` representing the
    gradient for the cost function C_x.  ``nabla_b`` and
    ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
    to ``self.biases`` and ``self.weights``."""
    nabla_b = [np.zeros(b.shape) for b in biases]
    nabla_w = [np.zeros(w.shape) for w in weights]
    # feedforward
    activation = x # this is a holder variable
    activations = [np.array(x)]  # This has everything after the sigmoid function
    # One is a list and the other is not...
    zs = []  # This pretty much stores everything before the sigmoid
    print(activation, activations)
    for b, w in zip(biases, weights):
        z = np.dot(w, activation)+b # it does the same feed-forward
        zs.append(z) # It takes the value BEFORE the sigmoid
        activation = sigmoid(z) # It adds the sigmoid
        activations.append(activation) # Activation
        print("Z Index")
        print(zs)
        print("Activation")
        print(activations)
        # This is SO NICE! It basically has everything we need
    # # backward pas
    delta = cost_derivative(activations[-1], y) * \
        sigmoid_prime(zs[-1]) # It takes the derivatives
    print(delta)
    nabla_b[-1] = delta
    print(nabla_b) # Append it to the end
    nabla_w[-1] = np.dot(delta, activations[-2].transpose())
    print(nabla_w[-1]) # LOOK INTO THESE LATER
    # Note that the variable l in the loop below is used a little
    # differently to the notation in Chapter 2 of the book.  Here,
    # l = 1 means the last layer of neurons, l = 2 is the
    # second-last layer, and so on.  It's a renumbering of the
    # scheme in the book, used here to take advantage of the fact
    # that Python can use negative indices in lists.
    for l in range(2, num_layers): # STOPPED HERE
        z = zs[-l] # So we start by looking at the second to last.
        sp = sigmoid_prime(z) # Derivative
        delta = np.dot(weights[-l+1].transpose(), delta) * sp
        nabla_b[-l] = delta
        nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
    return (nabla_b, nabla_w)
    # return (0, 0)




# np.dot()
training_data = [[[0, 1], [0, 1]], [[0, 2], [1, 0]], [[0, 3], [1, 1]]]
print(random.shuffle(training_data)) # So this will just mix it all up
print(training_data)

mini_batch_size = 2
n = len(training_data)


mini_batches = [
    training_data[k:k+mini_batch_size]
    for k in range(0, n, mini_batch_size)]
print(mini_batches)
# This just pretty much groups the data we need


nabla_b = [np.zeros(b.shape) for b in biases]
nabla_w = [np.zeros(w.shape) for w in weights]
print(nabla_w)
mini_batch = mini_batches[0]
delta_nabla_b, delta_nabla_w = backprop(mini_batch[0][0], mini_batch[0][1])
# for x, y in mini_batch:
#     delta_nabla_b, delta_nabla_w = self.backprop(x, y)
#     nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
#     nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
# self.weights = [w-(eta/len(mini_batch))*nw
#                 for w, nw in zip(self.weights, nabla_w)]
# self.biases = [b-(eta/len(mini_batch))*nb
#                 for b, nb in zip(self.biases, nabla_b)]


# import numpy as np
# import random
# sizes = (2, 2, 2)
# num_layers = len(sizes)
# biases = [np.random.randn(y, 1) for y in sizes[1:]]
# weights = [np.random.randn(x, y) for x, y in zip(sizes[1:], sizes[:-1])]
# print(weights[0])
# print(weights[0].transpose())
# # OH. So we can transpose numpy arrays but we can't transpose lists.
