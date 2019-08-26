#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-07 11:01
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 15_快速排序.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
import random


class QuickSort(object):
    def __init__(self):
        """调用父类的object"""
        super(QuickSort, self).__init__()

    def quickSortedTraditional(self, data_sequence: list) -> list:
        data_sequence_length = len(data_sequence)
        if data_sequence_length < 2 and not data_sequence:
            return data_sequence
        pivot = 0
        pivot_value = data_sequence[pivot]
        morepart_l = [data_sequence[x] for x in range(data_sequence_length) if
                      data_sequence[x] >= pivot_value and pivot != x]
        lesspart_l = [data_sequence[x] for x in range(data_sequence_length) if
                      data_sequence[x] < pivot_value and pivot != x]
        sorted_sequence_l = self.quickSortedTraditional(lesspart_l) + [pivot_value] + self.quickSortedTraditional(
            morepart_l)
        return sorted_sequence_l

    def quickSortInplace(self, data_sequence, beg, end):
        if beg < end:
            pivot_i = self.findPivot(data_sequence, beg, end)
            self.quickSortInplace(data_sequence, beg, pivot_i)
            self.quickSortInplace(data_sequence, pivot_i + 1, end)

    def findPivot(self, data_sequence, beg, end):
        # 主元为第一个
        pivot_index = beg
        left_index = pivot_index + 1
        right_index = end - 1
        pivot_value = data_sequence[pivot_index]
        while True:
            # 特别注意:left_index <= right_index 放前头;
            # 多个条件表达式,最好大小方向一样,便于观察
            while left_index <= right_index and pivot_value > data_sequence[left_index]:
                left_index += 1
            while left_index <= right_index and pivot_value <= data_sequence[right_index]:
                right_index -= 1
            # 遍历完成
            if left_index > right_index:
                break
            # 两边不符合条件--data_sequence[pivot_index] > data_sequence[right_index] and data_sequence[pivot_index] < data_sequence[left_index]:
            else:
                # 两边不符合条件,需要换位置
                data_sequence[left_index], data_sequence[right_index] \
                    = data_sequence[right_index], data_sequence[left_index]
        data_sequence[pivot_index], data_sequence[right_index] \
            = data_sequence[right_index], data_sequence[pivot_index]
        return right_index


def testFindPivot():
    """测试主元"""
    quick_sort = QuickSort()
    l = [4, 3, 2, 1]
    assert quick_sort.findPivot(l, 0, len(l)) == 3
    l = [1]
    assert quick_sort.findPivot(l, 0, len(l)) == 0
    l = [2, 1]
    assert quick_sort.findPivot(l, 0, len(l)) == 1


def testQuickSort():
    quick_sort = QuickSort()
    sequence_l = list(range(10))
    random.shuffle(sequence_l)
    sorted_sequence = sorted(sequence_l)
    assert quick_sort.quickSortedTraditional(sequence_l) == sorted_sequence

    quick_sort.quickSortInplace(sequence_l, 0, len(sequence_l))
    assert sequence_l == sorted_sequence
