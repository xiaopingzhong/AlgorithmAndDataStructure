#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-15 19:52
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 3_pycallgraph函数调用.py
@Description: ==================================
    主要是对函数运行图的构建
@license: (C) Copyright 2013-2019.    
************************************************
"""

# *********+++++++++++*********========*********+++++++++++*********========
#   命令行:
#       pycallgraph graphviz --output-file=setup.png --include=['Node.*', "mainProcess"] 3_pycallgraph函数调用.py
#       pycallgraph graphviz -- ./test.py  生成pycallgraph图片
# *********+++++++++++*********========*********+++++++++++*********========

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import Config
from pycallgraph import GlobbingFilter


def mainProcess():
    pass


if __name__ == '__main__':
    config = Config()
    # #如果是某一类的函数，例如类gobang，则可以直接写'gobang.*'，
    # 表示以gobang.开头的所有函数。（利用正则表达式）
    # 主程序函数名也要写进去
    # exclude作用是关系图中不包括(exclude)哪些函数。(正则表达式规则)
    config.trace_filter = GlobbingFilter(include=['Node.*', "mainProcess"],
                                         exclude=[
                                             'pycallgraph.*',
                                             '*.secret_function'
                                         ])
    graphviz_output = GraphvizOutput()
    graphviz_output.output_file = "graph.png"
    with PyCallGraph(output=graphviz_output, config=config):
        # 主函数运行
        mainProcess()
