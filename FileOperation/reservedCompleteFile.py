#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-05-18 23:27
@Author  : zxp
@Project : OCR-ctpn
@File    : reservedCompleteFile.py
@Description: ==================================
    标签文件与图像文件进行比对
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


def getFilePathDict(files1_path_l, files2_path_l):
    directory_dict = {}
    for x in files1_path_l:
        (filepath, tempfilename) = os.path.split(x)
        (filename_x, extension) = os.path.splitext(tempfilename)
        for y in files2_path_l:
            (filepath, tempfilename) = os.path.split(y)
            (filename_y, extension) = os.path.splitext(tempfilename)
            if filename_x == filename_y:
                directory_dict[x] = y
                break
            else:
                continue

    return directory_dict


def getMergeResult(files1_path_l, files2_path_l):
    directory_dict = getFilePathDict(files1_path_l, files2_path_l)
    for x, y in zip(files1_path_l, files2_path_l):
        if x not in directory_dict:
            os.remove(x)
            os.remove(y)

    return None


if __name__ == '__main__':
    file1_directory = "/Users/ivega/Downloads/ICPR/train/image_9000/"
    file2_directory = "/Users/ivega/Downloads/ICPR/train/txt_9000/"
    files1_path_l = get_sub_files(file1_directory)
    files2_path_l = get_sub_files(file2_directory)
    getMergeResult(files1_path_l, files2_path_l)
