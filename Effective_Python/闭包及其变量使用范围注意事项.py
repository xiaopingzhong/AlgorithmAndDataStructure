#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-12 01:08
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 闭包及其变量使用范围注意事项.py
@Description: ==================================
    获取python的闭包里面的值,或者可以理解为对闭包里面变量的值的获取
    看能不能获取,主要是看内外两个同名变量是不是同时共享同一个内存id(重点)
    一般不可变的数据类型进行赋值,那么就不能获取里面的值,--
    主要是为了局部变量污染全局变量(也就是改变全局变量的地址).
    --因为闭包里面就相当于生成一个新的同名变量.
    除非在里面的变量加上nonlocal

@license: (C) Copyright 2013-2019.    
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
#  found_1 = [False]-->found_1 = [True]-->found_1: [False]
#   found_1 = [False]-->found_2[0] = True-->found_2: [True]
# *********+++++++++++*********========*********+++++++++++*********========

def sort_priority2(numbers, group):
    # found = False
    found_1 = [False]
    found_2 = [False]

    def helper(x):
        if x in group:
            # 因为它是对整个列表进行变动,因此变量的内存id会进行改变--一般变量会有灰色,
            # 说明没有引用到.--或者是局部变量着要引起注意
            # found_1 = [True]

            # 加上nonlocal的声明(其作用范围主要是在本文件之内)--修改成功,就是将其转换成非局部变量
            nonlocal found_1
            found_1= [True]

            # 她只是对列表当中的元素进行改变,因此原先的变量和此时的变量是共享一个内存id的
            found_2[0] = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found_1, found_2


if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    result_1, result_2 = (sort_priority2(numbers, group))
    print("found_1: {}\nfound_2: {}".format(result_1, result_2))
