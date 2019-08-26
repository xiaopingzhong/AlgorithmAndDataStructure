#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
************************************************
@Time    : 2019-07-31 09:59
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : 8_哈希表.py
@Description: ==================================
    哈希表--构建过程
@license: (C) Copyright 2013-2019.
************************************************
"""


# *********+++++++++++*********========*********+++++++++++*********========
#   学习知识:
#       调用__iter__的状态情况:list(list接收yield),for..in.. 对某个数据类型进行遍历的时候
#       length与size:尽量少使用length和size,因为两个意思相近,因此为了方便,根据名称设置大小及其容量
#       长度的获取:尽可能以属性的方式获取长度,更直观,简洁,必要时再写上__len__
#       在定义的函数或者类中,尽量不要出现直接的数值,可以使用全局变量或者类属性进行进行代替,减少后期重构成本
#       or 与if x in 出现的情况 等价
#       一般删除/出队的情况,都会返回删除的值,验证是否删除正确
#       基本元素的操作入口的形成:将Slot(key, value)插入到指定槽位,在这里我们就可以知道,该哈希表的基本元素类型是Slot类型--这点很重要
# *********+++++++++++*********========*********+++++++++++*********========


class Array(object):
    """
    实现 数据的 索引查找,根据索引设置值,清空,遍历,长度测量
    """

    def __init__(self, size=32, initial=None):
        """设置初始容量"""
        self.size = size
        self._items = [initial] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        # 值的修改没有返回值
        self._items[index] = value

    def __iter__(self):
        for item in self._items:
            yield item

    def __len__(self):
        # 其实返回的是数组的长度--用self.size也可以
        return len(self._items)

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value


# *********+++++++++++*********========*********+++++++++++*********========
#   开始部分,将哈希表的类型取作为数组
# *********+++++++++++*********========*********+++++++++++*********========


class Slot():
    # 设置哈希表当中槽位的状态
    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable():
    # 尚未使用的状态
    UNUSED = None
    # 删除元素之后的槽位状态
    EMPTY = Slot(None, None)
    # 哈希冲突探查的偏移量
    STEP = 5

    # 尽量少使用length和size,两个意思相近,因此为了方便,根据名称设置大小及其容量
    def __init__(self, capacity, initial=None, real_size=0):
        """
        初始化的时候,(哈希表的容量,槽位的初始状态,实际元素个数)
        :param capacity: 哈希表的容量
        :param initial: 槽位的初始状态
        :param real_size: 实际元素个数
        """
        self._item_with_array = Array(size=capacity, initial=initial)
        self.real_size = real_size
        self.capacity = capacity

    def __len__(self):
        return self.real_size

    # *********+++++++++++*********========*********+++++++++++*********========
    #   __hash__与__eq__,hash()
    #       __hash__方法返回一个整数(可以通过hash生成一个唯一的标识id)，用来表示该对象的唯一标识，配合__eq__方法判断两个对象是否相等(==)：
    # *********+++++++++++*********========*********+++++++++++*********========

    def _hash(self, key):
        """_hash()找到key在哈希表当中的逻辑下标(绝对值)
        hash()这个方法主要是针对新建的key-value
        hash方法的功能是根据Key来定位这个K-V在链表数组中的位置的。
        也就是hash方法的输入应该是个Object类型的Key，输出应该是个int类型的数组下标
        :param key:
        :return:
        """
        return abs(hash(key)) % self.capacity

    def findKeyIndex(self, key):
        """
        找到key在哈希表当中的真实下标
        :param key:
        :return:
        """
        # 得到逻辑下标
        index = self._hash(key)
        hashtable_capacity = self.capacity

        # 在哈希表当中的槽位不为HashTable.UNUSED的情况下进行查找
        while self._item_with_array[index] is not HashTable.UNUSED:

            # 槽位已经使用过,但是值已经删除,因此HashTable.EMPTY--曾经使用的槽位状态
            if self._item_with_array[index] is HashTable.EMPTY:
                index = (index * self.STEP + 1) % hashtable_capacity
                continue

            # 槽位有值的情况下,比较key,因为self._item_with_array[index]为Slot类型
            # 后面有说明,因为Hashtable在一开始插入的值为Slot,因此后期对哈希表的处理,主要是对Slot实例处理
            elif self._item_with_array[index].key == key:
                return index
            else:

                # 把常数项提取为类属性:STEP
                index = (index * self.STEP + 1) % hashtable_capacity
        # 没有找到key对应的真实下标
        return None

    def findInsertLocation(self, key):
        """为key,在哈希表当中找到合适的插入位置"""

        # 得到key的逻辑下标
        index = self._hash(key)

        # 跳过正在使用的槽位
        while self._item_with_array[index] not in (HashTable.UNUSED, HashTable.EMPTY):
            index = (index * 5 + 1) % self.capacity
        return index

    @property
    def load_factor(self):
        """静态属性方法"""
        return abs(self.real_size) / self.capacity

    def add(self, key, value):
        """为哈希表增加元素"""

        # 判断key是否存在,存在则更新对应的value值,否则直接插入
        find_index = self.findKeyIndex(key)

        # key不存在,直接插入
        if find_index is None:
            # 为key寻找合适的槽位--index
            index = self.findInsertLocation(key)

            # 重点
            # 将Slot(key, value)插入到指定槽位,在这里我们就可以知道,该哈希表的基本元素类型是Slot类型--这点很重要
            self._item_with_array[index] = Slot(key, value)
            # 实际元素个数加一
            self.real_size += 1

            # 装载因子大于0.8,则进行重哈希
            if self.load_factor >= 0.8:
                self.rehashing()

            # 插入成功
            return True
        else:
            # key存在,只需要对值进行更新
            index = self.findKeyIndex(key)
            # 因为之前一开始插入的时候就是Slot,因此self._item_with_array[index]是Slot类型
            # 因此有value和key属性
            self._item_with_array[index].value = value

            # 只对值进行更新,没有增加函数
            return False

    def rehashing(self):
        """重哈希,主要是构建新的哈希表,同时将旧哈希表当中的数据迁移到新哈希表当中,实现哈希表的扩容"""

        # 先保存旧哈希表
        old_hashtable = self._item_with_array

        # 得到新哈希表的容量:在这里是两倍
        new_capacity = self.capacity * 2
        # with HashTable(newsize, initial=HashTable.UNUSED) as ht:
        #     self._item_with_array=ht._item_with_array

        # 构建新的hashtable同时初始化了哈希表的基本载体--new_hashtable._item_with_array
        new_hashtable = HashTable(new_capacity, initial=HashTable.UNUSED)

        # 更新哈希表--用新的哈希表取代旧的哈希表
        self._item_with_array = new_hashtable._item_with_array

        # 更新哈希表的容量
        self.capacity = new_hashtable.capacity

        # 更新哈希表的元素
        self.real_size = new_hashtable.real_size

        # 对旧哈希表进行遍历,取出非空槽位上对应的数据
        for slot in old_hashtable:

            # or 可以使用if x in 列表(所有情况)
            if slot in (HashTable.EMPTY, HashTable.UNUSED):
                # if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                continue
            else:
                # 根据key找到合适的位置/槽位插入
                index = self.findInsertLocation(slot.key)
                # 根据位置进行插入
                self._item_with_array[index] = slot
                # 实际元素的个数加一
                self.real_size += 1

    def get(self, key):
        """根据key获取哈希表的元素"""

        # 首先判断在哈希表当中是否存在key,不存在返回为None
        index = self.findKeyIndex(key)

        # key存在在哈希表当中
        if index:

            # 取出对应的value并返回
            value = self._item_with_array[index].value
            return value
        # 不存在则直接返回False
        return False

    def remove(self, key):
        """根据key移除哈希表当中的元素"""

        # 判断哈希表当中是否存在key,存在则返回对应下标,--因为哈希表会自动扩容,因此一个位置对应一个实例,不用担心会取出多个Slot
        index = self.findKeyIndex(key)

        # 不存在
        if index is None:
            # 错误是由语法不正确产生的；异常是没有语法错误的情况下，执行期间产生的
            raise KeyError()

        # 置空之前,取出待删除的值
        remove_value = self._item_with_array[index].value

        # 置空
        self._item_with_array[index] = HashTable.EMPTY
        self.real_size -= 1

        # 一般删除的情况,都会返回删除的值,验证是否删除正确
        return remove_value

    def __iter__(self):
        # 遍历Hashtabel实例
        for slot in self._item_with_array:  # 会调用数组的__iter__
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key


def test_hash_table():
    """测试"""
    h = HashTable(8, initial=HashTable.UNUSED, real_size=0)

    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)

    assert len(h) == 3
    assert h.get('a') == 0
    assert h.get('b') == 1
    assert h.get('hehe') is False

    h.remove('a')

    assert h.get('a') is False

    # 对哈希表当中的key进行排序---也就是对hash表进行遍历
    assert sorted(list(h)) == ['b', 'c']

    # n=50
    for i in range(100000):
        h.add(i, i)

    for i in range(100000):
        assert h.get(i) == i

    # assert 0
