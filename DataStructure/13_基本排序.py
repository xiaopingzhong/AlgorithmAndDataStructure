#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-05 10:58
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 13_基本排序.py
@Description: ==================================
    冒泡排序,选择排序,插入排序
@license: (C) Copyright 2013-2019.    
************************************************
"""

# *********+++++++++++*********========*********+++++++++++*********========
#   三个排序方法的复杂度为:O(n^2)
#   冒泡排序: 每次寻找最大/小值--放到最后
#   选择排序: 每次寻找相对 大/小值--找到之后,与最前面的数据互换.
#   插入排序: 以插入的方式(插入之前进行比较)得到有序数据
#   从小到大: 索引值和值的方向是一样的;从大到小,索引值和值的方向是一样的
# *********+++++++++++*********========*********+++++++++++*********========
import random


class BaseSort(object):
    def __init__(self):
        """继承父类的排序--写的一个初始化代码"""
        super(BaseSort, self).__init__()

    def bubbleSort(self, data_quence):
        """从小到大排序,后面的的顺序会固定"""
        data_quence_length = len(data_quence)
        for x in range(data_quence_length - 1):
            # 比较的范围
            for y in range(data_quence_length - 1 - x):
                if data_quence[y] > data_quence[y + 1]:
                    """顺序排序,索引值和值方向相同"""
                    data_quence[y], data_quence[y + 1] = data_quence[y + 1], data_quence[y]
        return data_quence

    def selectSort(self, data_sequence):
        """每次找到最小的,与第一个数互换,依次比较"""
        data_sequence_length = len(data_sequence)
        # 选择的次数
        for x in range(0, data_sequence_length - 1):
            min_index = x
            # 选择的范围
            for y in range(x, data_sequence_length):
                # 选出此次最小的值,用min_index标记
                if data_sequence[min_index] > data_sequence[y]:
                    min_index = y
            # 最小值与当前位置的值互换
            if min_index != x:
                data_sequence[min_index], data_sequence[x] = data_sequence[x], data_sequence[min_index]
        return data_sequence

    def insertSort(self, data_sequence):
        data_quence_length = len(data_sequence)
        # 比较次数及其比较范围
        for i in range(1, data_quence_length):
            # pos就是为data_sequence中i位置的值,所找到合适的插入位置
            pos = i
            value = data_sequence[i]
            while pos > 0 and value < data_sequence[pos - 1]:
                data_sequence[pos], data_sequence[pos - 1] = data_sequence[pos - 1], value
                pos -= 1
            # 为i位置上的值 找到合适的位置插入(在有序数列当中)
            data_sequence[pos] = data_sequence[i]
        return data_sequence


def testBaseSorted():
    sequence_l = list(range(10))
    random.shuffle(sequence_l)
    sorted_sequence = sorted(sequence_l)
    base_sort = BaseSort()
    assert base_sort.bubbleSort(sequence_l) == sorted_sequence
    assert base_sort.selectSort(sequence_l) == sorted_sequence
    assert base_sort.insertSort(sequence_l) == sorted_sequence
