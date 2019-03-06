#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    n2 = 0
    n1 = number
    k = 0
    if number < 0:
        k = 1
        n1 = abs(n1)
    while n1 > 0:
        digit = n1 % 10 
        n1 = n1 // 10 
        n2 = n2 * 10 
        n2 = n2 + digit 
    if k == 1:
        return -n2
    else:
        return n2
    raise NotImplementedError
