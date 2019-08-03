#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-22 03:17
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : CatchException.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
from Effective_Python.设置自定义异常.DefineException import testRaise, PreconditionsException


def catchException():
    try:
        # 很关键,指定所抛出的异常类型名称
        testRaise()
    except PreconditionsException as e:
        # 打印异常的名称
        print(e)


if __name__ == '__main__':
    catchException()
