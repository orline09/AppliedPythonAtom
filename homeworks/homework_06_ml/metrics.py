#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    error = np.sum((y_true, y_hat) ** 2) / len(y_true)
    return error


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    error = np.sum(abs(y_true - y_hat)) / len(y_true)
    return error


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    y_mean_line = np.avarage(y_true)
    squared_error_regr = np.sum((y_true - y_hat) ** 2)
    squared_error_y_mean = np.sum((y_true - y_mean_line) ** 2)
    error = 1 - squared_error_regr / squared_error_y_mean
    return error

