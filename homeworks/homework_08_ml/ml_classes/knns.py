#!/usr/bin/env python
# coding: utf-8

import numpy as np


class KNNRegressor:
    """
    Построим регрессию с помощью KNN. Классификацию писали на паре
    """

    def __init__(self, n):
        '''
        Конструктор
        :param n: число ближайших соседей, которые используются
        '''
        self.n = n
        self.was_fit = False

    def fit(self, X, y):
        '''
        :param X: обучающая выборка, матрица размерности (num_obj, num_features)
        :param y: целевая переменная, матрица размерности (num_obj, 1)
        :return: None
        '''
        self.x = X
        self.y = y
        self.was_fit = True

    def predict(self, X):
        '''
        :param X: выборка, на которой хотим строить предсказания (num_test_obj, num_features)
        :return: вектор предсказаний, матрица размерности (num_test_obj, 1)
        '''
        y = []
        assert len(X.shape) == 2
        for t in X:
            # Посчитаем расстояние от всех элементов в тренировочной выборке
            # до текущего примера -> результат - вектор размерности трейна
            d = np.sqrt(np.sum((X-t) ** 2))
            # Возьмем индексы n элементов, расстояние до которых минимально
            # результат -> вектор из n элементов
            idx = np.argsort(d)[:self.n]
            prediction = np.average(self.y[idx])
            y.append(prediction)
        return y