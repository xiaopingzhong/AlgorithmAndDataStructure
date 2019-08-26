#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-22 03:17
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 9_2_CatchException.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
from Effective_Python.设置自定义异常.DefineException import testRaise, PreconditionsException


def catchException():
    try:
        # 很关键,指定所抛出的异常类型名称
        testRaise()
    # 因此except直接捕捉的是自定义类型,
    # 而不需要哪种
    # except Exception as e:
    # 此时,因此那个此时e是ExceptionInfo类型
    except PreconditionsException as e:
        print(type(e))  # PreconditionsErr类型
        # 打印异常的名称
        print(e)


if __name__ == '__main__':
    catchException()
