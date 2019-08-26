#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-04 10:25
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 12_线性查找与二分查找.py
@Description: ==================================
    线性查找与二分查找
@license: (C) Copyright 2013-2019.    
************************************************
"""

class TraditionalSearch():
    """传统查找方法总结"""
    def linearSearchTraditional(self, destination_value, sequence):
        """传统线行查找"""
        for index, value in enumerate(sequence):
            print(index, value)
            if destination_value == value:
                return index

    def linearSearchRecursion(self, destination_value, sequence):
        """递归式线性查找"""
        sequence_length = len(sequence)
        if not sequence_length:
            # -1代表不存在,失败
            return -1
        # 设置逼近递归出口条件
        index = sequence_length - 1
        # 设置递归出口
        if sequence[index] == destination_value:
            return index
        # 分解子问题--递归函数
        return self.linearSearchRecursion(destination_value, sequence[0:index])

    def binarySearchRecursion(self, value, sorted_sequence):
        """递归式二分查找"""
        sequence_length = len(sorted_sequence)
        # 注意长度的判断
        if not sequence_length:
            return -1
        mid = int(sequence_length / 2)
        if sorted_sequence[mid] == value:
            return mid
        elif sorted_sequence[mid] < value:
            # 分解子问题--递归函数
            return self.binarySearchRecursion(sorted_sequence=sorted_sequence[mid + 1, sequence_length], value=value)
        else:
            return self.binarySearchRecursion(sorted_sequence=sorted_sequence[0:mid], value=value)


def testTraditionalSearch():
    sequence_l = [0, 1, 2, 3, 4, 5, 6, 7]
    traditional_search = TraditionalSearch()
    assert traditional_search.linearSearchTraditional(4, sequence_l) == 4
    assert traditional_search.linearSearchRecursion(5, sequence_l) == 5
    assert traditional_search.binarySearchRecursion(4, sequence_l) == 4
