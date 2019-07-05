#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-05 11:28
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 找出框对角线上的两个坐标.py
@Description: ==================================
    找出最大与最小的坐标(也就是对角线上的两个坐标)--为了裁剪图片
@license: (C) Copyright 2013-2019.    
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
#   input: [1410, 526, 1410, 485, 1562, 485, 1562, 526]
#   out:[1410, 485] [1562, 526]
# *********+++++++++++*********========*********+++++++++++*********========

def findMinAndMaxAxis(axis_l: list):
    axil_pair_l = []
    for x, y in zip(axis_l[::2], axis_l[1::2]):
        axil_pair_l.append([x, y])

    # search the max Coordinate point
    min = axil_pair_l[0]
    for per in axil_pair_l[1:]:
        if min[0] >= per[0] and min[1] >= per[1]:
            min = per
        else:
            continue

    # search the max Coordinate point
    max = axil_pair_l[0]
    for seg in axil_pair_l[1:]:
        if seg[0] >= max[0] and seg[1] >= max[1]:
            max = seg
        else:
            continue

    return min, max


if __name__ == '__main__':
    bbox_point = [1410, 526, 1410, 485, 1562, 485, 1562, 526]
    min_point, max_point = findMinAndMaxAxis(bbox_point)
    # [1410, 485] [1562, 526]
    print(min_point, max_point)
