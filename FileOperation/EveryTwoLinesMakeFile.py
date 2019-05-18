#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-05-18 23:27
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : EveryTwoLinesMakeFile.py
@Description: ==================================
    每两行单独成为一个文件
@license: (C) Copyright 2013-2019.    
************************************************
"""

import os


def everyTwoLineMakeFile(filePath):
    """
    每读取文件的两行单独成为一个文件;
    具体结果为:
    ![1](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190519000224.png)
    ![2](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190519000331.png)
    :rtype: object
    :param filePath:
    :return:
    """
    result = []
    """
    with就是为了防止文件忘了关闭,导致数据只写入一部分,因为系统不是
    'r':代表对文件的操作模式,读取出来的是字符串,
    'rb':read binary :返回的是字节,w与wb类似,
    r+则是读写都可以
    encoding主要是为了以某种编码格式进行文件读取;
    errors主要是为了文件以某件编码格式进行读取的时候,
    文件有编码不规范的现象出现UnicodeDecodeError;
    """
    with open(filePath, 'r', encoding='utf-8', errors='ignore') as f1:
        for x in zip(f1.readlines()):
            result.append(x)
    n = 1
    count = 1
    path = '/Users/ivega/Desktop/xx/file/sep'
    # 设置文件的存储路径
    os.chdir(path)
    # 新建一个文件
    file = open(str(n) + '.txt', 'w')
    for i in range(len(result)):  # 一行行的把数据从硬盘加载到内存里读出来
        if (count == 1):
            # 将tuple数据转换为字符串str数据
            file.write(" ".join(tuple(result[i])).strip(' \u200b\u200b\u200b'))
            # 每写入一次,count就会加一
            count = 2
            print(result[i])
        else:
            # count = 2时还会再写入一行,第二行
            file.write(" ".join(tuple(result[i])).strip('\u200b\u200b\u200b').strip('\n'))
            print(result[i])
            # 得到新的文件名
            n += 1
            file = open(str(n) + '.txt', 'w')
            count = 1
    # 最后文件写完之后记得保存
    file.close()


if __name__ == '__main__':
    filePath="/Users/ivega/Desktop/xx/file/result.txt"
