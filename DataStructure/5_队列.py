#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-16 09:32
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 5_队列.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""

class Array(object):
    """
    因为对队列是有列表来进行承载的.引用之前定义的数组及其列表
    """
    def __init__(self, size=32):
        """
        设置无限长的数组
        :param size:
        """
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        """
        定义获取方法
        :param index:
        :return:
        """
        return self._items[index]

    def __setitem__(self, index, value):
        """
        设置值
        :param index:
        :param value:
        :return:
        """
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        """
        清空None
        :param value:
        :return:
        """
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        """
        迭代方法
        :return:
        """
        for item in self._items:
            yield item


class FullError(Exception):
    """
    已经满了的错误
    """
    pass


class ArrayQueue(object):

    def __init__(self, maxsize):
        """
        设置容量,基本承载结构--数组
        设置头尾
        :param maxsize:
        """
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        """
        入队
        :param value:
        :return:
        """
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        # 余数入队
        # 核心代码
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        """
        出队
        :return:
        """
        # 头部,余数出队
        # 核心代码
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


def testQueue():
    import pytest    # pip install pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(FullError) as excinfo:   # 我们来测试是否真的抛出了异常
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == 5

    assert q.pop() == 0
    assert q.pop() == 1

    q.push(5)

    assert len(q) == 4

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0