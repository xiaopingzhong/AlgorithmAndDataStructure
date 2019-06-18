#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-18 14:46
@Author  : zxp
@Project : text-detection-ctpn 3
@File    : ImageCorrection.py
@Description: ==================================
    对不同图片进行对应的画框
@license: (C) Copyright 2013-2019.
************************************************
"""

import cv2 as cv
import os
import numpy as np

DATA_FOLDER = "/data/zxp/DATASET/Train/LSVT/"
OUTPUT = "/data/zxp/DATASET/Train/mlt/"


def writebox(image_path, gt_path):
    im_fns_l = os.listdir(os.path.join(image_path, "image"))
    im_fns_l.sort()
    for im_fn in im_fns_l:
        image = cv.imread(im_fn)
        # get complete filename
        basename = os.path.basename(image_path)
        # get the filename without ext
        bfn = os.path.splitext(basename)[0]
        with open(os.path.join(gt_path, "label", bfn) + ".txt", "w") as f:
            lines = f.readlines()
        for line in lines:
            # str.strip()就是把字符串(str)的头和尾的空格，以及位于头尾的\n \t之类给删掉。
            splitted_line = line.strip().lower().split(',')
            # #map() 会根据提供的函数对指定序列做映射。第一个参数 function
            # 以参数序列中的每一个元素调用 function 函数，
            # 返回包含每次 function 函数返回值的新列表。
            # clockwise situation
            x1, y1, x2, y2, x3, y3, x4, y4 = map(float, splitted_line[:8])
            # print(x1, y1, x4, y4, x3, y3, x2, y2)
            poly = np.array([x1, y1, x2, y2, x3, y3, x4, y4]).reshape([4, 2])
            #  thickness represent the Line thickness
            # image has line

            # *********+++++++++++*********========*********+++++++++++*********========
            # annother line method: cv2.rectangle确实是靠 确定对角线 来画矩形的
            #  cv.rectangle(image, (p[0], p[1]), (p[2], p[3]), color=(0, 0, 255), thickness=1)
            # *********+++++++++++*********========*********+++++++++++*********========
            cv.polylines(image, [poly.astype(np.int32).reshape((-1, 1, 2))], True, color=(0, 255, 0), thickness=2)
        cv.imwrite(os.path.join("./result/", os.path.basename(image_path)), image)
        # cv2.imshow("imput", image)
        # cv2.imshow("output", rotated)
        # 无限制等待用户的触发,常与imshow()使用
        # cv2.waitKey(0)

if __name__ == '__main__':
    image_path= DATA_FOLDER
    gt_path = OUTPUT
    writebox(image_path, gt_path)


