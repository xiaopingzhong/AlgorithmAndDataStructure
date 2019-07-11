#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-11 12:53
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 1_ADT抽象数据类型.py
@Description: ==================================
    定义抽象数据类型
@license: (C) Copyright 2013-2019.    
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
#   xx: 公有变量
#   _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
#   __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问,使用 _Class__object可以访问(因为一切皆对象)
#   __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__,或者很基础的一些操作--加减乘除
#   xx_:单后置下划线,用于避免与Python关键词的冲突
#   参考: https://www.zhihu.com/question/19754941
# *********+++++++++++*********========*********+++++++++++*********========


# *********+++++++++++*********========*********+++++++++++*********========
#   测试结果:https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190711132616.png
# *********+++++++++++*********========*********+++++++++++*********========

class Bag(object):
    def __init__(self,maxsize=10):
        self.maxsize=10
        # self._items=list()
        # 定义承载所有元素的数据结构形式
        self._items=[]

    #  定义特殊加法
    def add(self,item):
        if len(self)>self.maxsize:
            raise Exception
        self._items.append(item)

    def remove(self,item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_Bag():
    # instance Bag
    bag=Bag()

    # call add method
    bag.add(1)
    bag.add(2)
    bag.add(3)

    # call the special method named len
    # 特殊方法的调用方法--直接用文件名调用
    # 显式调用__len__()
    assert bag.__len__()==3,"Bag个数不一致"

    # 普通方法--直接调用即可
    bag.remove(2)
    # 隐式调用--__len__
    assert len(bag)==2,"Bag个数不一致"

    # 隐式调用--__iter__
    for i in bag:
        print("隐式调用打印:")
        print(i)

    # 显式调用使用__iter__
    bag_iter=bag.__iter__()
    for x in bag_iter:
        print(x)

if __name__ == '__main__':
    test_Bag()






