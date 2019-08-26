#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-14 23:39
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 2_静态属性,静态方法,类方法.py
@Description: ==================================
    静态属性,静态方法,类方法的比较和解释
@license: (C) Copyright 2013-2019.    
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
#   静态属性:主要是对属性(类属性或者初始化属性--对象属性)进行操作---self,因为初始化属性比类属性等级更高.
#   静态方法:为类的使用做铺垫,但是不引用类或者实例--设置环境变量--(一般不使用self,cls,虽然不报错)
#   类方法: 会引用到类,但是不需要类的实例化--例如查看类的名称,返回类的属性(不是初始化属性),因为cls就相当于是一个类的实例
#   参考:
#       [python大作战之静态属性，静态方法，继承等综合代码练习](https://blog.csdn.net/qq_29053519/article/details/86483213)
#       [python(八)：静态属性、类方法、静态方法](https://blog.csdn.net/ak739105231/article/details/85721271)
# *********+++++++++++*********========*********+++++++++++*********========

class People(object):
    # 类的属性
    name = "张三"

    def __init__(self, age=10):
        # 初始化属性
        self.age = age
        # 私有属性
        # 因为这个静态属性是对原有属性进行操作,
        # 因此初始化的时候不需要指定类型
        self.__hobby = None
        self.shop = "购物"

    @classmethod
    def running(cls, value):
        """
        类方法
        :return:
        """
        return people.name, value

    @staticmethod
    def eat(food):
        """
        静态方法参数可以加self,cls之类的
        :param food:
        :return:
        """
        print("{} likes {}".format(people.name, food))

    @property
    def hobby(self):
        """
        静态属性
        property主要是弥补python当中没有setter和getter
        """
        return age

    @hobby.setter
    def hobby(self, value):
        # 就会调用静态属性hobby的setter方法
        self.__hobby = value



if __name__ == '__main__':
    people = People(10)
    # 在开发中，我们常常需要定义一些方法，这些方法跟类有关，
    # 但在实现时并不需要引用类或者实例，例如，设置环境变量，修改另一个类的变量，
    # 等。这个时候，我们可以使用静态方法.
    People.eat("马铃薯")
    # 例如查看类的名称--不需要实例化,但是需要引用类,或者类的属性(不是初始化属性)
    print(People.running(value=10))
    age=33
    print(people.hobby)
    age=44
    print(people.hobby)
