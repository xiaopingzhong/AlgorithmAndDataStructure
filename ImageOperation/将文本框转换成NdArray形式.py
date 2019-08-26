#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-01 21:24
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 将文本框转换成NdArray形式.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""

def readBox2NdArray(bbox_path):
    """
    make the box about point into the ndarray
    :param bbox_path:
    :return:
    """
    sum_point_l = []
    with open(bbox_path, mode='r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        for x in lines:
            numerical_l = x.split(",")[:8]
            # removeNode the "\n" and transfer into float
            for i, x in enumerate(numerical_l):
                if '\n' in x:
                    new_x = x.replace("\n", "")
                    new_x = float(new_x)
                else:
                    new_x = float(x)
                numerical_l[i] = new_x
            sum_point_l.append(numerical_l)
    # Transfer from string to int
    # sum_point_l = [float(p) for p in numerical_l]

    sum_point_arr = np.array(sum_point_l)
    # print(sum_point_arr)
    return sum_point_arr