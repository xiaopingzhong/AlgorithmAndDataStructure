#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-01 21:36
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : NdArray是否为空判断.py
@Description: ==================================
    
@license: (C) Copyright 2013-2019.    
************************************************
"""

# *********+++++++++++*********========*********+++++++++++*********========
# >>> import numpy as np
# >>> np.array(None).size
# 1
# >>> np.array(None).shape
# ()
# >>> np.prod(())
# 1.0
# 因此ndarray为None的时候,不为空,这个需要注意,为()
# *********+++++++++++*********========*********+++++++++++*********========
import cv2
import numpy as np
import os


def judgeNdArrayisNone(one_img_path):
    """
    judge the imread result
    """
    img = cv2.imread(one_img_path)
    # judge the img whether or not None in order to interrupt
    # if None,we choose skip the picture
    #################core code########################
    if np.array(img).shape == ():
        return np.array(img)
    else:
        return img
    #################core code########################


def AfterJudgeDoSomething(images_path):
    """
    choose the skip the image
    :return:
    """
    # Only Get the fileName
    images_l = os.listdir(images_path)
    for x in images_l:
        img = judgeNdArrayisNone(x)
        if img.shape == ():
            continue
        pass
