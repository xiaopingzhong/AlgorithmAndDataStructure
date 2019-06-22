#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-22 22:09
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : RotateWithAlpha_Opencv.py
@Description: ==================================
    添加alpha通道并旋转--opencv方式--缺点:旋转的resize不好确定,但是通用
@license: (C) Copyright 2013-2019.    
************************************************
"""

import os
import numpy as np
import cv2

from ImageOperation.RotatePicture import rotate


def rorateWithAlpha(image_dir,angle,scale):
    """
    带有透明度的旋转
    :param image_dir: 图片目录
    :param angle: 旋转角度
    :param scale:
    :return:
    """

    # get absolute path about every image in the directory named data_dir
    image_l=os.listdir(image_dir)
    image_l=[os.getcwd()+"/data_test/"+x for x in image_l]
    image_l.sort()
    print(image_l)

    # add alpha to the image whose suffix is PNG or png
    for input_file in image_l:
        # BGR ndArray
        img=cv2.imread(input_file)
        # check the channel
        if img.ndim!=4:
            b_channel, g_channel, r_channel = cv2.split(img)
            alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # creating a dummy alpha channel image.
            img = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

        # rotate the current image
        rotated=rotate(img, angle,scale)

        # save the rotated image
        basename = os.path.basename(input_file)
        filename = os.path.splitext(basename)[0]
        ext = os.path.splitext(basename)[1]
        cv2.imwrite(filename + "_ImageCorrection_Huff" + ext, rotated)


if __name__ == '__main__':
    image_dir = "./data_test/"
    angle=90
    # scale: symbol the shrink  ratio :缩放比例
    scale=0.75
    rorateWithAlpha(image_dir,angle,scale)
