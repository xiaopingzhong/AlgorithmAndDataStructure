#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-14 10:02
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 18_优先级队列.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
from DataStructure.DefineException import FullException, EmptyException


class Array(object):
    """
    实现 数据的 索引查找,根据索引设置值,清空,遍历,长度测量
    """

    def __init__(self, size=32, initial=None):
        """设置初始容量"""
        self.size = size
        self._items = [initial] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        # 值的修改没有返回值
        self._items[index] = value

    def __iter__(self):
        for item in self._items:
            yield item

    def __len__(self):
        # 其实返回的是数组的长度--用self.size也可以
        return len(self._items)

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value


class MaxHeap(object):
    """最大堆"""

    def __init__(self, maxsize=None, count=0):
        self.maxsize = maxsize
        self._items = Array(size=maxsize)
        self._count = count

    def __len__(self):
        return self._count

    def addNode(self, value):
        if self._count >= self.maxsize:
            raise FullException("已经满了")
        self._items[self._count] = value
        self._count += 1
        # 添加之后保持需要保持堆特性
        self.keepMaxHeapWhenInsert(insert_index=self._count - 1)

    def keepMaxHeapWhenInsert(self, insert_index):
        """插入时保持堆特性"""
        # 插入节点勿过界--因为之前有不断相减self._count - 1
        if insert_index > 0:
            parent_index = int(insert_index - 1 / 2)
            if self._items[parent_index] < self._items[insert_index]:
                self._items[parent_index], self._items[insert_index] = self._items[insert_index], self._items[
                    parent_index]
                self.keepMaxHeapWhenInsert(parent_index)

    def extractMax(self):
        """提取根节点类似pop()操作"""
        if self._count <= 0:
            raise EmptyException("堆,已经空了")
        max_value = self._items[0]
        self._count -= 1
        self._items[0] = self._items[self._count]
        self._items[self._count] = None
        self.keepMaxHeapWhenDelete(delete_index=0)
        return max_value

    def keepMaxHeapWhenDelete(self, delete_index):
        """删除时保持堆特性"""
        left_index = delete_index * 2 + 1
        right_index = delete_index * 2 + 2
        large_index = delete_index
        # 注意:左,右孩子的索引小于堆的实际长度(小于等于最后一个节点的索引)
        if left_index < self._count and right_index < self._count:
            if self._items[large_index] <= self._items[left_index] \
                    and self._items[right_index] <= self._items[left_index]:
                large_index = left_index
            # 来到这步,说明根节点大于左节点
            elif self._items[large_index] <= self._items[right_index]:
                large_index = right_index

        # 比较之后,需要考虑多个节点的个数情况,单个节点不变
        if large_index != delete_index:
            self._items[delete_index], self._items[large_index] = self._items[large_index], self._items[delete_index]
            self.keepMaxHeapWhenDelete(large_index)

    def sortWithMaxHeap(self, data_sequence):
        """利用堆特性进行从大到小排序"""
        for data in data_sequence:
            self.addNode(data)
        # 利用堆的实际长度代替,再次for循环
        while self._count > 0:
            yield self.extractMax()


class PriorityQueue(MaxHeap):
    """优先级队列继承最大堆"""
    def __init__(self, maxsize=None):
        """继承(同时可以扩展)最大堆的初始化方法"""
        super(PriorityQueue, self).__init__(maxsize)

    # *********+++++++++++*********========*********+++++++++++*********========
    #   等同于:class PriorityQueue(object):
    #     """优先级队列,使用最大堆来实现"""
    #     def __init__(self, maxsize):
    #         self.maxsize = maxsize
    #         self._maxheap = MaxHeap(maxsize)
    # *********+++++++++++*********========*********+++++++++++*********========

    def push(self, priority, value):
        """增加节点"""
        entry = (priority, value)
        self.addNode(entry)

    def pop(self, is_priority):
        """根据最大堆的推出方法和序列间堆比较方法实现"""
        entry = self.extractMax()
        if is_priority:
            return entry[1]
        else:
            return entry

    def isEmpty(self):
        """主要是为了对数据进行完全pop的标记"""
        return self._count


def testPriorityQueue():
    priority_data = [(4, 'purple'), (0, 'white'), (3, 'orange'), (1, 'black')]

    priority_queue = PriorityQueue(maxsize=30)
    for entry in priority_data:
        priority_queue.push(entry[0], entry[1])

    expect_result_l = ['purple', 'orange', 'black', 'white']
    while priority_queue.isEmpty():
        for result in expect_result_l:
            assert priority_queue.pop(is_priority=True) == result
