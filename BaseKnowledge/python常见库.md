# 常见库
## os模块/操作系统接口
　　**I/O模块当中也有open**,在python3当中将io.open成为内置函数(open),python2当中,os.open与io.open就开始不一样
　　open函数/io.open函数:读取文件到内容,会返回一个文件对象
　　os.open则是返回的 是,**打开文件的方式标记**
[python os.open()和open()](https://www.cnblogs.com/enochmeng/p/9990505.html)

```
f = os.open("test2.py", os.O_NONBLOCK)
#os.O_NONBLOCK下标为3,以os.O_NONBLOCK方式打开
print f  # 结果为3
```
　　open()返回为文件对象--有read(),write方法
```
f = open("test.log", "wb")
print f # 结果为<open file 'test.log', mode 'wb' at 0x0000000002835030>
```
　　因此文件打开常用open().或者io.open,因此`"import os"` 风格而非`from os import *`。这样可以保证随操作系统不同而有所变化的 os.open() 不会覆盖内置函数 open()。

## 文件通配符
　　glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
```
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```
## Sys.argv
　　Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，关键就是要明白这参数是**从程序外部输入的**(用户输入的参数)，而非代码本身的什么地方，要想看到它的效果就应该将程序保存了，从外部来运行程序并给出参数.因为接收的是外部输入的参数(不一定是代码本身所需要的参数)。因此就会有一连串的参数,其中第一个参数为程序所在的绝对地址
　　sys模块在系统程序与变量交互的时候用的比较多---例如用户输入的参数
　　[Python中 sys.argv的用法简明解释](http://www.cnblogs.com/aland-1415/p/6613449.html)
## 定向终止
　　大多脚本的定向终止都使用 "sys.exit()"。
## 数学
(1)math模块为浮点运算提供了对底层C函数库的访问:
```
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```
(2)random模块:提供了生成随机数的工具。
```
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
```
## 日期时间
　　支持日期和时间算法的同时，实现的重点放在更**有效的处理和格式化输出**,有两种时间类型:**date,datetime类型**
```
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
>>> # dates support calendar arithmetic(重点)
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```
常用时间处理方法
```
今天 today = datetime.date.today()
昨天 yesterday = today - datetime.timedelta(days=1)
上个月 last_month = today.month - 1 if today.month - 1 else 12
当前时间戳 time_stamp = time.time()
时间戳转datetime datetime.datetime.fromtimestamp(time_stamp)
datetime转时间戳 int(time.mktime(today.timetuple()))
datetime转字符串 today_str = today.strftime("%Y-%m-%d")
字符串转datetime today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
补时差 today + datetime.timedelta(hours=8)
```
## 性能度量 --timeit模块
　　不同方法的运行时间 --timeit模块
　　Timer(函数名, 参数(字符串的格式,分号,不同参数)).timeit()
```
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```
## 区间判断
　　数值/日期在区间的判断:--[python-intervals](https://github.com/AlexandreDecan/python-intervals)
`pip install python-intervals`
## 三元运算符
　　a=条件为真时的执行语句 if 条件 else 条件不成立时的执行语句
例子:当条件判断成立时，变量赋值为 .3(float函数)，不成立时，变量赋值为 .5 (float函数)
```
a = .3 if predicate else .5
```
## 一行两个for 循环 一个if
　　嵌套的for...[if]...语句可以**从多个List中选择满足if条件的元素组成新的List或者{},()**---**因此就没有else语句(这个要特别注意)--因为符合条件的才会有机会组成新的数据**--关键是组成新的list
　　`[(x, y) for  x in  a for  y in  b if(x%2==0)and(y<'x')]`其中最外面的[],是返回类型,(x,y)是里面的元素,其元素类型为tuple类型,总之元素类型要符合返回类型所能接受的值就可以.
一个具体的例子如下:
```
>>> a=[1,2]
>>> b=[2,4]
>>> [[x,y] for x in a for y in b if(x+1)==y]
[[1, 2]]
>>> [(x,y) for x in a for y in b if(x+1)==y]
[(1, 2)]
>>> {x:y for x in a for y in b if(x+1)==y}
{1: 2}
>>> {str(x):y for x in a for y in b if(x+1)==y}
{'1': 2}
>>> {str(x):str(y) for x in a for y in b if(x+1)==y}
{'1': '2'}
>>> {str(x):str(y) for x in a for y in b}
{'1': '4', '2': '4'}
```
## 在交互式环境实现多句一行
用`;`进行隔开就可以
## 比较日期大小
[Python 判断日期大小( 判断开始时间是否早于结束时间)](https://www.cnblogs.com/pylemon/archive/2012/01/06/2315363.html)
直接用datetime对象进行比较
## lower_pattern.extend是没有返回值
sum_pattern = lower_pattern.extend([currency_pattenrn, upper_pattern])
## dict的key问题
```
>>> {2:"f",2:"e","d":"d","d":"e"}
{2: 'e', 'd': 'e'}
>>> {(2,3):"d"}
{(2, 3): 'd'}
```
相同的key,后面会覆盖前面的;
元组,字符串,数字都是可以直接作为key,因为这些类型都具备这个条件-**-不可修改**.
## 太多的 if 语句
但是太多的 if 语句使得代码不易扩展，而且代码可读性也要大打折扣。
## 1-100之和
```
>>> sum(range(101))
5050
```