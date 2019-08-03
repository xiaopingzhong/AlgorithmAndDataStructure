#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-20 09:55
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 6_栈.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""

from collections import deque
import pytest


class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        if self.root.next is self.root:  # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


        # *********+++++++++++*********========*********+++++++++++*********========
        #   本章栈的实现
        # *********+++++++++++*********========*********+++++++++++*********========


class Deque(CircularDoubleLinkedList):
    """栈的出队"""
    def pop(self):
        """尾节点删除"""
        if len(self) == 0:
            raise Exception('empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        """头结点出队"""
        if len(self) == 0:
            raise Exception('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


def test_deque():
    dq = Deque()
    dq.append(1)

    dq.append(2)
    assert list(dq) == [1, 2]

    dq.appendleft(0)
    assert list(dq) == [0, 1, 2]

    dq.pop()
    assert list(dq) == [0, 1]

    dq.popleft()
    assert list(dq) == [1]

    dq.pop()
    assert len(dq) == 0


class Stack(object):
    """
    栈的属性和方法设置--因为栈其实是单头队列
    """
    def __init__(self):
        """使用自定义的出队方法"""
        self.deque = Deque()

    def push(self, value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()


class Stack2(object):
    """使用内置的出队方法"""
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def empty(self):
        return len(self._deque) == 0


def testStack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    with pytest.raises(Exception) as excinfo:
        s.pop()
    assert 'empty' in str(excinfo.value)


if __name__ == '__main__':
    testStack()
