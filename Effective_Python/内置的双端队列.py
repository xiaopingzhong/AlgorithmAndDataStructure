#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-22 02:03
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 内置的双端队列.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
from bisect import bisect_left
from collections import deque, defaultdict
from heapq import heappush, heappop


def dequeTest(value1,value2,value3):
    """
    双端队列
    :param value1:
    :param value2:
    :param value3:
    :return:
    """
    fifo=deque()
    fifo.append(value1)
    fifo.append(value2)
    fifo.append(value3)
    print(fifo)
    # pop默认是从尾部开始删除---fiLo
    # popleft则是从头部删除--实现fifo
    fifo.pop()
    print(fifo)

def dictTest():
    """
    带有默认值的dict
    :return:
    """
    # defaultdict的参数为可可遍历数据-list,int
    default_dict=defaultdict(list)
    # default_dict.setdefault
    # 0---在进行查询的时候,如果key没有如果指定了value的默认值,就不会出现keyError
    print(default_dict["ke"])
    # defaultdict(<class 'int'>, {'ke': 0})
    print(default_dict)

def heapTest():
    """
    堆队列--一般是最小堆
    :return:
    """
    a=[]
    heappush(a,6)
    heappush(a,4)
    heappush(a,8)
    heappush(a,3)

    # 3
    # 4
    # 6
    # 8
    print(heappop(a))
    print(heappop(a))
    print(heappop(a))
    print(heappop(a))

def binarySearchTest():
    test_l=list(range(10**6))
    # 线性级别
    i_index=test_l.index(991234)
    print(i_index)

    # 二分查找,对数级别
    index=bisect_left(test_l,991234)
    print(index)



if __name__ == '__main__':
    dequeTest(1,3,4)
    dictTest()
    heapTest()
    binarySearchTest()


