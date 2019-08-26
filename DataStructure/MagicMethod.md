************************************************
@Time    : 2019-08-23 22:19
@Author  : zxp
@Project : AlgorithmAndDataStructure
@File    : MagicMethod.py
@Description: ==================================
    记载各类魔法方法
@license: (C) Copyright 2013-2019.    
************************************************

# 通用
(1)__len__ -->len(任何类型):只要设置好方法
(2)__iter__(self)-->
          for x in self, 
          if x in self,
          list(self)
          while
          iter(self)
          -->三者都会用到iter方法--遍历同类型的实例--这个千万记住
          --> self类型的实例 ,详见10_集合.py
(3)__contains__ --包含 in操作
# 字典
(1)__setitem__(self,key,value)  对应 字典当中的 a[key]=value---赋值
(2)__getitem__(self,key) 对应 字典当中的 a[key],判断key对应的value值是否存?--判断
(3)__delitem__(self,key)   对应 del myDict[2]

# 集合
(1)__or__ --> |
(2)__and__--> &
(3)__sub__--> -
说明:
## and or 与 & |
   (1)a，b是数值变量， 则&， |表示**位运算**， and，or则依据a，b是否非0来决定输出，
   (2)a，b是逻辑变量(也就是True,或者False)


