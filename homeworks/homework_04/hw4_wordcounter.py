#!/usr/bin/env python
# coding: utf-8

from multiprocessing.dummy import Pool
from functools import partial
import os


def word_count_inference(path_to_dir):
    """
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    """
    files = os.listdir(path_to_dir)
    new_dict, new_dict['total'] = {}, 0
    func = partial(count_dict, path_to_dir, new_dict)
    pool = Pool(os.cpu_count())
    pool.map(func, files)
    return new_dict


def reading_file(path_to_dir, filename):
    with open(path_to_dir + '/' + filename, "r") as file:
        return len(file.read().split())


def count_dict(path_to_dir, dict_one, filename):
    k = reading_file(path_to_dir, filename)
    dict_one[filename] = k
    dict_one['total'] += k
    return
