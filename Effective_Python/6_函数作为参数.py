#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-15 21:44
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 6_函数作为参数.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""


def hi():
    """
    新建一个被调用的函数
    :return:
    """
    print("这个是被调用的函数,测试打印输出")


def callFunctionByName(function_name):
    """
    根据函数名称实现作为参数
    :param function_name:
    :return:
    """
    function_name()


if __name__ == '__main__':
    # 是传递函数名称,不是字符串
    function_name = hi
    callFunctionByName(function_name)