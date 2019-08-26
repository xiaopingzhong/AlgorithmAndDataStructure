#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-03 18:36
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 9_1_DefineException.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""


class FullException(Exception):
    """已经满了的异常"""

    def __init__(self, err=None):
        super(FullException,self).__init__(self, err)

    @property
    def fullExceptiontoString(self):
        return str(self)


class EmptyException(Exception):
    """已经满了的异常"""

    def __init__(self, err=None):
        Exception.__init__(self, err)

    @property
    def emptyExceptiontoString(self):
        return str(self)
