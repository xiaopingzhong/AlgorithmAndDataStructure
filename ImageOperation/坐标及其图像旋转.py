#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-30 18:32
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 坐标及其图像旋转.py
@Description: ==================================
    文本框及其图像的旋转(批量)
@license: (C) Copyright 2013-2019.
************************************************
"""
import os
from math import fabs, sin, radians, cos

import numpy as np
import cv2


####input:  1.img type:numpy_array  2.angle  type:int 3.point type:numpy_array shape(None,8)
# None 表示标注框的个数，8分别是四边形标注框，四个顶点的(x,y)坐标
####output: 1.img 2.point 旋转后变化后的点坐标  shape（None，8） 8个坐标，顺序左上，右上，右下，左下

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


def rotation_point(img_path, angle=15, point_path=None, keep_size=False):
    """
    文本框的旋转
    :param img_path:
    :param angle:
    :param point_path:
    :param keep_size: 是否保持尺寸
    :return:
    """
    # Get the absolute path
    img_path = img_dir + "/" + img_path
    point_path = point_dir + "/" + point_path
    if keep_size:
        print(img_path)
        img = cv2.imread(img_path)

        # judge the img whether or not None in order to interrupt
        # if None,we choose skip the picture
        if np.array(img).shape == ():
            return np.array(img), np.array(img)
        cols = img.shape[1]
        rows = img.shape[0]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        img = cv2.warpAffine(img, M, (cols, rows))
        a = M[:, :2]  ##a.shape (2,2)
        b = M[:, 2:]  ###b.shape(2,1)
        b = np.reshape(b, newshape=(1, 2))
        a = np.transpose(a)
        # TypeError: 'float' object cannot be interpreted as an integer
        point = readBox2NdArray(point_path)
        point = np.reshape(point, newshape=(int(len(point) * 4), 2))
        point = np.dot(point, a) + b
        point = np.reshape(point, newshape=(len(point) // 4, 8))

        # for i, box in enumerate(point):
        #     cv2.polylines(img, [box[:8].astype(np.int32).reshape((-1, 1, 2))], True, color=(0, 255, 0), thickness=2)
        # filename = os.path.basename(img_path)
        # cv2.imwrite("./new_data/" + filename, img[:, :, ::-1])
        # print(point)
        return img, point
    else:
        img = cv2.imread(img_path)
        # judge the img whether or not None in order to interrupt
        # if None,we choose skip the picture
        if np.array(img).shape == ():
            return np.array(img), np.array(img)
        cols = img.shape[1]
        rows = img.shape[0]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

        heightNew = int(cols * fabs(sin(radians(angle))) + rows * fabs(cos(radians(angle))))
        widthNew = int(rows * fabs(sin(radians(angle))) + cols * fabs(cos(radians(angle))))
        M[0, 2] += (widthNew - cols) / 2
        M[1, 2] += (heightNew - rows) / 2

        img = cv2.warpAffine(img, M, (widthNew, heightNew))
        a = M[:, :2]  ##a.shape (2,2)
        b = M[:, 2:]  ###b.shape(2,1)
        b = np.reshape(b, newshape=(1, 2))
        a = np.transpose(a)
        point = readBox2NdArray(point_path)
        # print(np.shape(point))
        # exit(1)
        point = np.reshape(point, newshape=(len(point) * 4, 2))
        point = np.dot(point, a) + b
        point = np.reshape(point, newshape=(len(point) // 4, 8))
        # print(point)
        return img, point


def rotation_summarize(img_dir, point_dir, angle, keep_size):
    """
    图像与文本框的旋转的汇总(批量旋转)
    :param img_dir:
    :param point_dir:
    :param angle:
    :param keep_size:
    :return:
    """
    img_dir_l = os.listdir(img_dir)
    print(len(img_dir_l))

    for img_path in img_dir_l:
        img_filename = os.path.basename(img_path)
        img_basename, ext = os.path.splitext(img_filename)

        # search the relative point by the image name
        point_dir_l = os.listdir(point_dir)
        relative_point_path_l = [x for x in point_dir_l if img_basename + ".txt" in x]
        if len(relative_point_path_l) == 1:
            relative_point_path = relative_point_path_l[0]

            # get the rotated img and relative point

            img, point = rotation_point(img_path=img_path, angle=angle, point_path=relative_point_path,
                                        keep_size=keep_size)
            if img.shape == () and point.shape == ():
                continue

            # 追加写入,文件不存在则进行创建(是文件不存在,a+模式不能创建目录)
            if not os.path.exists(save_point_dir):
                os.makedirs(save_point_dir)
            with open(file=save_point_dir + img_basename + "_neg" + ".txt", mode="w") as f:
                # write the rotate bbox in the rotated img and write into the new file
                for i, box in enumerate(point):
                    # write the box
                    # cv2.polylines(img, [box[:8].astype(np.int32).reshape((-1, 1, 2))], True, color=(0, 255, 0),
                    #               thickness=2)

                    # Conver list to String to write into txt

                    # Firstly ,the list element need to be str
                    box_str = [str(x) for x in box[:8]]

                    line_point_str = ",".join(box_str)
                    f.write(line_point_str + "\n")

            # save the image which has been bboxed
            if not os.path.exists(save_image_dir):
                os.makedirs(save_image_dir)

            cv2.imwrite(save_image_dir + img_basename + "_neg" + ext, img)


if __name__ == '__main__':
    FILE_SAVE_ROOT_DIR = "/data/zxp/DATASET/Test/"
    img_dir = "/data/zhh/PSENet-master/data/cn_data/test_images"
    point_dir = "/data/zhh/PSENet-master/data/cn_data/test_gt"
    save_point_dir = FILE_SAVE_ROOT_DIR + "label/"
    save_image_dir = FILE_SAVE_ROOT_DIR + "image/"

    rotation_summarize(img_dir=img_dir, point_dir=point_dir, angle=180, keep_size=True)
