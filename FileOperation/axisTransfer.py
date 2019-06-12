
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019/5/6 5:06 PM
@Author  : zxp
@Project : OCR-CTPN
@File    : axisTransfer.py
@Description: ==================================
    读取不同数据集之间坐标之间的转换,转换为顺时针的形式
@license: (C) Copyright 2013-2019.
************************************************
"""

import os


def get_sub_files(dir_path, recursive=False):
    """
    获取目录下所有文件名
    :param dir_path:目录名
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


def axisTransfer(files_dir):
    filepath_l = get_sub_files(files_dir)
    for x in filepath_l:
        fileName = os.path.basename(x)
        f_new = open(fileName, 'w+', encoding='utf-8')
        with open(x, mode='r',encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                print("转换之前：")
                print(line)
                axis_l = line.split(",", maxsplit=8)
                temp0, temp1 = axis_l[2], axis_l[3]
                axis_l[2], axis_l[3] = axis_l[6], axis_l[7]
                axis_l[6], axis_l[7] = temp0, temp1
                line=",".join(axis_l[0:8])
                line=line+"\n"
                print("转换之后：")
                print(line)
                f_new.write(line)


if __name__ == '__main__':
    os.chdir("/Users/ivega/Desktop/1/nn1/")
    file_dir="/Users/ivega/Desktop/1/nn/"
    axisTransfer(file_dir)

