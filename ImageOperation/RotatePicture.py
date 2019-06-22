#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-22 22:21
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : RotatePicture.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""

import cv2


def rotate(image, angle,scale):
    # grab the dimensions of the image
    (h, w) = image.shape[:2]
    # if the center is None, initialize it as the center of
    # the image
    center = (w // 2, h // 2)
    # perform the rotation
    #  -angle位置参数为角度参数负值表示顺时针旋转;
    #  1.0位置参数scale是调整尺寸比例（图像缩放参数），建议0.75
    # 获得旋转的比例,角度和中心点
    M = cv2.getRotationMatrix2D(center, angle, scale)
    # 仿射变换
    rotated = cv2.warpAffine(image, M, (w, h))
    # return the rotated image
    return rotated

