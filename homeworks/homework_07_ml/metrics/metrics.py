#!/usr/bin/env python
# coding: utf-8

import numpy as np


def logloss(y_true, y_pred, eps=1e-15):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    p = np.clip(y_pred, eps, 1 - eps)
    if y_true == 1:
        return -np.log(p)
    else:
        return -np.log(1 - p)


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    loss = np.sum(np.array(y_true) == np.array(y_pred))/len(y_true)
    return loss


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    true_y = np.array(y_true)
    pred_y = np.array(y_pred)
    if np.sum(pred_y) == 0:
        return 0.0
    else:
        loss = np.sum(true_y[pred_y == 1]) / np.sum(pred_y)
        return loss


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    true_y = np.array(y_true)
    pred_y = np.array(y_pred)
    if np.sum(true_y) == 0:
        return 0.0
    else:
        loss = np.sum(pred_y[true_y == 1]) / np.sum(true_y)
        return loss


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    tpr = recall(y_true, y_pred)
    Leng = len([i for i, j in zip(y_pred, y_true) if i[0] == 1 and j[0] == 0])
    count = len([i for i, x in enumerate(y_true) if x == 0])
    fpr = Leng / count
    loss = (1 + tpr - fpr) / 2
    return loss
