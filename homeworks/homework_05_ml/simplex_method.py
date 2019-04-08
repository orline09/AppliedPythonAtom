#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    matrix = np.array([])
    x = np.concatenate((a, [c * (-1)]), axis=0)
    x = np.concatenate((x, np.eye(b.shape[0] + 1)), axis=1)
    x = np.concatenate((x, np.append(b, [0], axis=0).reshape(x.shape[0], 1)), axis=1)

    while x[-1, x[-1, :] < 0].shape[0] != 0:
        pivot_column = np.argmin(x, axis=1)[-1]
        row = np.argmin(x[:, -1][:-1] / x[:, pivot_column][:-1])
        x[row, :] = x[row, :] / x[row, pivot_column]
        for i in np.arange(x.shape[0]):
            if i == row:
                continue
            x[i, :] = x[i, :] - x[row, :] * x[i, pivot_column]
    for j in np.arange(a.shape[1]):
        if (np.linalg.norm(x[:, j]) == 1) & (len(np.nonzero(x[:, j])[0]) == 1):
            matrix = np.append(matrix, x[np.nonzero(x[:, j])[0], -1])
        else:
            matrix = np.append(matrix, [0])
    return matrix
