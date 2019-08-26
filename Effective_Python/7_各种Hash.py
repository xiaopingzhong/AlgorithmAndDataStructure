#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-04 16:19
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 7_各种Hash.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""


# __hash__方法返回一个整数，用来表示该对象的唯一标识，配合__eq__方法判断两个对象是否相等(==)：
# http://kaito-kidd.com/2017/02/22/python-magic-methods/
class Person(object):
    def __init__(self, uid):
        self.uid = uid

        def __repr__(self):
            return 'Person(%s)' % self.uid

    def __hash__(self):
        return self.uid

    def __eq__(self, other):
        return self.uid == other.uid


p1 = Person(1)
p2 = Person(1)
p1 == p2  # True
