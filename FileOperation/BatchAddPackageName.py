#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-05-18 23:50
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : BatchAddPackageName.py
@Description: ==================================
    批量添加依赖名
@license: (C) Copyright 2013-2019.    
************************************************
"""


def batchAddPackageName(file1Path, file2Path):
    """
    file1Path的内容是项目所需要的依赖名,可以自动生成,也可以自动添加
    file2Path的内容则是格式化写入之后的结果:目的是为了在docker中使用
    ---RUN pip install  --index https://pypi.mirrors.ustc.edu.cn/simple/ numpy
    具体DockerFile文件信息查看:https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190518235839.png
    :return:None
    """
    ff = open(file2Path, 'w')
    with open(file1Path, 'r') as f:
        line = f.readlines()
        for line_list in line:
            line_new = 'RUN pip install  --index https://pypi.mirrors.ustc.edu.cn/simple/ ' + line_list
            ff.write(line_new)


if __name__ == '__main__':
    file1Path = "./old.txt"
    file2Path = "./ new.txt"
    batchAddPackageName(file1Path, file2Path)
