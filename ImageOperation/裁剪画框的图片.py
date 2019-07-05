#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-01 21:23
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : cutImage.py
@Description: ==================================
    根据BBOX裁剪图片
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
    with open(bbox_path, mode='r') as f:
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


def findMinAndMaxAxis(axis_l):
    """
    search min point, max point
    :param axis_l:
    :return:
    """
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


def cropImage(one_image_path, one_point_path):
    """
    剪切单张图片
    :param one_image_path:
    :param one_point_path:
    :return:
    """
    im_fn = os.path.basename(one_image_path)
    # ndarray
    img = cv2.imread(one_image_path)
    # (?,8)--ndarray
    boxes = readBox2NdArray(one_point_path)
    for i, box in enumerate(boxes):
        # cv2.polylines(img, [box[:8].astype(np.int32).reshape((-1, 1, 2))], True, color=(0, 255, 0),
        #               thickness=2)
        box_l = list(box)
        min_point, max_point = findMinAndMaxAxis(box_l)
        # ***********************core code******************************************
        img1 = img.copy()
        crop_img = img1[int(min_point[1]):int(max_point[1]), int(min_point[0]):int(max_point[0])]
        # print(box[5])
        # exit(1)
        # ***********************core code******************************************
        basename = os.path.basename(im_fn)
        basename = os.path.splitext(basename)[0] + "-{}".format(i) + os.path.splitext(basename)[1]
        if not os.path.exists(OUT_PATH):
            os.makedirs(OUT_PATH)
        # ***********************core code******************************************
        cv2.imwrite(os.path.join(OUT_PATH, basename), crop_img)
        # ***********************core code******************************************


def sum_cropImage(image_dir, point_dir):
    # 裁剪目录下所有图片
    img_l = os.listdir(image_dir)
    point_l = os.listdir(point_dir)
    for x in img_l:
        img_filename = os.path.splitext(x)[0]
        for y in point_l:
            point_filename = os.path.splitext(y)[0]
            # 图片文件名和标签文件名前缀一样
            if img_filename == point_filename:
                cropImage(image_dir + "/" + x, point_dir + "/" + y)
            else:
                continue


if __name__ == '__main__':
    # 剪切结果输出目录
    OUT_PATH = "./result"
    # 原始图片目录
    image_dir = "./data/image"
    # 预测图片的对应的文本框
    point_dir = "./data/label"
    sum_cropImage(image_dir, point_dir)
