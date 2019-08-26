#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-06 11:00
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 14_归并排序.py
@Description: ==================================

@license: (C) Copyright 2013-2019.    
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
#   归并排序:运用递归的思想---两两合并--根据递归出口,不断分解-->O(nlogn)
# *********+++++++++++*********========*********+++++++++++*********========

# *********+++++++++++*********========*********+++++++++++*********========
#   实现递归思想的简单方式之一:
#       if 条件(递归出口的条件):
#           递归出口,返回的数据  作为递归方法的参数
#       else部分:--逼近递归出口的条件
#           数据递归(切分至单个数据),之后实现对最简单情况的方法递归
# *********+++++++++++*********========*********+++++++++++*********========
import random


def mergeSortWithRecursion(data_sequence):
    """递归方式 实现归并"""
    data_sequence_length = len(data_sequence)
    # 1.归并排序的递归部分
    # 递归出口--使得问题规模较小
    if data_sequence_length <= 1:
        return data_sequence
    # 靠近递归口
    mid = int(data_sequence_length / 2)
    # 分解的子问题递归
    left_half_l = mergeSortWithRecursion(data_sequence[:mid])
    right_half_l = mergeSortWithRecursion(data_sequence[mid:])
    # 2.归并排序的合并部分
    new_sequence_l = mergeSortedList(left_half_l, right_half_l)
    return new_sequence_l


def mergeSortedList(left_half_l, right_half_l):
    left_half_length=len(left_half_l)
    right_half_length=len(right_half_l)
    left_index=right_index=0
    new_sorted_sequence_l=list()
    # 长度相等的部分,两两比较,指针移动
    while left_index<left_half_length and right_index<right_half_length:
        if left_half_l[left_index]<right_half_l[right_index]:
            new_sorted_sequence_l.append(left_half_l[left_index])
            left_index+=1
        else:
            new_sorted_sequence_l.append(right_half_l[right_index])
            right_index+=1

    # 两个列表 多出部分的处理
    while left_index<left_half_length:
        new_sorted_sequence_l.append(left_half_l[left_index])
        left_index += 1

    while right_index<right_half_length:
        new_sorted_sequence_l.append(right_half_l[right_index])
        right_index += 1

    return new_sorted_sequence_l

def testMergeSortWithRecursion():
    sequence_l = list([5, 9, 3, 2, 4, 6, 8, 0, 1, 7])
    random.shuffle(sequence_l)
    sorted_squence_l=sorted(sequence_l)
    assert mergeSortWithRecursion(sequence_l)==sorted_squence_l
