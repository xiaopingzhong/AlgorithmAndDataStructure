#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019/5/6 5:35 PM
@Author  : zxp
@Project : ContractVerification
@File    : CutQueryReserveSplitCharacter.py
@Description: ==================================
    保留分割符的分割方式
@license: (C) Copyright 2013-2019.    
************************************************
"""


def cutQuery(query):
    # query ='从两小两大风险点梳理分众传媒资源扩张计划'
    cut_flag = ['!', '?', '。', '！', '？', '；', ';', '\n']
    length = len(query)
    start = 0
    end = 0
    r_l = []
    for i in range(length):
        if query[i] in cut_flag:
            r_l.append(query[start:i + 1])
            end = i + 1
            start = i + 1
    # 疑问？
    if end != length:
        query_f = query[end:]
        r_l.append(query_f)
    return r_l
