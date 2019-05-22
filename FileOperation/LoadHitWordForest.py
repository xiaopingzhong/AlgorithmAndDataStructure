#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019/5/6 5:06 PM
@Author  : zxp
@Project : ContractVerification
@File    : LoadHitWordForest.py
@Description: ==================================
    扫描同义词词林,构建归一化的近义词词典
@license: (C) Copyright 2013-2019.    
************************************************
"""

import os

synonym_word_dict = {}


def loadHitWordForest(word_forest_path):
    """
    加载同义词词林,将所有的近义词映射到该组的第一个单词当中
    :param word_forest_path:
    :return:
    """
    assert os.path.isfile(word_forest_path)
    with open(word_forest_path, encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip().split()
            assert len(line[0]) == 8
            # [-1]表示的是第一个元素的倒数第一个字符
            if line[0][-1] == '=' and len(line) > 2:
                synonym_word_dict.update({word: line[1] for word in line[1:]})
    return synonym_word_dict

if __name__ == '__main__':
    word_forest_path="../Resource/cilin_ex.txt"
    synonym_word_dict=loadHitWordForest(word_forest_path)
