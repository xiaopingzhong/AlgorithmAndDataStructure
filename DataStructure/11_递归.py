#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-03 09:48
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 11_递归.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
from collections import deque


# *********+++++++++++*********========*********+++++++++++*********========
#  学习部分:
#       用栈实现递归,把每次得到的临时变量压入到栈中
#       为提高效率,这次使用的是python内置的双端队列--只在受限的一端(通常是尾部)进行
# *********+++++++++++*********========*********+++++++++++*********========

class Stack(object):
    """使用双端队列,实现左端进,右端出"""
    def __init__(self):
        self.stack_with_deque = deque()

    def push(self, value: object) -> None:
        self.stack_with_deque.append(value)

    def pop(self):
        return self.stack_with_deque.popleft()

    def judgeStackEmpty(self):
        return len(self.stack_with_deque)


def printNumberRecursion(n):
    """以栈的方式,实现递归输出,自主设定n的范围"""
    stack_with_deque = Stack()
    while n > 0:
        stack_with_deque.push(n)
        n -= 1

    while stack_with_deque.judgeStackEmpty():
        """有时候需要判断某个数据结构是否为空,式子比较长或者比较复杂,单独成函数"""
        print(stack_with_deque.pop())

if __name__ == '__main__':
    """对0-10进行递归--注意这种写法"""
    printNumberRecursion(10)