#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import mean_squared_error
import numpy as np


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self.th = 0
        self.right = 0
        self.left = 0

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        pred = np.zeros(y.shape)
        # max error
        first_error = mean_squared_error(y, pred)
        for i in range(len(X) - 1):
            th_step = (X[i] + X[i+1]) / 2
            left_step, right_step = X[X <= self.th], X[X > self.th]
            pred[i+1:] = right_step
            pred[:i+1] = left_step
            check_error = mean_squared_error(y, pred)
            if check_error < first_error:
                self.th = th_step
                self.left = left_step
                self.right = right_step
                first_error = check_error

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        pred = np.zeros(X.shape)
        for number in X:
            if number > self.th:
                pred[number] = self.right
            else:
                pred[number] = self.left
        return pred
