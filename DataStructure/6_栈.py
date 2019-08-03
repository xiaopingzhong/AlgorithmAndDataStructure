#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-03 19:52
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 6_栈.py
@Description: ==================================

@license: (C) Copyright 2013-2019.
************************************************
"""
import pytest

from DataStructure.DefineException import EmptyException


class Node():
    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class CycleDoubleLinkedList():
    """
    属性: root,maxsize,length
    操作: head_node,tail_node,append,len,appendleft,remove,popleft,iter_node,iter_node_reverse
    """

    def __init__(self, maxsize=10, length=0):
        # 在__init__可以定义在同一行定义多个变量
        self.maxsize = maxsize
        node = Node()
        # 因为node.previous,node.next都是节点,因此可以的话,
        # 也可以先指定类型,虽然后面可以添加上去
        node.previous, node.next = node, node
        self.root = node
        self.lenght = length

    def head_node(self):
        """
        获取头结点--只是单纯获取头结点,但是并没有进行判断---为了后面删除节点做准备
        :return:
        """
        return self.root.next

    def tail_node(self):
        """
        获取尾节点
        :return:
        """
        return self.root.previous

    def append(self, value):
        """
        添加节点:判断能不能添加,添加的方式有多种
        :param value:
        :return:
        """
        # 应该是容量小于等于长度的时候,就说明链表已经满了
        if self.maxsize is not None and self.maxsize <= self.lenght:
            raise Exception("has Fulled")
        value_node = Node(value)

        # 把两种情况考虑进去了
        tail_node = self.tail_node() or self.root

        # 先建立新节点的连接
        value_node.previous = tail_node
        value_node.next = self.root

        # 后改变对应原有节点的连接
        tail_node.next = value_node
        self.root.previous = value_node

        # 长度进行相应改变
        self.lenght += 1

    def appendLeft(self, value):
        """
        :param value:
        :return:
        """
        # 容量和长度的大小比较符号注意
        if self.maxsize is not None and self.maxsize <= self.lenght:
            raise Exception("has Fulled")
        value_node = Node(value)

        head_node = self.head_node()

        if self.lenght != 0:
            # 先设置 新节点的连接
            value_node.next = head_node
            value_node.previous = self.root

            # 在设置之后节点的连接.
            self.root.next = value_node
            head_node.previous = value_node
        else:
            value_node.next = self.root.previous
            value_node.previous = self.root.next

            self.root.next = value_node
            self.root.previous = value_node

        self.lenght += 1

    def remove(self, value_node: Node):
        if self.lenght == 0:
            # raise Exception("is empty")
            return
        # 后一个节点连接前一个节点(value_node.next.previous-->value_node.previous)
        value_node.next.previous = value_node.previous
        # 前一个节点连接后一个节点---注意箭头指向(前指向后,value_node.previous.next-->value_node.next)
        value_node.previous.next = value_node.next
        # 记住还要记得返回删除节点
        self.lenght -= 1
        return value_node

    def iter_node(self):
        """
        迭代生成返回单个节点
        :return:
        """
        # 从头结点开始
        current_node = self.root.next
        if self.lenght == 0:
            return

        # while current_node.next is not None:--否则会陷入无线循环,
        # root在添加节点之后,其不为None,因为previous和next都确定了
        # 因为是循环双向链表
        # 这是一个比较普遍的写法,记住
        while current_node.next is not self.root:
            yield current_node
            current_node = current_node.next

        # 如果只有一个头结点,那么直接返回头结点
        yield current_node

    def __iter__(self):
        """
        迭代生成返回单个节点
        :return:
        """
        for node in self.iter_node():
            yield node.value

    def __len__(self):
        return self.lenght

    def iter_node_reverse(self):
        """
        反序遍历
        :return:
        """
        if self.lenght == 0:
            return
        # 从尾节点开始--一般是self.root.previous所指向的节点--这个和正向遍历很相像
        current_node = self.root.previous

        # 从尾到根节点
        while current_node.previous is not self.root:
            # 每次生成单个node
            yield current_node
            current_node = current_node.previous
        # 如果只有一个节点(头节点),那么就直接返回,否则进行遍历
        yield current_node

        # *********+++++++++++*********========*********+++++++++++*********========
        #   开始部分:基于循环双向列表,构建双端队列,之后基于双端队列构建堆栈
        # *********+++++++++++*********========*********+++++++++++*********========


class DoubleQueue(CycleDoubleLinkedList):
    def pop(self):
        if len(self) == 0:
            raise EmptyException("the double queue is empty")
        tail_node = self.tail_node()
        tail_value = tail_node.value
        self.remove(tail_node)
        return tail_value

    def popleft(self):
        """返回左边删除的值"""
        if len(self) == 0:
            raise EmptyException("the double queue is empty")
        head_node = self.head_node()
        remove_node = self.remove(head_node)
        return remove_node.value


class Stack():
    def __init__(self):
        self._double_queue = DoubleQueue()

    def push(self, value):
        self._double_queue.append(value)

    def pop(self):
        return self._double_queue.pop()

    def __len__(self):
        return len(self._double_queue)


def test_Stack():
    stack = Stack()
    size = 5
    for x in range(size):
        stack.push(x)
    assert len(stack) == 5, "长度相等"

    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == 0

    with pytest.raises(EmptyException) as exce_info:
        stack.pop()
    assert "the double queue is empty" == exce_info.value.emptyExceptiontoString


if __name__ == '__main__':
    test_Stack()
