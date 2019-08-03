#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-18 10:02
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 5_队列实现.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
# 内置的出队包
from collections import deque
import pytest


class Node(object):
    """定义节点"""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        """便于断点调试"""
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """链接表的实现"""
    def __init__(self, maxsize=None):
        """

        :param maxsize:
        """
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        """添加值的复杂度为常数级别"""
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """遍历,从头结点开始"""
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def remove(self, value):
        """根据值进行节点删除"""
        prevnode = self.root
        curnode = self.root.next
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                del curnode
                self.length -= 1
                return 1
            else:
                prevnode = curnode
        return -1

    def find(self, value):
        """寻找值对应节点所在的下标"""
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):    # O(1)
        """删除头结点"""
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        """清空链表"""
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0



class EmptyError(Exception):
    """自定义异常"""
    pass


class Queue(object):

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_link_list = LinkedList()

    def __len__(self):
        return len(self._item_link_list)

    def push(self, value):    # O(1)
        """ 队尾添加元素 """
        return self._item_link_list.append(value)

    def pop(self):
        """队列头部删除元素"""
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_link_list.popleft()


def testQueue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2

    with pytest.raises(EmptyError) as excinfo:
        q.pop()
    assert 'empty queue' == str(excinfo.value)


class MyQueue:
    """
   调用deque实现一个队列,这个在effective python 当中有提及
    """
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]