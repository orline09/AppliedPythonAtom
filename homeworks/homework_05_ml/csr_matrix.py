#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:
    """
    CSR (2D) matrix.
    Here you can read how CSR sparse matrix works: https://en.wikipedia.org/wiki/Sparse_matrix
    """
    def __init__(self, init_matrix):
        """
        :param init_matrix: can be usual dense matrix
        or
        (row_ind, col, data) tuple with np.arrays,
            where data, row_ind and col_ind satisfy the relationship:
            a[row_ind[k], col_ind[k]] = data[k]
        """
        self.shape = init_matrix.shape
        self.A = np.array([])
        self.IA = np.array([0])
        self.JA = np.array([])
        if isinstance(init_matrix, tuple) and len(init_matrix) == 3:
            self.A = np.append(self.A, init_matrix[2])
            self.JA = np.append(self.JA, init_matrix[1])
            self.IA = np.zeros(init_matrix[0][-1] + 2)
            for i in init_matrix[0]:
                self.IA[i + 1:] += 1
        elif isinstance(init_matrix, np.ndarray):
            self.A = np.append(self.A, init_matrix[np.nonzero(init_matrix)])
            for i in np.arange(init_matrix.shape[0]):
                self.JA = np.append(self.JA, np.nonzero(init_matrix[i, :]))
            sum = 0
            for i in np.arange(init_matrix.shape[0]):
                sum += init_matrix[i, :][np.nonzero(init_matrix[i, :])].shape[0]
                self.IA = np.append(self.IA, sum)
        else:
            raise ValueError

    def get_item(self, i, j):
        for k in np.arange(self.IA[i], self.IA[i + 1]):
            if self.JA[int(k)] == j:
                return self.A[int(k)]
        return 0

    def set_item(self, i, j, value):
        found = False
        for k in np.arange(self.IA[i], self.IA[i + 1]):
            if self.JA[k] == j:
                self.A[k] = value
                found = True
                break
        if not found:
            if self.IA[i + 1] - self.IA[i] == 0:
                self.A = np.insert(self.A, self.IA[i + 1], value)
                self.JA = np.insert(self.JA, self.IA[i + 1], j)
                self.IA[i + 1:] += 1
            for k in np.arange(self.IA[i], self.IA[i + 1]):
                if (j < self.JA[k]) | (k == np.arange(self.IA[i], self.IA[i + 1])[-1]):
                    self.A = np.insert(self.A, k + 1, value)
                    self.JA = np.insert(self.JA, k + 1, j)
                    self.IA[i + 1:] += 1
                    break

    def to_dense(self):
        max_row_len = int(self.IA.shape[0] - 1)
        max_col_len = int(np.amax(self.JA) + 1)
        result = np.zeros([max_row_len, max_col_len])
        for i in np.arange(max_row_len):
            for j in np.arange(self.IA[int(i)], self.IA[int(i) + 1]):
                result[int(i), int(self.JA[int(j)])] = self.A[int(j)]
        return result
