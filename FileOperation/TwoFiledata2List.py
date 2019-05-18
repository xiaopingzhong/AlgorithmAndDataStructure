#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-05-18 23:36
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : TwoFiledata2List.py
@Description: ==================================
    将摘要及其标签(两个标签)存入到List列表当中,便于数据库读取
@license: (C) Copyright 2013-2019.    
************************************************
"""
from pymongo import MongoClient, collection

def twoFiledata2List(file1Path, file2Path):
    # 将文本中的数据存到List列表当中
    with open(file1Path, 'r') as f1, open(file1Path, 'r') as f2:
        sourceInLine1 = f1.readlines()
        sourceInLine2 = f2.readlines()
        dataset1 = []
        dataset2 = []
        for line in sourceInLine1:
            temp1 = line.strip('\n')
            dataset1.append(temp1)
        for line in sourceInLine2:
            temp1 = line.strip('\n')
            dataset2.append(temp1)
    return dataset1, dataset2


if __name__ == '__main__':
    file1_path = '/Users/ivega/Downloads/摘要/1.txt'
    file2_path = '/Users/ivega/Downloads/摘要/2.txt'
    # 得到对应的数据库
    list1, list2 = twoFiledata2List(file1_path, file2_path)
    # 连接数据库
    conn = MongoClient('127.0.0.1', 27017)
    # 没有则自动创建nlp_chinese数据库和对应的inter集合
    inter_collection = conn.nlp_chinese.inter
    for n in range(len(list1)):
        # 将读取到的了两个列表传入到collection这个集合当中
        collection.insert_one({'input': list1[n], 'target': list2[n]})
    for i in collection.find():
        print(i)