#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-03 18:24
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 5_2数组形式的队列.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
import pytest

from DataStructure.DefineException import FullException, EmptyException


# *********+++++++++++*********========*********+++++++++++*********========
#   数组的首尾部分分别作为 出队和入队的接口.
# *********+++++++++++*********========*********+++++++++++*********========

class Array(object):
    """
    实现 数据的 索引查找,根据索引设置值,清空,遍历,长度测量
    """

    def __init__(self, size=32):
        self.size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        # 值的修改没有返回值
        self._items[index] = value

    def __iter__(self):
        for item in self._items:
            yield item

    def __len__(self):
        return len(self._items)

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

# *********+++++++++++*********========*********+++++++++++*********========
#   开始部分:
# *********+++++++++++*********========*********+++++++++++*********========


class QueueWithArray():
    def __init__(self, maxsize, head=0, tail=0):
        """用数组作为队列的载体"""
        self.maxsize = maxsize
        self._item_with_array = Array(maxsize)
        self.head = head
        self.tail = tail

    def __len__(self):
        """使用首尾对应索引号相减即可得到"""
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize and self.maxsize is not None:
            raise FullException("the Queue has fulled")
        # 取模得到当前的索引的位置,设置值
        self._item_with_array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        """为什么不要删除相应数据,因为我们只需要根据首尾下标获得最新状态的队列,因此删除不删除没什么影响"""
        # 需要先进行判断
        if len(self) <= 0:
            raise EmptyException("the Queue has empty")
        # 没问题则进行出队
        pop_value = self._item_with_array[self.tail % self.maxsize]
        self.tail += 1
        return pop_value


def testQueueWithArray():
    maxsize = 5
    array_queue = QueueWithArray(maxsize=maxsize)
    for x in range(maxsize):
        array_queue.push(x)

    assert len(array_queue) == 5

    # 异常测试
    with pytest.raises(FullException) as exceInfo:
        array_queue.push(maxsize)
    assert "full" in exceInfo.value.fullExceptiontoString

    # *********+++++++++++*********========*********+++++++++++*********========
    #       典型错误,
    #       for x in range(maxsize):
    #     #     assert array_queue.pop() == 0
    #     #     assert array_queue.pop() == 1
    #     #     assert array_queue.pop() == 2
    #     #     assert array_queue.pop() == 3
    #     #     assert array_queue.pop() == 4
    # *********+++++++++++*********========*********+++++++++++*********========
    for x in range(maxsize):
        assert array_queue.pop() == x

    # 检查异常是否一致
    with pytest.raises(EmptyException) as exceInfo:
        array_queue.pop()
    assert "empty" in exceInfo.value.emptyExceptiontoString
