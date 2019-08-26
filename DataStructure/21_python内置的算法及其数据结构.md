# 常见的 内置数据结构及其算法

优先使用python内置的算法,因为更全,更高效—有些是用C语言编写的

| 数据结构/算法 | 语言内置                        | 内置库                                                       |
| ------------- | ------------------------------- | ------------------------------------------------------------ |
| 线性结构      | list(列表)/tuple(元祖)          | array(数组，不常用)/collections.namedtuple                   |
| 链式结构      |                                 | collections.deque(双端队列)                                  |
| 字典结构      | dict(字典)                      | collections.Counter(计数器)/OrderedDict(有序字典)/defaultdict |
| 集合结构      | set(集合)/frozenset(不可变集合) |                                                              |
| 排序算法      | sorted                          |                                                              |
| 二分算法      |                                 | bisect模块                                                   |
| 堆算法        |                                 | heapq模块                                                    |
| 缓存算法      |                                 | functools.lru_cache(Least Recent Used, python3)              |