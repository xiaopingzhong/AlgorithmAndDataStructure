#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-05-29 19:50
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : GetAllFileInDirecoty.py
@Description: ==================================
    递归获取所有目录下的文件，返回各个文件的具体路径
@license: (C) Copyright 2013-2019.    
************************************************
"""
import os


def get_sub_files(dir_path, recursive=False):
    """
    获取目录下所有文件名，返回文件路径
    :param dir_path:
    :param recursive: 是否递归
    :return:
    """
    file_paths = []
    for dir_name in os.listdir(dir_path):
        cur_dir_path = os.path.join(dir_path, dir_name)
        if os.path.isdir(cur_dir_path) and recursive:
            # 递归获取所有的文件的路径
            file_paths = file_paths + get_sub_files(cur_dir_path)
        else:
            # 否则添加到列表当中
            file_paths.append(cur_dir_path)
    return file_paths