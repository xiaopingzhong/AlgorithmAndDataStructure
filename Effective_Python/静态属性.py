#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-14 22:57
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 静态属性.py
@Description: ==================================
    主要是对静态属性的本质及其应用场景进行说明
@license: (C) Copyright 2013-2019.    
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
# 静态属性:
# 若想方便使用想将类的函数属性同对象的数据属性一样可供对象直接调用，可以在类中的函数前加上装饰器@property，这样就将函数属性
# 转换为类似数据属性一样可供直接调用（封装）
# 但是不可被修该（不同于数据属性），静态属性可以访问类的数据属性和实例的数据属性
# 静态属性不可传参数,(只有self)
# 类的实例默认无法修改静态属性(重点)
# 被@property装饰的方法只能看着是一个属性，不能加()来调用
# 参考: https://blog.csdn.net/qq_29053519/article/details/86483213
# *********+++++++++++*********========*********+++++++++++*********========


# *********+++++++++++*********========*********+++++++++++*********========
#       静态属性本质上就是以函数的形式,对原有的数据进行操作--因此参数只能为self,也就是对象本身
#   因此常将静态属性应用在 需要对对象本身的属性进行比较的复杂的操作上.--因此实现好操作之后
#   我们就相应的函数添加@property,实现对对象的属性操作结果进行封装.其实就
#   相当于为对象新产生了一个属性
# *********+++++++++++*********========*********+++++++++++*********========


class cal:
    cal_name = '计算器'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property  # 在cal_add函数前加上@property，使得该函数可直接调用，封装起来
    def cal_add(self):
        return self.x + self.y


c = cal(10, 11)
print(c.cal_name)  # >>> '计算器'   调用类的数据属性
print(c.cal_add)  # >>> 21  这样调用类函数属性看起来跟调用数据属性一样  c.cal_name
# c.cal_add = 10  # 这样修改会报错，因为不可被修改
