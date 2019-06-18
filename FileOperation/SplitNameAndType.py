#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-17 14:37
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : SplitNameAndType.py
@Description: ==================================
    获取文件名及其后缀名
    # 参考:https://blog.csdn.net/jacke121/article/details/76685759
@license: (C) Copyright 2013-2019.    
************************************************
"""
import os

filePath="/Volumes/软件/OCR数据集/gt_9494.jpg"
# gt_9494.jpg
file_name_with_suffix=os.path.basename(filePath)
# ("gt_9494" , ".jpg")
only_file_name=os.path.splitext(file_name_with_suffix)[0]
