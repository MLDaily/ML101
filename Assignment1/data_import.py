import numpy as np
import pandas as pd


def get_data():
    x = pd.read_csv('data/ex2data1.txt')
    x2 = pd.read_csv('data/ex2data2.txt')

    X = x.values[:, :-1]
    y = x.values[:, -1]
    X2 = x2.values[:, :-1]
    Y2 = x2.values[:, -1]

    m = X.shape[0]
    n = X.shape[1]

    theta = np.zeros((n + 1, 1))

    return theta, X, y, m, n
