#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019/5/6 3:50 PM
@Author  : zxp
@Project : ContractVerification
@File    : DiffTimeFormat2DateTimeFormat.py
@Description: ==================================
    单个不同格式的日期归一化
@license: (C) Copyright 2013-2019.
************************************************
"""
import datetime
import re
import intervals as In


def DiffTimeFormat2DateTimeFormat(time_str):
    """
    将字符串格式(年月日.---,///)的日期转换成datetime格式的日期,便于比较
    :param time_str:
    :return:
    """
    time_l = re.findall(r"\d+", time_str)
    # time_l=['2019','09','06']
    if time_l:
        # print("打印字符长度:")
        # print(len("".join(time_l)))
        # 日期检查及其格式化
        if (len(time_l) == 3):
            try:
                time_datetime = datetime.datetime.strptime("{}-{}-{}".format(time_l[0], time_l[1], time_l[2]),
                                                           "%Y-%m-%d")
            except Exception as e:
                # print(e)
                input_date_str = input("输入格式错误,重新输入正确的日期格式:")
                abstract_date_l = re.findall("\d+", input_date_str)
                # 这个递归函数,执行期间,如果正常执行,还是会走try...else语句,这个注意
                # try语句还是执行不正常的话,会一直执行try...except语句,直至正常执行走try...else语句
                # 因此保险起见,即使在else语句有返回值,也添加return
                return DiffTimeFormat2DateTimeFormat(abstract_date_l)
            else:
                print("打印try语句当中的time_datetime:")
                print(time_datetime)
                return time_datetime
        elif (len(time_l) == 2):
            if (len("".join(time_l)) in In.closed(5, 6)):
                try:
                    time_datetime = datetime.datetime.strptime("{}-{}".format(time_l[0], time_l[1]), "%Y-%m")
                except Exception as e:
                    # print(e)
                    input_date_str = input("输入格式错误,重新输入正确的日期格式:")
                    abstract_date_l = re.findall("\d+", input_date_str)
                    return DiffTimeFormat2DateTimeFormat(abstract_date_l)
                else:
                    return time_datetime
            elif (len("".join(time_l)) in In.closed(2, 4)):
                try:
                    time_datetime = datetime.datetime.strptime("{}".format(time_l[0]), "%Y")
                except Exception as e:
                    # print(e)
                    input_date_str = input("输入格式错误,重新输入正确的日期格式:")
                    abstract_date_l = re.findall("\d+", input_date_str)
                    return DiffTimeFormat2DateTimeFormat(abstract_date_l)
                else:
                    return time_datetime
        return None
