#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    a = list_of_lists
    if a is None:
        return None
    if len(a) == 1 and len(a[0]) == 1:
        return a[0][0]
    if len(a) != len(a[0]):
        return None
    if len(a) == 2:
        sum = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        return sum
    sum = 0
    for i in range(len(a)):
        mul = 1
        k = i
        for j in range(len(a)):
            mul *= a[j][k]
            if (k == len(a) - 1):
                k = 0
            else:
                k = k + 1
        sum += mul
    for i in range(len(a)):
        mul = 1
        k = i
        for j in range(len(a)):
            mul *= a[j][k]
            if k == 0:
                k = len(a) - 1
            else:
                k = k - 1
        sum -= mul
    return sum
    raise NotImplementedError
