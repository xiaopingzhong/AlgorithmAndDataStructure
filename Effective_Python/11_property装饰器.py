#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-24 00:02
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 11_property装饰器.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
# property的getter, setter和deleter方法同样可以用作装饰器：
# @property是一个很好的装饰器，避免使用  显式  的setter和getter函数--但是缺点就是:空间开销比较大
# 三种类型: property,setter,deleter
class C(object):
    def __init__(self):
        self._x = None

    @property #是一个装饰器
    # 在这里就相当于是一个getter方法了
    # 获得当前的值,至于获得什么属性(或者哪几个)的值自己可以选择
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    # 注意函数名还是为x ,但是参数个数不一样了,多了一个赋值参数,至于具体
    # 赋值那个属性,自己选择
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
