#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-15 09:55
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 4_循环双向链表.py
@Description: ==================================
    循环双向链表
@license: (C) Copyright 2013-2019.    
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
#   说明:root节点在初始化的时候,value,previous,next都为None,也就是都指向自己
# *********+++++++++++*********========*********+++++++++++*********========

class Node():
    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class cycleDoubleLinkedList():
    """
    属性: root,maxsize,length
    操作: head_node,tail_node,append,len,appendleft,removeNode,popleft,iter_node,iter_node_reverse
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
            #
            value_node.next = self.root.previous
            value_node.previous = self.root.next

            self.root.next = value_node
            self.root.previous = value_node

        self.lenght += 1

    def remove(self, value_node: Node):
        if self.lenght == 0:
            # raise Exception("is empty")
            return
        # 后一个节点连接前一个节点
        value_node.next.previous = value_node.previous
        # 前一个节点连接后一个节点
        value_node.previous = value_node.next
        # 记住还要记得删除节点
        self.lenght -= 1
        return value_node



        # return value_node

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


def testCycleDoubleLinkedList():
    # 实例化循环双向链表
    maxsize = 10
    cycle_double_link_list = cycleDoubleLinkedList(maxsize=maxsize)

    # 添加元素
    cycle_double_link_list.append(0)
    cycle_double_link_list.append(1)
    cycle_double_link_list.append(2)
    # 坐标添加元素
    cycle_double_link_list.appendLeft(4)

    # 长度判断
    assert len(cycle_double_link_list) == 4

    # 元素判断
    assert list(cycle_double_link_list) == [4, 0, 1, 2]

    # 遍历判断
    assert [node.value for node in cycle_double_link_list.iter_node()] == [4, 0, 1, 2]

    # 反向遍历判断
    assert [node.value for node in cycle_double_link_list.iter_node_reverse()] == [2, 1, 0, 4]

    # 头结点
    head_node = cycle_double_link_list.head_node()
    tail_node = cycle_double_link_list.tail_node()

    assert head_node.value == 4
    assert tail_node.value == 2

    # 删除头结点
    cycle_double_link_list.remove(value_node=head_node)
    assert len(cycle_double_link_list) == 3
    # assert list(cycle_double_link_list) == [0,1,2]

    cycle_double_link_list.remove(tail_node)

    assert len(cycle_double_link_list) == 2
    # assert list(cycle_double_link_list) == [0, 1]
    # assert 0
