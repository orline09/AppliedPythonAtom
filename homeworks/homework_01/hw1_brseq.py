#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(len(input_string)):
        if input_string[i] == '(':
            s1 += 1
        elif input_string[i] == '[':
            s2 += 1
        elif input_string[i] == '{':
            s3 += 1
        if input_string[i] == ')':
            s1 -= 1
        elif input_string[i] == ']':
            s2 -= 1
        elif input_string[i] == '}':
            s3 -= 1
        if s1 < 0 or s2 < 0 or s3 < 0:
            return False
    if s1 == s2 == s3:
        return True
    else:
        return False
    raise NotImplementedError