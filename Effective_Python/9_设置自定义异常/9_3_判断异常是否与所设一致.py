#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-03 18:00
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 9_3_判断异常是否与所设一致.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
import pytest


class EmptyError(Exception):
    # EmptyError与FullError是相同的初始化本质上相同
    # 显式定义自定义异常的初始化--其实这个可以省略
    def __init__(self, err=None):
        Exception.__init__(self, err)

    @property
    def emptyError2String(self):
        """以属性的方式来调用方法,这样就显得很直观"""
        return str(self)


def exceptionIsSame():
    with pytest.raises(EmptyError) as exceInfo:
        simple_queue.pop()
    assert "it is empty" == exceInfo.value.emptyError2String, "为空"


if __name__ == '__main__':
    exceptionIsSame()
