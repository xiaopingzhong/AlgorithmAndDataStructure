#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-18 12:41
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 1_两数之和.py
@Description: ==================================
    two number sum
@license: (C) Copyright 2013-2019.    
************************************************
"""

# *********+++++++++++*********目标数与对应两数之和的下标*********+++++++++++*********========
#   构建Hash字典,目标值-当前遍历的值=查找值,不存在的先放到hash字典,存在则返回对应下标.
# *********+++++++++++*********========*********+++++++++++*********========

# *********+++++++++++*********目标数与对应两数之和的下标*********+++++++++++*********========
#   关键点: 构建 两个加数与目标数之间的联系,首先确定一个加数,将其放到确定的数据结构当中(可以是列表或者字典)
#   适用场景: 将目标数拆分成以某个列表元素的表现形式
# *********+++++++++++*********========*********+++++++++++*********========



class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Notice: need to add self,Don't forget
        :param nums:
        :param target:
        :return:
        """



        result_dict = {}
        for i, k in enumerate(nums):
            if result_dict.get(target - k) is not None:
                return i, result_dict.get(target - k)
            else:
                result_dict[k] = i


if __name__ == '__main__':
    result = soul.two_sum(nums=[2, 5, 6, 3], target=8)
    print(result)
