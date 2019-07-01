#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-01 21:23
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 裁剪画框的图片.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""
import os
import cv2
import numpy as np


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
            # remove the "\n" and transfer into float
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


def cropImage(one_image_path,one_point_path):
    im_fn=os.path.basename(one_image_path)
    # ndarray
    img=cv2.imread(one_image_path)
    # (?,8)--ndarray
    boxes=readBox2NdArray(one_point_path)
    for i, box in enumerate(boxes):
        cv2.polylines(img, [box[:8].astype(np.int32).reshape((-1, 1, 2))], True, color=(0, 255, 0),
                      thickness=2)
        img1 = img.copy()

        #***********************core code******************************************
        crop_img = img1[box[1]:box[5], box[0]:box[4]]
        # ***********************core code******************************************
        basename = os.path.basename(im_fn)
        basename = os.path.splitext(basename)[0] + "-{}".format(i) + os.path.splitext(basename)[1]
        if not os.path.exists(OUT_PATH):
            os.makedirs(OUT_PATH)
        # ***********************core code******************************************
        cv2.imwrite(os.path.join(OUT_PATH, basename), crop_img)
        # ***********************core code******************************************

if __name__ == '__main__':
    OUT_PATH="./data/"
    one_image_path="./test/1.jpg"
    one_point_path="./test/2.txt"
    cropImage(one_image_path,one_point_path)
