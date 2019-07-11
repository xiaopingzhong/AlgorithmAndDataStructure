#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-11 10:49
@Author  : zxp
@Project : untitled1
@File    : 普通TestCase单例测试.py
@Description: ==================================
    主要的测试模版
@license: (C) Copyright 2013-2019.    
************************************************
"""
from unittest import TestCase,main
from add import add


# *********+++++++++++*********========*********+++++++++++*********========
# 参考视频:https://www.bilibili.com/video/av27203819/?spm_id_from=333.788.videocard.0
# *********+++++++++++*********========*********+++++++++++*********========

# 方式一:一个测试用例,可以测试多个测试函数,这个类主要是实现规范化测试.
# TestAdd集成unittest.TestCase这个测试类



if __name__ == '__main__':
    # unittest.main() 函数会自动调用当前的测试类TestAdd1
    main()


