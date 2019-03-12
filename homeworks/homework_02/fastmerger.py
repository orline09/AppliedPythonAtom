#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        res = []
        i = 0
        additional = []
        for i in range(len(list_of_lists)):
            if list_of_lists[i]:
                additional.append((list_of_lists[i][-1], i))
        heap = MaxHeap(additional)
        for i in range(k):
            n = heap.extract_maximum()
            res.append(n[0])
            list_of_lists[n[1]].pop()
            if list_of_lists[n[1]]:
                heap.add((list_of_lists[n[1]][-1], n[1]))
        return res
