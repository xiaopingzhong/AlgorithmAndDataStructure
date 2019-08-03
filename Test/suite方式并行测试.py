#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-11 12:38
@Author  : zxp
@Project : untitled1
@File    : suite方式并行测试.py
@Description: ==================================
    多个测试用例 并行测试--suite方式
@license: (C) Copyright 2013-2019.    
************************************************
"""
import unittest
from unittest import TestCase

from Test.add import add


#*********+++++++++++*********========*********+++++++++++*********========
#   多个测试样例进行联合测试--suite集合(将多个测试样例装进suite集合当中)
#*********+++++++++++*********========*********+++++++++++*********========


class TestAdd1(TestCase):
    # 可以同时测试多个函数--测试函数1
    def test_add(self):
        """
        真正测试部分可以自己自定义
        :return:
        """
        add_result = add(1, 2)
        # assert 表达式,断言错误信息
        assert add_result == 3, "相加结果正确"

    # 测试函数2
    def test_mul(self):
        """
        真正测试部分可以自己自定义
        :return:
        """
        mul_result = 1 * 2
        # assert 表达式,断言错误信息
        # 成功则不报错会继续执行下去,不成功的话,则会进行有报错信息---AssertionError: 相乘结果错误
        assert mul_result == 3, "相乘结果错误"


class TestAdd2(TestCase):

    # 可以同时测试多个函数--测试函数1
    def test_add(self):
        """
        真正测试部分可以自己自定义
        :return:
        """
        add_result = add(1, 2)
        # assert 表达式,断言错误信息
        assert add_result == 2, "相加结果正确"

    # 测试函数2
    def test_mul(self):
        """
        真正测试部分可以自己自定义
        :return:
        """
        mul_result = 1 * 2
        # assert 表达式,断言错误信息
        # 成功则不报错会继续执行下去,不成功的话,则会进行有报错信息---AssertionError: 相乘结果错误
        assert mul_result == 2, "相乘结果错误"


if __name__ == '__main__':
    # 转换成TestSuite类型的
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAdd1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestAdd2)

    # 将两个TestSuite类型的放进suite集合当中
    suite = unittest.TestSuite([suite1, suite2])

    # 进行suite集合测试--verbosity=2代表测试的样例类个数
    unittest.TextTestRunner(verbosity=2).run(suite)
