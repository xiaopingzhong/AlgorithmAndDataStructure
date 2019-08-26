#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-08-20 12:12
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 20_图.py
@Description: ==================================
    图的遍历: 深度遍历与广度遍历
@license: (C) Copyright 2013-2019.    
************************************************
"""

from collections import deque

# 邻接表的构建
GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def __len__(self):
        return len(self._deque)


class GraphTravel(object):
    BFS_Traveled_s = set()
    DFS_Traveled_s = set()
    DFS_stack_Traveled_s = set()

    def breadFirstSearch(self, graph_dict, start_node):
        """使用队列,出队一个节点之后,递归与其相岭的节点"""
        node_q = Queue()
        node_q.push(start_node)
        while node_q:
            current_node = node_q.pop()
            print(current_node)
            if current_node not in self.BFS_Traveled_s:
                self.BFS_Traveled_s.add(current_node)
                for adjacent_node in graph_dict[current_node]:
                    if adjacent_node not in self.BFS_Traveled_s:
                        node_q.push(adjacent_node)

    def deepFirstSearch(self, graph_dict, start_node):
        # 构建递归出口
        if start_node not in self.DFS_Traveled_s:
            print(start_node)
            self.DFS_Traveled_s.add(start_node)

        # 逼近递归出口
        for adjacent_node in graph_dict[start_node]:
            if adjacent_node not in self.DFS_Traveled_s:
                # 分解问题
                self.deepFirstSearch(graph_dict, adjacent_node)

    def dfsUseStack(self, graph_dict, start_node):
        stack = Stack()
        stack.push(start_node)
        # 有时候将数据存入到某种数据结构中进行递归,直至该种数据结构为空
        while stack:
            current_node = stack.pop()
            if current_node not in self.DFS_stack_Traveled_s:
                print(current_node)
                # Warning:打印(遍历)之后记得添加到标记列表当中
                self.DFS_stack_Traveled_s.add(current_node)
            #  reversed与stack进出栈顺序的特性
            for adjacent_node in reversed(graph_dict[current_node]):
                if adjacent_node not in self.DFS_stack_Traveled_s:
                    stack.push(adjacent_node)


def testGraphTravel():
    graph_travel = GraphTravel()
    graph_travel.breadFirstSearch(GRAPH, "A")
    graph_travel.deepFirstSearch(GRAPH, "A")
    graph_travel.dfsUseStack(GRAPH, "A")
