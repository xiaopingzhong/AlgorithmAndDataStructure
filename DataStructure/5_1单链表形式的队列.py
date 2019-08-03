#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-03 15:22
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 5_1单链表形式的队列.py
@Description: ==================================
    简单队列的实现(FIFO)
@license: (C) Copyright 2013-2019.    
************************************************
"""
import pytest


# *********+++++++++++*********========*********+++++++++++*********========
#   代码心得:
#       (1)__len()__是为了更好判断增删改查和代码简洁
#       (2) 自定义异常:为什么可以直接FullError("it has fulled"),Exception,BaseException,__init__
#       (3) @property: 以属性的方式来调用方法--只能对实例(实例本身,属性,方法)作用
#       (4)出现错误或者异常的时候,if那句专门用来处理异常(常用于出处理少数情况)---本质上就是对出现少数情况时的一个处理,因为异常和错误本来就是少数情况
# *********+++++++++++*********========*********+++++++++++*********========


class Node():
    """
    创建基本元素节点--Node
    """

    def __init__(self, value=None, next=None):
        """
        初始化节点属性(value与next)
        因为单链表就是只有next这一个指针,主要是指向下一个节点
        节点主要包括两部分,一个是值,一个指向下一个节点的指针,可以先设置为None,之后具体赋值
        :param value:
        :param next:
        """
        self.value = value
        self.next = next

    def __str__(self):
        """
        主要是为了格式化输出        :return:
        """
        print("Node: value:{},next:{}".format(self.value, self.next))


class SingleLinkedList():
    """
    主要操作: 增 删 查,遍历,长度
    """

    def __init__(self, maxsize=None):
        """
        maxsize(容量)的大小设置为None,说明该类型的链表的长度没有限制
        初始化主要涉及: 单链表的容量和根节点,尾节点,和长度--也就是节点的个数(长度和容量是不一样的)这些属性
        单链表的容量:可以预设好,因此可以将其作为关键字参数
        根节点root:因为在链表的初始化,根节点必须要有的,因此需要指定数据类型--Node
        尾节点tail_node:这个在初始化的时候,不做要求,但是后期需要加上
        得出结论:
            看一个属性指定类型,主要看它初始化时候,是不是一定也要进行初始化,否则可以先使用None来进行替代
            否则该属性一定是需要指定数据类型的(例如在这里的length和根结点root)
        一般定义某个类型的初始化时所选的容器:主要有三种情况:
            (1)一个是直接定义一个元素所属的类型(在这里体现为Node类型),然后在Node类型中定义不同Node对象的连接方式
                ,这个常用在链式结构当中,Node类型与Next属性
            (2)一个直接定义保存所有的元素的数据类型:例如前面Bag类型中定义其数据结构为[],在这里元素的类型
                为基本类型.因为是[]类型,因此元素直接的迭代方式已经很明确了.-->常用于线性结构之中
            (3)还有一种更加复杂,就是定义好了保存所有元素的数据结构类型,同时也确定了元素里面的元素里面的迭代方式
                这个主要是数据的维度是二维的情况下--例如外部是List,每个元素是多个键值对的dict类型.
        总结:
            属性的类型在初始化是否需要确定,看其在初始化是不是一定是要确定的;
            类型的容器的选择主要是根据具体问题来分析之后选用不同的数据结构,有时,不单单是线性或者链式结构,
            两者的结合.
        :param maxsize: 单链表的容量,None表示无线容量
        """
        self.maxsize = maxsize
        self.root = Node()
        self.tail_node = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        """
        主要思想:从尾部添加,分成两个部分:
            (1)是否可以添加
            (2)添加的情况:空链表添加,非空链表添加---因为不同的情况,因为指针对应的节点是不一样的
                    加上操作是基于节点,因此需要分开情况计算
        :param value:
        :return:
        """
        # 主要是从链表的尾部添加
        # 判断容量是否足够
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("The singleLinkedList is fulled")

        # 转换成节点
        value_node = Node(value)

        tail_node = self.tail_node

        # (1)空链表添加的情况
        if tail_node is None:

            self.root.next = value_node
        else:

            # 非空链表的添加
            tail_node.next = value_node

        # 既然是尾部添加节点--因此加完之后更新尾部节点--便于下一次添加
        self.tail_node = value_node

        # 长度也即及时更新
        self.length += 1

    def appendleft(self, value):
        """
        头部添加
        :param value:
        :return:
        """

        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("The singleLinkedList is fulled")

        value_node = Node(value)
        if self.tail_node is None:
            self.tail_node = value_node

        # 核心代码,注意一定是先添加连接,之后在断开原有的连接
        head_node = self.root.next
        value_node.next = head_node
        self.root.next = value_node

        # 长度及时更新
        self.length += 1

    def __iter__(self):
        """
        遍历链表
        :return:
        """
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """
        从头部节点开始添加
        :return:
        """
        current_node = self.root.next
        while current_node:
            yield current_node
            current_node = current_node.next

    def remove(self, value):
        """
        删除指定值---需要先进行链表的遍历
        两种情况:
            value对应的节点刚好在尾部节点;
            value值对应的节点不在尾部
        :param value:
        :return:
        """
        # 因此需要将根节点作为前一个节点,主要是为了防止,头结点就是等于value的值
        prebefore_node = self.root

        for node in self.iter_node():
            if node.value == value:
                # 先建立新链接
                prebefore_node.next = node.next
                # 如果节点值刚好在尾部节点
                if node is self.tail_node:
                    # 需要先更新尾部节点的状态,否则会直接删除,丢失尾部节点信息(常犯错误)
                    self.tail_node = prebefore_node
                del node
                self.length -= 1
                return 1
            else:
                # 没有则及时更新前一个节点的信息
                prebefore_node = node
        return -1

    def popleft(self):
        """
        左边删除,一般使用pop方法得到是删除的值
        :return:
        """
        # 判断是否可以进行节点删除--判断链表是是否为空
        if self.length == 0:
            raise Exception("the singleLinkedList is empty")

        head_node = self.root.next
        # 先建立连接
        self.root.next = head_node.next
        self.length -= 1
        value = head_node.value
        # 之后删除对应节点
        del head_node
        return value

    def clear(self):
        """
        清空链表
        :return:
        """
        # 先删除各个节点
        for node in self.iter_node():
            del node

        # 之后重置链表的各个属性
        self.root.next = None
        self.length = 0
        self.tail_node = None

    def reversed(self):
        """
        主要思想: 从头部节点开始,我们需要:
            将正序链表的上一个节点当作 反序链表的下一个节点:current_node.next = prebefore_node
            然后将当前节点更新为下一个节点,将上一个节点更新为当前节点---
                prebefore_node = current_node
                current_node = next_node
        :return:
        """
        current_node = self.root.next
        self.tail_node = current_node
        prebefore_node = None
        while current_node:

            # 先保存真是真实链表的值作为下一个
            next_node = current_node.next
            # 之后将当前的节点的下一个节点重新设置为上一个点--关键代码
            current_node.next = prebefore_node

            if next_node is None:
                # next_node = current_node --因为current_nod
                # 说明是头结点之后没有节点了.因此下个节点就是头结点的本身,不用反序了,
                self.root.next = current_node
            # 更新节点状态,便于遍历
            prebefore_node = current_node
            current_node = next_node

    def find(self, value):
        """
        根据值进行寻找
        :param value:
        :return:
        """
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1


class FullError(Exception):
    pass


class EmptyError(Exception):
    # EmptyError与FullError是相同的初始化本质上相同
    # 显式定义自定义异常的初始化--其实这个可以省略
    def __init__(self, err=None):
        Exception.__init__(self, err)

    @property
    def emptyError2String(self):
        """以属性的方式来调用方法,这样就显得很直观"""
        return str(self)


class QueueWithLinkedList():
    def __init__(self, maxsize=None, ):
        self.maxsize = maxsize
        # 单下划线,说明在内部使用,只是对程序员起一个提示的作用
        self._item_with_singleLinkeList = SingleLinkedList()

    def __len__(self):
        # 设置长度测量方法,目的是为了之后更好对增删查(设置长度的作用)
        return len(self._item_with_singleLinkeList)

    def push(self, value):
        if self.maxsize is not None and len(self._item_with_singleLinkeList) >= self.maxsize:
            # if self.maxsize is not None and len(self) >= self.maxsize:
            # 因为之前已经定义了len(self)的方法,
            # 本质上还是会调用len(self._item_with_singleLinkeList)--为了简约
            raise FullError("it has fulled")  # 自定义异常
        self._item_with_singleLinkeList.append(value)

    def pop(self):
        """
        出队的值为返回值
        :return:
        """
        if len(self._item_with_singleLinkeList) <= 0:
            # 使用的情况--if的设置的情况选择
            raise EmptyError("it is empty")
        return self._item_with_singleLinkeList.popleft()


def testQueueWithLinkedList():
    print(FullError("it has fulled"))
    # 因为FullError继承于Exception,并且Exception又继承BaseException,因此默认由init方法生成一个异常对实例
    """
    具体见这个自定义异常,继承Exception.__init__(self, err),
    其中err可以自定义,因此我们直接使用FullError("it has fulled"),实际也不会报错,
    但是还是会调用Exception.__init__(self, err),因此我们省略了上述步骤--
    但是复杂的操作有利于更好地自定义异常--因此我们根据异常的多少和频繁程度,
    自定义我们是否需要进行自定义异常对详细设置
    
    class DatabaseException(Exception):
    def __init__(self, err='数据库错误'):
        Exception.__init__(self, err)
    """
    simple_queue = QueueWithLinkedList()
    simple_queue.push(0)
    simple_queue.push(1)
    simple_queue.push(2)

    assert len(simple_queue) == 3, "长度不相等"

    assert simple_queue.pop() == 0, "出队元素不为0"
    assert simple_queue.pop() == 1, "出队元素不为1"
    assert simple_queue.pop() == 2, "出队元素不为2"

    assert len(simple_queue) == 0, "出队后长度不一样"

    # 这个主要是测试异常的情况--是否和设置的一致.
    with pytest.raises(EmptyError) as exceInfo:
        simple_queue.pop()

    # exceInfo是ExceptionInfo类型
    print(type(exceInfo))  # <class '_pytest._code.code.ExceptionInfo'>
    # exceInfo.value才是自定义的类型
    print(type(exceInfo.value))  # <class 'DataStructure.用单链表实现简单队列.EmptyError'>
    # 因为是exceInfo.value是自定义类型EmptyError,
    # 默认是没有提供遍历的东西,我们可以设置遍历的方法,在EmptyErro提供一个toString方法,或者直接str()
    # assert "it is empty" == str(exceInfo.value),"为空"

    # 为EmptyError定义一个EmptyError 转string的方法,由于使用@property静态属性注解emptyError2String这个方法
    # 因此我们可以使用以属性的方式来调用方法-->这个很重要--但是参数只能是类型本身的实例(包括实例的属性,方法,实例本身)
    assert "it is empty" == exceInfo.value.emptyError2String, "为空"
