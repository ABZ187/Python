import numpy as np
import h5py
import matplotlib.pyplot as mp
import pickle


def get_input(loaded_file, data_set):  # extract training set from file
    data_set = loaded_file.get(data_set)
    data_set = np.array(data_set)
    return data_set


def flatten_input(raw_X):  # Flattens input parameters
    d = raw_X.shape
    X = raw_X.reshape(d[0], d[1] * d[2] * d[3]).T
    return X


def layer(loaded_file, data_set, l1, l2, l3):  # number of layers with nodes
    d = get_input(loaded_file, data_set).shape
    layer_dims = [d[1] * d[2] * d[3], l1, l2, l3]
    return layer_dims


def initialize(layer_dims):  # initializes random weights and biases
    parameters = {}
    L = len(layer_dims)
    for l in range(1, L):
        parameters["W" + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) * 0.01
        parameters["b" + str(l)] = np.zeros([layer_dims[l], 1])
    return parameters


def forward_prop(parameters, layer_no):  # returns Z as dictionary
    parameters["Z" + str(layer_no)] = np.dot(parameters["W" + str(layer_no)], parameters["A" + str(layer_no - 1)]) + \
                                      parameters["b" + str(layer_no)]
    return parameters


def acti_func_(activation, parameters, layer_no):
    Z = parameters["Z" + str(layer_no)]
    if activation == "relu":
        Z[Z < 0] = 0
    elif activation == "sigmoid":
        Z = np.around(Z, 5)
        # print("Z",Z)
        Z = 1 / (1 + np.exp(-Z, dtype=np.float64))
    parameters["A" + str(layer_no)] = Z
    return parameters


def acti_backprop(Z_list):  # relu inverse
    Z_list = list(Z_list)
    Z_list = np.array(Z_list)
    Z_list[Z_list < 0] = 0
    Z_list[Z_list > 0] = 1
    Z_list[Z_list == 0] = 1
    return Z_list


def back_prop(train_set_y, parameters, L):
    grads = {"dZ" + str(L): parameters["A" + str(L)] - train_set_y}
    m = parameters["Z" + str(L)].shape[1]
    for l in reversed(range(1, L)):
        grads["dZ" + str(l)] = np.dot(parameters["W" + str(l + 1)].T, grads["dZ" + str(l + 1)]) * acti_backprop(
            parameters["Z" + str(l)])
        grads["dW" + str(l)] = np.dot(grads["dZ" + str(l)], parameters["A" + str(l - 1)].T)
        grads["db" + str(l)] = np.sum(grads["dZ" + str(l)], axis=1, keepdims=True) / m
    return grads


def update_parameters(parameters, grads, L, alpha):
    for l in range(1, L):
        parameters["W" + str(l)] = parameters["W" + str(l)] - alpha * grads["dW" + str(l)]
        parameters["b" + str(l)] = parameters["b" + str(l)] - alpha * grads["db" + str(l)]
    return parameters


def compute_cost(cost, parameters, train_set_y, L):
    train_set_y = np.array(train_set_y)
    m = train_set_y.shape[0]
    # print('"A" + str(L)',parameters["A" + str(L)])
    c = -(np.dot(train_set_y, np.log(parameters["A" + str(L)]).T) + np.dot((1 - train_set_y),
                                                                           np.log(1 - parameters["A" + str(L)]).T)) / m
    cost.append(c)
    return cost


def model(address):
    f = h5py.File(address, 'r')
    raw_X = get_input(f, 'train_set_x')
    train_set_y = get_input(f, 'train_set_y')
    train_set_x = flatten_input(raw_X)
    # train_set_y = Y[:170]
    # test_set_y = Y[170:]
    # train_set_x = X[:, :170]
    # test_set_x = X[:, 170:]
    layer_dims = layer(f, 'train_set_x', 4, 3, 1)
    L = len(layer_dims) - 1
    parameters = initialize(layer_dims)
    parameters["A0"] = train_set_x

    for l in range(1, L):
        parameters = forward_prop(parameters, l)
        parameters = acti_func_("relu", parameters, l)
    parameters = forward_prop(parameters, L)
    parameters = acti_func_("sigmoid", parameters, L)
    # print(parameters["A"+str(L)])
    return parameters, L, train_set_y


def train_model(iterations):
    cost = []
    parameters, L, train_set_y = model('E:\Arbaaz Shaikh\PycharmProjects\pythonProject\datasets/train_catvnoncat.h5')
    for i in range(iterations):
        compute_cost(cost, parameters, train_set_y, L)
        grads = back_prop(train_set_y, parameters, L)
        parameters = update_parameters(parameters, grads, L, 50)
        # print("cost", cost)
        # mp.plot(cost)
        # mp.show()
    cost = np.squeeze(cost)
    para = {}
    for l in range(1, L+1):
        para['W' + str(l)] = parameters['W' + str(l)]
        para['b' + str(l)] = parameters['b' + str(l)]
    return para, parameters, L, cost


para, parameters, L, cost = train_model(10)

i = h5py.File("E:\Arbaaz Shaikh\PycharmProjects\pythonProject\datasets/test_catvnoncat.h5", 'r')
test_X = get_input(i, 'test_set_x')
test_set_x = flatten_input(test_X)
para['A0'] = test_set_x
print(para)
for l in range(1, L):
    forward_prop(para, l)
    para['A' + str(l)] = acti_func_("relu", para, l)
para2 = {"Z" + str(L): np.dot(para['W' + str(L)], para['A' + str(L - 1)]) + para['b' + str(L)]}
para['A' + str(L)] = acti_func_("sigmoid", para, L)
print(cost)
# g = open('trained.py', 'wb')
# for l in range(1,L):
#     # g.writelines('W' + str(l))
#     pickle.dump(para,g)
# g.close()
# g = open('trained.py', 'r')
