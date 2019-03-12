#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.main = []
        self.input_data = array[:]
        self.build_heap()

    def add(self, elem_with_priority):
        self.main.append(elem_with_priority)
        i = len(self.main) - 1
        while i > 0:
            parent = (i - 1) // 2
            if comparator_d(self.main[i], self.main[parent]):
                leaf = self.main[i]
                self.main[i] = self.main[parent]
                self.main[parent] = leaf
                i = parent
            else:
                break

    def build_heap(self):
        i = 1
        if len(self.input_data):
            self.main.append(self.input_data[0])
            while i < len(self.input_data):
                self.add(self.input_data[i])
                i += 1


class MaxHeap(Heap):

    def __init__(self, array):
        Heap.__init__(self, array)

    def extract_maximum(self):
        res = self.main[0]
        last = len(self.main) - 1
        self.main[0] = self.main[last]
        self.main.pop()
        i = 0
        while 2*i+1 <= len(self.main) - 1:
            # one leaf
            if 2 * i + 1 == len(self.main) - 1:
                j = 2*i + 1
                if comparator_d(self.main[j], self.main[i]):
                    # swap main[i] and main [j]
                    h = self.main[i]
                    self.main[i] = self.main[j]
                    self.main[j] = h
                break
            else:
                left_i = 2*i+1
                right_i = 2*i + 2
                if comparator_d(self.main[left_i], self.main[right_i]):
                    j = left_i
                else:
                    j = right_i
                if comparator_d(self.main[j], self.main[i]):
                    # swap main[i] and main [j]
                    h = self.main[i]
                    self.main[i] = self.main[j]
                    self.main[j] = h
                i = j
        return res


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
