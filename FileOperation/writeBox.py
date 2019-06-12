#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-13 01:09
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : writeBox.py
@Description: ==================================
    画框文件--坐标为:顺时针的四个点
@license: (C) Copyright 2013-2019.    
************************************************
"""

from PIL import Image,ImageDraw
import os

def writebox(image_path,gt_path):
    image = Image.open(image_path)
    #创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(image)

    #draw.polygon([(902,1217),(1288,1215),(1288,1269),(903,1271)], outline=(255,0,0))
    #坐标参数依次是左上角、右上角、右下角、左下角，outline里面是RGB参数：红、绿、蓝
    boxes=[]
    with open(gt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            box=line.split(",")[:8]
            boxes.append(box)
    for box in boxes:
        box=[float(x) for x in box]
        draw.polygon([(box[0],box[1]),(box[2],box[3]),(box[4],box[5]),(box[6],box[7])],outline=(0,255,0))
    # image.show()
    # 保存图片
    os.chdir("/data/zxp/tf_ctpn/data/res/")
    """
    保存参考:https://blog.csdn.net/weixin_41935140/article/details/83308359
    """
    image.save("gt2.jpg",quality=100)



if __name__ == '__main__':
    image_path = '/data/zxp/tf_ctpn/data/demo/gt_10001.jpg'
    gt_path='/data/zxp/tf_ctpn/OCREval/gt_10001.txt'
    writebox(image_path,gt_path)