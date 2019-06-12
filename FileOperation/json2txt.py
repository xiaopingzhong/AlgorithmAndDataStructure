#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-05-18 23:27
@Author  : zxp
@Project : OCR-ctpn
@File    : cv.py
@Description: ==================================
    数据集格式转换--将单个json转换为众多txt
@license: (C) Copyright 2013-2019.
************************************************
"""
import json
import os


def dataSetFormatTransfer(json_path):
    with open(json_path, 'r') as f:
        data_dict: dict = json.load(f)
    for x in data_dict.keys():
        file_path = os.getcwd()+"/data/dataset/train_gt/" + "{}".format(x) + ".txt"
        with open(file_path, "w") as file:
            for y in data_dict[x]:
                for z in y.keys():
                    if z == "points":
                        # 展平二维数组
                        axis_l = [q for p in y[z] for q in p]
                        one_place_str = "{},{},{},{},{},{},{},{}\n".format(axis_l[6], axis_l[7], axis_l[4], axis_l[5],
                                                                           axis_l[2], axis_l[3], axis_l[0], axis_l[1])
                        # 换行输出
                        file.write(one_place_str)

                    else:
                        continue
        # exit(1)


if __name__ == '__main__':
    dataSetFormatTransfer(os.getcwd()+"/data/dataset/train_full_labels.json")
