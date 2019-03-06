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
    res = 1
    a = list_of_lists
    if len(a) != len(a[0]):
        return False
    n = len(a)
    for i in range(n):
        j = max(range(i,n), key=lambda k: abs(a[k][i]))
        if i != j:
            a[i],a[j] = a[j],a[i]
            res *= -1
        if a[i][i] == 0:
            return 0
        res *= a[i][i]
        for j in range(i+1,n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k]-b*a[i][k] for k in range(n)]
    return res                      
    raise NotImplementedError
