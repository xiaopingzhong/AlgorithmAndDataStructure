#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-16 11:02
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 19_二叉查找树.py
@Description: ==================================
    二叉查找树
@license: (C) Copyright 2013-2019.    
************************************************
"""
from DataStructure.DefineException import EmptyException

NODE_LIST = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
]


class BinaryTreeNode(object):
    """二叉查找树的节点"""

    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """二叉查找树"""

    def __init__(self, root=BinaryTreeNode()):
        self.root = root

    @classmethod
    def buildFrom(cls, node_list):
        """构建一颗二叉查找树,key作为各个节点的主键"""
        nodes_dict = {}
        # 在类方法中只能使用cls,不是self
        cls._count = 0
        for node_data in node_list:
            # 把节点名称作为key,之后生成一个节点,之后将节点名称作为key,节点作为value,得到nodes_dict
            key = node_data["key"]
            # 节点的key既是主键,也是value的值--都是数值类型--基本数据类型
            # 但是 left和right属性则是BinaryTreeNode类型
            node = BinaryTreeNode(key=key, value=key)
            nodes_dict[key] = node

        for node_data in node_list:
            node_key = node_data["key"]
            node = nodes_dict[node_key]

            if node_data["is_root"]:
                cls.root = node

            node.left = nodes_dict.get(node_data["left"])
            node.right = nodes_dict.get(node_data["right"])
            cls._count += 1
        return cls(cls.root)

    def __len__(self):
        return self._count

    def searchNode(self, start_node, node_key):
        """根据key查找节点---在构建的时候就决定了"""
        if start_node is None:
            return None
        elif start_node.key > node_key:
            return self.searchNode(start_node.left, node_key)
        elif start_node.key < node_key:
            return self.searchNode(start_node.right, node_key)
        else:
            return start_node

    def fetchValue(self, node_key, default=None):
        """要查找节点的值,先根据key找到该节点"""
        node = self.searchNode(self.root, node_key)
        if node is None:
            return default
        return node.value

    def fetchMinNode(self, start_node: BinaryTreeNode):
        """查找最小节点,--最左"""
        if start_node is None:
            return None
        elif start_node.left is None:
            return start_node
        return self.fetchMinNode(start_node.left)

    def fetchMinValue(self, start_node):
        """查找最小节点的值,必然先找到最小节点(基于key)"""
        min_node = self.fetchMinNode(start_node=start_node)
        min_value = min_node.value if min_node else None
        return min_value

    def addNode(self, key, value):
        """添加节点"""
        node = self.searchNode(start_node=self.root, node_key=key)
        if node is not None:
            node.value = value
            return False
        else:
            self.insertNode(start_node=self.root, node_key=key)

    def insertNode(self, start_node, node_key):
        """插入节点,保持二叉树的特性"""
        if start_node is None:
            start_node = BinaryTreeNode(key=node_key, value=node_key)
        elif start_node.key > node_key:
            start_node.left = self.insertNode(start_node=start_node.left, node_key=node_key)
        elif start_node.key < node_key:
            start_node.right = self.insertNode(start_node=start_node.right, node_key=key)
        return start_node

    def removeNode(self, key):
        """删除指定节点"""
        if key in self:
            self._count -= 1
            # 返回删除的节点
            return self.removeKeepState(self.root, key)

    def removeKeepState(self, start_node: BinaryTreeNode, key):
        """保持删除节点之后,二叉树的状态"""
        # 这个是没有找到的情况
        # 为空
        if start_node is None:
            return start_node
        # 逼近递归出口
        elif start_node.key > key:
            # 分解问题
            start_node.left = self.removeKeepState(start_node.left, key)
            return start_node
        elif start_node.key < key:
            start_node.right = self.removeKeepState(start_node.right, key)
            return start_node

        # 找到左子树的情况--也就是递归的出口
        else:
            # 只有一个节点时,左右孩子为0
            if start_node.left is None and start_node.right is None:
                return None
            # 只有一个左/右孩子
            elif start_node.left is None or start_node.right is None:
                if start_node.left is not None:
                    # 供--分解问题对应代码接收
                    return start_node.left
                else:
                    return start_node.right
            else:
                # 如果待删除的节点为根节点,只需要找到其后继结点(右子树的最左的节点)
                successor_node = self.fetchMinNode(start_node.left)
                # 后继结点替换根节点
                start_node.key, start_node.value = successor_node.key, successor_node.value
                # 更新右子树对状态--因为移动了一个节点
                start_node.right = self.removeKeepState(start_node.right, key)
                return start_node

    def __contains__(self, key):
        """对应包含 in ,在in 中点击,即会跳转"""
        return self.searchNode(self.root, key)


def testBstTree():
    binary_search_tree = BinarySearchTree.buildFrom(node_list=NODE_LIST)

    for data_dict in NODE_LIST:
        node_key = data_dict["key"]
        assert binary_search_tree.fetchValue(node_key) == node_key

    assert binary_search_tree._count == len(NODE_LIST)
    binary_search_tree.fetchValue(-1)

    assert binary_search_tree.fetchMinValue(start_node=binary_search_tree.root) == 1

    binary_search_tree.removeNode(1)
    assert binary_search_tree.fetchValue(1) is None

    assert binary_search_tree._count == len(NODE_LIST) - 1

    binary_search_tree.addNode(key=0, value=0)

    assert binary_search_tree.fetchMinValue(binary_search_tree.root) == 0

    binary_search_tree.removeNode(29)

    assert binary_search_tree.fetchValue(29) is None
