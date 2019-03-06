#!/usr/bin/env python
# coding: utf-8


def List_dict(val, res, key):
    if isinstance(val, (list, set, tuple)):
        for element in val:
            List_dict(element, res, key)
    else:
        if res.get(val) is None:
            res[val] = key
        elif isinstance(res.get(val), (list, set, tuple)):
            res.get(val).append(key)
        else:
            res[val] = [res.get(val), key]


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    res = {}
    try:
        for key in source_dict.keys():
            List_dict(source_dict.get(key), res, key)
        return res
    except AttributeError:
        return res
    raise NotImplementedError
