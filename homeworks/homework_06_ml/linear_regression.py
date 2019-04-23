#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat):
    error = np.sum((y_true, y_hat) ** 2) / len(y_true)
    return error


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambd = lambda_coef
        self.alpha = alpha
        self.fitted = False
        self.weights
        assert regulatization in ("L1", "L2", None)
        self.regularizarion = regulatization

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        iterations = 2019
        accur_step = 0.001
        self.fitted = True
        N, M = X_train.shape
        first_step = np.inf
        self.weights = np.random.randn(M) / np.sqrt(M)
        for i in range(iterations):
            if self.regularizarion == 'L1':
                W = self.alpha * np.ones(M) / 2
                W[0] = 0
            if self.regularizarion == 'L2':
                W = self.alpha * self.weights
                W[0] = 0
            if self.regularizarion is None:
                W = 0
            prediction = self.predict(X_train)
            self.weights -= (2 / N) * self.lambd * (X_train.T.dot((prediction - y_train)) + W)
            check = mse(y_train, prediction)
            if np.abs(first_step - check) < accur_step:
                break
            return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.fitted is True:
            if all(X_test[:, 0] == 1):
                return X_test.dot(self.weights)
            else:
                ones = np.ones((X_test.shape[0], 1))
                X_test = np.hstack([ones, X_test])
                return X_test.dot(self.weights)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if self.fitted is True:
            return self.weights
