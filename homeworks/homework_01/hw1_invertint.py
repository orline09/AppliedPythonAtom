#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    n2 = 0
    n1 = number
    while n1 > 0:
        digit = n1 % 10 
        n1 = n1 // 10 #fgdk.j
        n2 = n2 * 10 
        n2 = n2 + digit 
    return n2
    raise NotImplementedError
