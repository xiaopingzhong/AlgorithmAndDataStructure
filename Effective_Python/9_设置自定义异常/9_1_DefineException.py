#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-22 03:20
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 9_1_DefineException.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""


class DatabaseException(Exception):
    def __init__(self, err='数据库错误'):
        Exception.__init__(self, err)


class PreconditionsException(DatabaseException):
    def __init__(self, err='PreconditionsErr'):
        DatabaseException.__init__(self, err)


def testRaise():
    raise PreconditionsException()
