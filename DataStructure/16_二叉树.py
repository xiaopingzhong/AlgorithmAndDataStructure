#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-10 11:02
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 16_二叉树.py
@Description: ==================================

@license: (C) Copyright 2013-2019.    
************************************************
"""

from collections import deque


class Queue(object):
    """作为堆栈的基础"""

    def __init__(self):
        self._items = deque()

    # 增
    def append(self, value):
        return self._items.append(value)

    # 删
    def pop(self):
        return self._items.popleft()

    def empty(self):
        return len(self._items) == 0


class Stack(object):
    """便于二叉树节点遍历"""
    # 初始化栈
    def __init__(self):
        self._items = deque()

    # 进栈
    def push(self, value):
        return self._items.append(value)

    # 出栈
    def pop(self):
        return self._items.pop()

    # 判断栈是否为空
    def empty(self):
        return len(self._items) == 0\

class BinaryNode():
    def __init__(self,data=None,left=None,right=None,isroot=None):
        self.data=data
        self.left=left
        self.right=right
        self.isroot=isroot

class BinaryTree(object):
    def __init__(self,root=BinaryNode()):
        self.root=root

    @classmethod
    def buildFrom(cls,node_list):     # 因为构建一颗二叉树之后,需要返回BinaryTree实例
        node_dict={}
        for one_node_data in node_list:
            node_name=one_node_data["data"]
            node_dict[node_name]=BinaryNode(data=node_name)

        for one_node_data in node_list:
            node_name=one_node_data["data"]
            node=node_dict[node_name]
            if one_node_data["is_root"]:
                cls.root=node
            node.left=node_dict.get(one_node_data["left"])
            node.right=node_dict.get(one_node_data["right"])
        # 返回BinaryTree实例,也就是一个二叉树对象
        return cls(cls.root)

    # preorder,inorder,postorder 都可以使用栈进行遍历,但是使用递归的方法更省时
    def preorederTravel(self,binary_tree:BinaryNode):
        """前序遍历
         类似对链表进行递归遍历,也从根节点开始
        :param binary_tree:一般是最大二叉树的根节点,
                因为其能代表的是最大二叉树--从根节点通过遍历能得到整科二叉树
        :return:
        """
        if binary_tree is not None:
            print(binary_tree.data)
            self.preorederTravel(binary_tree.left)
            self.preorederTravel(binary_tree.right)

    def inorederTravel(self,binary_tree:BinaryNode):
        """中序遍历"""
        if binary_tree is not None:
            self.inorederTravel(binary_tree.left)
            print(binary_tree.data)
            self.inorederTravel(binary_tree.right)

    def postorderTravel(self,binary_tree:BinaryNode):
        """后序遍历"""
        if binary_tree is not None:
            self.postorderTravel(binary_tree.left)
            self.postorderTravel(binary_tree.right)
            print(binary_tree.data)

    def layerTravelTraditional(self,binary_tree:BinaryNode):
        """传统方式层次遍历-->分别保存当前层和下一层(左右子节点)的节点,之后向下层遍历"""
        if binary_tree is not None:
            current_layer_node_l=[]
            next_layer_node_l=[]
            # 说明肯定有根节点
            current_layer_node_l.append(binary_tree)
            while current_layer_node_l or next_layer_node_l:
                for current_node in current_layer_node_l:
                    print(current_node)
                    if current_node.left:
                        # 是current_node的left节点,不是binary_tree
                        next_layer_node_l.append(current_node.left)
                    if current_node.right:
                        next_layer_node_l.append(current_node.right)
                current_layer_node_l=next_layer_node_l
                next_layer_node_l=[]

    def layerTravelWithQueue(self,binary_tree:BinaryNode):
        """通过当前层的节点存储,推出的过程,同时也将对应的叶子节点存入队列当中,自己画示意图就可以推理"""
        if binary_tree is not None:
            queue=Queue()
            queue.append(binary_tree)
            # 不断推出当前层的节点
            while not queue.empty():
                current_node=queue.pop()
                print(current_node.data)
                if current_node.left:
                    # 注意:是当前节点的left,不是binary_tree
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

    def reverseBinaryTree(self,binary_tree:BinaryNode):
        """二叉树反转"""
        if binary_tree is not None:
            binary_tree.left,binary_tree.right=binary_tree.right,binary_tree.left
            self.reverseBinaryTree(binary_tree.left)
            self.reverseBinaryTree(binary_tree.right)






def testBinaryTree():
    node_list = [
        {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
        {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
        {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
        {'data': 'H', 'left': None, 'right': None, 'is_root': False},
        {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
        {'data': 'F', 'left': None, 'right': None, 'is_root': False},
        {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
        {'data': 'I', 'left': None, 'right': None, 'is_root': False},
        {'data': 'J', 'left': None, 'right': None, 'is_root': False},
    ]
    binary_tree=BinaryTree.buildFrom(node_list)
    # 类似对链表进行递归遍历,也从根节点开始
    binary_tree.preorederTravel(binary_tree.root)
    binary_tree.inorederTravel(binary_tree.root)
    binary_tree.postorderTravel(binary_tree.root)
    binary_tree.reverseBinaryTree(binary_tree.root)
    binary_tree.layerTravelTraditional(binary_tree.root)
    binary_tree.layerTravelWithQueue(binary_tree.root)
    # assert 0


