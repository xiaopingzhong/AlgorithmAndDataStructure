#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019/5/6 5:06 PM
@Author  : zxp
@Project : OCR-CTPN
@File    : dataSetSegment.py
@Description: ==================================
    数据集划分,划分为6:2:2
@license: (C) Copyright 2013-2019.
************************************************
Created on Wed Oct  3 22:13:52 2018
@author: 天蓝蓝铭靓靓+zxp
"""

import os
import random
import shutil


def divideDataset(Train_dir, Valid_dir, Test_dir, train_percentage, valid_percentage):
    if not os.path.exists(Valid_dir):
        os.mkdir(Valid_dir)
    if not os.path.exists(Test_dir):
        os.mkdir(Test_dir)
    pictures = os.listdir(Train_dir)
    random.shuffle(pictures)
    # for folder in pictures:
    #     # dir = Train_dir + '/' + folder + '/'
    #     # if not os.path.exists(Test_dir + '/' + folder + '/'):
    #     #     os.mkdir(Test_dir + '/' + folder + '/')
    #     # pictures = os.listdir(dir)
    train_num = int(len(pictures) * train_percentage)
    valid_num = int(len(pictures) * valid_percentage)
    for i in pictures[train_num:train_num + valid_num]:
        shutil.move(dir + i, Test_dir + '/')
    for i in pictures[train_num + valid_num:]:
        shutil.move(dir + i, Valid_dir + '/')


if __name__ == '__main__':
    Train_dir = "/data/zxp/tf_ctpn/data/dataset/mlt/label"
    Test_dir = "/data/zxp/tf_ctpn/data/dataset/test_gt"
    Valid_dir = "/data/zxp/tf_ctpn/data/dataset/valid_gt"
    train_percentage = 0.6  # 训练集比例，(0,1)
    valid_percentage = 0.2
    divideDataset(Train_dir, Valid_dir, Test_dir, train_percentage, valid_percentage)
