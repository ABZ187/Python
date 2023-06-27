import matplotlib.pyplot as mp
import numpy as np
import h5py
import copy

f = h5py.File('E:\Arbaaz Shaikh\PycharmProjects\pythonProject\datasets/train_catvnoncat.h5', 'r')

def get_input(loaded_file, data_set):  # extract traning set from file
    data_set = loaded_file.get(data_set)
    data_set = np.array(data_set)
    return data_set

def initialize(layer_dims):  # initializes randon weights and biases
    parameters = {}
    L = len(layer_dims)
    for l in range(1, L):
        print(l)
        parameters["W" + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1])
        parameters["b" + str(l)] = np.zeros([layer_dims[l], 1])
    return parameters

def layer(loaded_file, data_set,l1,l2,l3):  # number of layers with nodes
    d = get_input(loaded_file, data_set).shape
    layer_dims = [d[1] * d[2] * d[3], l1, l2, l3]
    return layer_dims

def forward_prop(parameters, layer_no):  # retuns Z as dictionary
    parameters["Z" + str(layer_no)] = np.dot(parameters["W" + str(layer_no)], parameters["A" + str(layer_no - 1)]) + parameters["b" + str(layer_no)]
    return parameters

def acti_func_(activation, parameters, layer_no):
    Z = parameters["Z" + str(layer_no)]
    if activation == "relu":
        Z[Z < 0] = 0
    elif activation == "sigmoid":
        Z = 1/(1+np.exp(-Z))
    parameters["A" + str(layer_no)] = Z
    return parameters


def flatten_input(raw_X):  # Flattens input parameters
    d = raw_X.shape
    X = raw_X.reshape(d[0], d[1] * d[2] * d[3]).T
    return X

def compute_cost(cost,parameters, train_set_y, L):
    train_set_y=np.array(train_set_y)
    m = train_set_y.shape
    m=train_set_y.shape[0]
    c = -(np.dot(train_set_y, np.log(parameters["A" + str(L)]).T) - np.dot((1 - train_set_y),np.log(1 - parameters["A" + str(L)]).T)) / m
    cost.append(c)
    return cost

f = h5py.File('E:\Arbaaz Shaikh\PycharmProjects\pythonProject\datasets/train_catvnoncat.h5', 'r')
raw_X = get_input(f, 'train_set_x')
Y = get_input(f, 'train_set_y')
X = flatten_input(raw_X)
train_set_y = Y[:170]
test_set_y = Y[170:]
train_set_x = X[:, :170]
test_set_x = X[:, 170:]
layer_dims = layer(f, 'train_set_x',4,3,1)
L = len(layer_dims) - 1
parameters = initialize(layer_dims)
print("para",parameters.keys())
parameters["A0"] = train_set_x
for l in range(1, L):
    parameters = forward_prop(parameters, l)
    parameters = acti_func_("relu", parameters, l)
parameters = forward_prop(parameters, L)
parameters = acti_func_("sigmoid", parameters, L)
compute_cost(cost,parameters, train_set_y, L)
print(parameters.keys())
