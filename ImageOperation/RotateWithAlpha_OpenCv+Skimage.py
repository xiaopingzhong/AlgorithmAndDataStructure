#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-22 22:31
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : RotateWithAlpha_OpenCv+Skimage.py
@Description: ==================================
    skimage与opencv相结合的旋转
@license: (C) Copyright 2013-2019.    
************************************************
"""

import cv2
import os
import numpy as np
from skimage.transform import rotate
from skimage import io


# *********+++++++++++*********========*********+++++++++++*********========
#  reference article:
#   Python 中各种imread函数的区别与联系:https://blog.csdn.net/guduruyu/article/details/71440186
#   opencv imread读取alpha通道: http://www.voidcn.com/article/p-dppkkysa-vh.html
#   python OpenCV – 将alpha通道添加到RGB图像:https://codeday.me/bug/20190115/514559.html
#
#  result:
#   ![rotate_result](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/alpha.gif)
# *********+++++++++++*********========*********+++++++++++*********========


def rotateWithAlpha_OpenCvSkimage(image_dir,rot_angle):
    # get every image's absolute path in the directory named image_dir
    image_l=os.listdir(image_dir)
    image_l=[os.getcwd()+"/data_test/"+x for x in image_l]
    image_l.sort()
    print(image_l)
    for input_file in image_l:
        # BGR nd-Array
        img=cv2.imread(input_file)
        # check the image channel
        if img.ndim!=4:
            b_channel, g_channel, r_channel = cv2.split(img)
            alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # creating a dummy alpha channel image.
            img = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

        # Because io.imread's output--RGB ndArray
        # cv2.imread output--BGR ndArray
        # what's more, added the alpha channel
        # need BGRA-->RGBA
        img=bgra2rgba(img)

        # use skimage.transform import rotate(),resize is useful
        rotated = rotate(img, rot_angle, resize=True)

        # save the rotated image
        basename = os.path.basename(input_file)
        filename = os.path.splitext(basename)[0]
        ext = os.path.splitext(basename)[1]
        # use io.imsave not cv2.imwrite
        io.imsave(filename + "_ImageCorrection_Huff" + ext, rotated)



## BGRA to RGBA.
def bgra2rgba(img):
    a = alpha(img)
    rgba = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    if a is not None:
        rgba[:, :, 3] = a
    return rgba


def alpha(img):
    if len(img.shape) == 2:
        return None
    cs = img.shape[2]
    if cs != 4:
        return None
    return img[:, :, 3]


if __name__ == '__main__':
    image_dir = "./data_test/"
