import tflearn
import numpy as np
model.load('cancer.model')
print(np.round(model.predict([test_x[10]])[0]))
print(test_y[10])
