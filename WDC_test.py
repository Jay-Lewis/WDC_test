

import numpy as np
import math
import scipy


def gen_matrix(size, x, y):
    m,n = size
    W = np.random.normal(0,1.0/n,size)

    z1 = np.matmul(W, x)
    z2 = np.matmul(W, y)

    W_x_plus, W_y_plus = relu_operation(W, z1, z2, m ,n)
    W = np.matmul(np.transpose(W_x_plus), W_y_plus)

    return W

def relu_operation(W, z1, z2, m, n):
    indices_x = [i for i, value in enumerate(z1) if value < 0]
    indices_y = [i for i, value in enumerate(z2) if value < 0]
    print(indices_x)
    print(indices_y)
    W_x = W
    W_y = W

    for index in indices_x:
        print(index)
        W_x[index,:] = np.ones(n)

    for index in indices_y:
        W_y[index,:] = np.zeros(n)

    print(W_x)
    print(W_y)

    return W_x, W_y

def get_x_y():
    x = np.asarray([1, 0])
    rand_theta = np.random.uniform()*math.pi
    y = np.asarray([math.cos(rand_theta), math.sin(rand_theta)])

    return x, y

#-------------------------
# Theta Test
#-------------------

x,y = get_x_y()
W_symm = gen_matrix([2, 2], x, y)

