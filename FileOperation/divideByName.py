#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019/5/6 5:06 PM
@Author  : zxp
@Project : OCR-CTPN
@File    : divideByName.py
@Description: ==================================
    根据划分之后GT文件,获取对应的图像文件
@license: (C) Copyright 2013-2019.
************************************************
"""

import os
import shutil


def divideImagesByGtName(test_gt_path,Train_Image_path,test_image_path):
    """
    根据拆分的gt文件,移动对应的图像文件
    :param test_gt_path:
    :param Train_Image_path:
    :param test_image_path:
    :return:
    """
    # complete fileName include suffix ---list
    picture_l = os.listdir(test_gt_path)
    # delete the suffix of picture_l
    picture_name_no_suffix_l=[os.path.splitext(x)[0] for x in picture_l]
    for x in picture_name_no_suffix_l:
        complete_name_str=x+".jpg"
        # print(complete_name_str)
        if complete_name_str in os.listdir(Train_Image_path):
            # print(1)
            shutil.move(Train_Image_path + complete_name_str, test_image_path)
        else:
            continue

if __name__ == '__main__':
    # 已经拆分的文件
    test_gt_path="/data/zxp/tf_ctpn/data/dataset/test_gt/"
    # 总图像文件
    Train_Image_path="/data/zxp/tf_ctpn/data/dataset/Train/image/"
    # 需要图像的存储的路径
    test_image_path="/data/zxp/tf_ctpn/data/dataset/Test/test_image/"
    divideImagesByGtName(test_gt_path, Train_Image_path, test_image_path)