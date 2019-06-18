#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-18 12:41
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : twoNumberSum.py
@Description: ==================================
    two number sum
@license: (C) Copyright 2013-2019.    
************************************************
"""
class Solution:
    def twoSum(self, nums, target):
        nums_1=nums[:-1]
        nums_2=nums[1:]
        match_number=0
        for x in range(len(nums_1)):
            match_number += 1
            for y in range(len(nums_2)):
                if nums_1[x]+nums_2[y]==target:

                    return [x,y+match_number]
                else:
                    continue

if __name__ == '__main__':
    soul=Solution()
    result=soul.twoSum([2,5,5,11],10)
    print(result)