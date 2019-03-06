#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    if operator == "plus":
        try:
            return x + y
        except TypeError:
            return None
    if operator == "minus":
        try:
            return x - y
        except TypeError:
            return None
    if operator == "mult":
        try:
            return x * y
        except TypeError:
            return None
    if operator == "divide":
        if y != 0:
            try:
                return x / y
            except TypeError:
                return None
        else:
            return None
    return None
    raise NotImplementedError
