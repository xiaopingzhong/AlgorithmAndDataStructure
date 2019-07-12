#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-12 13:15
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 2_数组和列表.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""


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
            self._items[i]=value

def test_array():
    size = 10
    arr = Array(size=size)

    arr[0] = 1

    assert arr[0] == 1
    assert len(arr) == 10, "长度不相等"

    arr.clear()
    assert arr[0] == None, "数组清零不成功"
    assert arr[0] is None, "数组清零不成功"
#
if __name__ == '__main__':
    test_array()