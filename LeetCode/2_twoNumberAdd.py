#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-06-19 21:13
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 2_twoNumberAdd.py
@Description: ==================================

@license: (C) Copyright 2013-2019.
************************************************
"""

# *********+++++++++++*********两数相加*********+++++++++++*********========
#   输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
#   输出：7 -> 0 -> 8
#   原因：342 + 465 = 807
#   注意进位
# *********+++++++++++*********========*********+++++++++++*********========

# *********+++++++++++*********两数相加*********+++++++++++*********========
#   关键点:加和进位
#   实现方式:链表元素变为整数(通过整数),之后逆向存储在链表当中
#   适用场景:两数相加的情况
# *********+++++++++++*********========*********+++++++++++*********========


# Definition for singly-linked list.
class ListNode:
    """
    链表形式,val和next属性(这个可以屏蔽,因为leetcode后台有实现,我们只需返回链表即可)
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def listNode2Int(LNode: ListNode) -> int:
    """
    将链表各个元素转换为整数
    :param LNode:
    :return:
    """
    LNode_str_l = []
    while LNode:
        LNode_str_l.append(str(LNode.val))
        LNode = LNode.next
    # ["2","4","3"]-->342
    l1_reverse = [x for x in LNode_str_l[::-1]]
    l1_int = int("".join(l1_reverse))
    return l1_int


class Solution:
    def addTwoNumbers(self, L1: ListNode, L2: ListNode) -> ListNode:
        if L1 and L2:
            # two number add
            L1_int = listNode2Int(L1)
            L2_int = listNode2Int(L2)
            result_int = L1_int + L2_int

            # reverse Memory
            # use the variable L4 to keep the ListNode head pointer
            L3 = L4 = ListNode(0)
            for x in str(result_int)[::-1]:
                L3.next = ListNode(int(x))
                L3 = L3.next
            # next说明过了头指针,返回的是ListNode类型
            return L4.next

        else:
            print("at least One ListNode is None")


if __name__ == '__main__':
    # ListNode original instance
    LNa1 = ListNode(3)
    LNa2 = ListNode(4)
    LNa3 = ListNode(2)
    # construct link
    LNa3.next = LNa2
    LNa2.next = LNa1

    LNb1 = ListNode(4)
    LNb2 = ListNode(6)
    LNb3 = ListNode(5)
    LNb3.next = LNb2
    LNb2.next = LNb1
    solution = Solution()
    add_data = solution.addTwoNumbers(LNa3, LNb3)
    # last print:  <__main__.ListNode object at 0x10733b9b0>
    print(add_data)
