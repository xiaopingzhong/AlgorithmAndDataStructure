# 基本概念
## 称之为胶水语言的原因
　　它常被昵称为胶水语言，能够把**用其他语言制作的各种模块(尤其是C/C++)很轻松地联结在一起**。常见的一种应用情形是，使用Python快速生成程序的原型(有时甚至是程序的最终界面)，然后对其中有**特别要求的部分，用更合适的语言改写**，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C/C++重写。
## 注释模块--单行注释与多行注释
以下实例我们可以输出函数的注释：
```
def a():
    '''这是文档字符串'''
    pass
print(a.__doc__)
```
## python解释器
Python 解释器可不止一种哦，有 CPython、IPython、Jython、PyPy
1. CPython 就是用 C 语言开发的了，是官方标准实现,>>>
2. IPython 是在 CPython 的基础之上在交互式方面得到增强的解释器ln
3. Jython 是专为 Java 平台设计的 Python 解释
4. PyPy 是 Python 语言（2.7.13和3.5.3）的一种快速、兼容的替代实现--速度快
## #!/usr/bin/python3与 #!/usr/bin/env python3
　` linux 或 unix 系统`:一个将python写死,一个将从配置文件中找到,类似'python=';
分成两种情况：
（1）如果调用python脚本时，使用:
```
python script.py 
#!/usr/bin/python 被忽略，等同于注释。
```
（2）如果调用python脚本时，使用:
```
./script.py 
#!/usr/bin/python 指定解释器的路径。
```
　　在Linux/Unix系统中，**你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行**：`#! /usr/bin/env python3`
　　然后**修改脚本权限，使其有执行权限**，命令如下：`$ chmod +x hello.py`
　　执行以下命令：`./hello.py`
　　输出结果为：`Hello, Python!`
## 实现多行语句:
语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
```
total = item_one + \
        item_two + \
        item_three
```
**在 [], {}, 或 () 中的多行语句**，不需要使用反斜杠(\)，例如：
```
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```
## 同一行实现多条语句
语句用`;`分割即可--便于在交互式命令行执行
`import sys; x = 'runoob'; sys.stdout.write(x + '\n')`
## import 与 from...import
```
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
```
具体使用方法为:** 以 time 模块为例  **：
1、将整个模块导入，例如：import time，在引用时格式为：time.sleep(1)。
2、将整个模块中**全部函数**导入，例如：from time import*，在引用时格式为：sleep(1)。
3、将模块中**特定函数**导入，例如：from time import sleep，在引用时格式为：sleep(1)。
4、将模块换个别名，例如：import time as abc，在引用时格式为：abc.sleep(1)
PS:导入到那个层次,就使用哪个层次
## help() 函数
在交互式命令行当中--help(max)-->之后按下 : q 两个按键即退出说明文档
## python中的首行注释
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
第一行:告诉linux/macos系统,这个可以用该系统下的python3运行;
第二行:告诉系统该文件是以utf-8的编码来读取的,但并不代表该文件本身就是utf-8,因此最保险使得文件格式为:`UTF-8 without BOM`,或者会有空格
# 回车与换行
## 原因及其本质
(1)原因:**电传打字机的延迟问题**和当时**计算机内存不足**造成的原因.
(2)本质:光标移动到本行行首与换行**相互独立**的问题

|                            | 回车                                                       | 换行                                                 |
| -------------------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| 含义                       | 光标移动到本行行首,但是没有换行                            | 单单进行换行,此时当前行为下一行                      |
| 字符位                     | 用hex viewer查看,对应 ASCII 码的16进制是 0x0d，10进制是 13 | 用hex viewer查看文件,对应16进制是 0x0a， 10进制是 10 |
| ascii码                    | \r                                                         | \n                                                   |
| 控制字符<br />(功能的标识) | Carriage(车轮) Return--简写为CR                            | Line Feed--LF                                        |
| 全文名                     | return                                                     | newLine                                              |

在hex viewer查看下的情况:
![](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190430000134.png)
## 不同系统的换行字符
\r\n:先进行光标移动到当前行行首,之后进行换行,当前行改为下一行,因此最后光标的位置会在下一行的行首,这也就是我们在window上常见的Enter键实现的功能.
\n:常见在linux当中,只有换行;
\r:常见在mac系统下,只有回车.
## 结果
1. 因此window下打开mac系统或者linux系统下创建的文件,就会只有一行,因为没有\n--换行符;因为那**两个系统没有完整的'\r\n'**,因此window就不会换行(window把'\r\n'看成一个完整的换行,少哪个都不行).
2. window文件在mac或者linux系统下,每行(每段)都会有^m的字符;
## 硬回车与软回车
shift+enter:软回车,在html代码是<br>标记,将对应的网页内容复制到word中变为**向下的箭头**--分行不分段,因此使得前后两行的**行间距大幅度缩小**
普通enter:在html代码是<p>..</p>标记,将对应的网页内容复制到word中变为**弯曲的箭头**,--起着分段的左右
## 参考文献
[关于“回车”的有趣历史 及 “回车”与“换行”的区别](https://www.cnblogs.com/dawn-l/p/5180373.html)
[终于搞懂了回车与换行的区别](https://blog.csdn.net/fanwenbo/article/details/54848429)
# 标准数据类型
Python3 中有六个标准的数据类型：
```
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
```
Python3 的六个标准数据类型中：
```
#注意不可变的
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
```
　　 type() 函数可以用来查询变量所指的对象类型,也可以用 isinstance 来判断,但是isinstance会认为子类的实例也属于父类类型,type则不会.因此我们可以总结:
  　(1)type() 主要常用来**判断未知数据**的类型,
  　(2)isinstance主要是用来**判断类之间是否是继承关系**
 ```
 >>> class A:
...     pass
>>> class B(A):
...     pass
>>> isinstance(B(), A)
True
>>> type(B()) == A
False
 ```
# 数字(Number)类型
## 概述
python中数字有四种类型：整数、布尔型、浮点数和复数。
```
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、**3E-2**
complex (复数), 如 1 + 2j、 1.1 + 2.2j，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， **复数的实部a和虚部b都是浮点型**。complex(x, y) 表示的是将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y
```
## 类型转换
　　三种不同的数值类型：int，float，complex--因此有int(x),float(x),complex(x)）
## 数学运算
+, -, * 和 // (向下取整)` **`,ceil(x)是向上取整
(1)`//` 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
```
>>> 7//2
3
>>> 7.0//2
3.0
>>> 7//2.0
3.0
>>>
```
(2)不同类型的数混合运算时会将整数转换为浮点数：
```
>>> 3 * 3.75 / 1.5
7.5
>>> 7.0 / 2
3.5
```
(3)在 **交互模式**中，最后被输出的表达式结果被赋值给变量 _ 。例如：
```
>>> a=6
>>> b=3
>>> a/b  #总是返回一个float数
2.0
>>> a+_  #_为式子(表达式)a/b的值,
8.0
```
说明:
　　实际情况是你也可以对于_ 赋值，_=10 是没有毛病的，但这样的结果会导致你在之后调用 _ 的时候全部变成了10
(4)不同类型的数混合运算时会将整数转换为浮点数：
```
>>> 3 * 3.75 / 1.5
7.5
>>> 7.0 / 2
3.5
```
# 字符串(String)

**因为字符串是一种特殊的tuple,而tuple又是一种不变的list,字符串是不可更改,同时可以用索引访问.因此在解决字符串的时候,遵循list取值原则**
## Python转义字符
```
\(在行尾时)	续行符
\b	退格(Backspace)
\000	空
\n	换行
\t	横向制表符
\r	回车
\f	换页
```
## 字符串运算符

加号 + 是列表连接运算符，星号 * 是重复操作

```
(1)空行:print(a+'\n')
(2)print(str[2:])             # 输出从第三个开始的后的所有字符
(3)print(str * 2)             # 输出字符串两次
(4)print(str + '你好')        # 连接字符串(也可以叫更新字符串)
(5)print('hello\nrunoob')      # **使用反斜杠(\)+n转义特殊字符**
(6)等待用户输入:input("等待用户输入:")
(7)双引号,单引号,引起来的任意文本;
(8)open(r"c://") 字符串前面加个r主要是为了防止字符串(路径)转义,参考:[python字符串前面加上'r'的作用](https://www.cnblogs.com/YangtzeYu/p/7875634.html),由于正则表达式和 \ 会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上'r'。
```

## 格式化字符串
　　在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。从python2.6开始引入了str.format()这个方式增强了格式化字符串,可以用来输出和写入.
```
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
```

python字符串格式化符号

| 符   号 | 描述                                 |
| ------- | ------------------------------------ |
| **%c**  | 格式化字符及其ASCII码(c,普通字符)    |
| %s      | 格式化字符串                         |
| %d      | 格式化整数                           |
| %u      | 格式化**无符号整型**                 |
| %o      | 格式化**无符号**八进制数             |
| %x      | 格式化**无符号**十六进制数           |
| %X      | 格式化**无符号**十六进制数（大写）   |
| %f      | 格式化浮点数字，可指定小数点后的精度 |
| %e      | 用**科学计数法格式化浮点数**         |
| %E      | 作用同%e，用科学计数法格式化浮点数   |
| %g      | %f和%e的简写                         |
| %G      | **%f 和 %E 的简写**                  |
| %p      | 用十六进制数格式化变量的地址         |

## unicode字符串
　　由于在python2当中,为了节省存储空间,在普通的字符(也就是在ascii码的范围之内的,占用一个字节,8bit)采用ascii码进行存储,对于其他字符使用unicode编码进行存储,(占用的是两个字节,16bit).主要实现手段就是在字符串前面添加u,即可.
　　但是在python3中,统一为unicode字符串存储

## 字符串的内建函数

| 序号 | 方法及描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | [capitalize()](https://www.runoob.com/python3/python3-string-capitalize.html) 将字符串的**第一个字符转换为大写** |
| 2    | [center(width, fillchar)](https://www.runoob.com/python3/python3-string-center.html) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。 |
| 3    | [count(str, beg= 0,end=len(string))](https://www.runoob.com/python3/python3-string-count.html) **返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数** |
| 4    | [bytes.decode(encoding="utf-8", errors="strict")](https://www.runoob.com/python3/python3-string-decode.html) Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来**解码给定的 bytes 对象**，这个 **bytes 对象可以由 str.encode() 来编码返回。** |
| 5    | [encode(encoding='UTF-8',errors='strict')](https://www.runoob.com/python3/python3-string-encode.html) 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是**'ignore'或者'replace'** |
| 6    | [endswith(suffix, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-endswith.html) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False. |
| 7    | [expandtabs(tabsize=8)](https://www.runoob.com/python3/python3-string-expandtabs.html) 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。 |
| 8    | [find(str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-find.html) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1 |
| 9    | [index(str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-index.html) 跟find()方法一样，只不过如果str不在字符串中会报一个异常. |
| 10   | [isalnum()](https://www.runoob.com/python3/python3-string-isalnum.html) 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False |
| 11   | [isalpha()](https://www.runoob.com/python3/python3-string-isalpha.html) 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False |
| 12   | [isdigit()](https://www.runoob.com/python3/python3-string-isdigit.html) 如果字符串只包含数字则返回 True 否则返回 False.. |
| 13   | [islower()](https://www.runoob.com/python3/python3-string-islower.html) 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False |
| 14   | [isnumeric()](https://www.runoob.com/python3/python3-string-isnumeric.html) 如果字符串中只包含数字字符，则返回 True，否则返回 False |
| 15   | [isspace()](https://www.runoob.com/python3/python3-string-isspace.html) 如果字符串中只包含空白，则返回 True，否则返回 False. |
| 16   | [istitle()](https://www.runoob.com/python3/python3-string-istitle.html) 如果字符串是标题化的(见 title())则返回 True，否则返回 False |
| 17   | [isupper()](https://www.runoob.com/python3/python3-string-isupper.html) 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False |
| 18   | [join(seq)](https://www.runoob.com/python3/python3-string-join.html) 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
| 19   | [len(string)](https://www.runoob.com/python3/python3-string-len.html) 返回字符串长度 |
| 20   | [ljust(width[, fillchar\])](https://www.runoob.com/python3/python3-string-ljust.html) 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。 |
| 21   | [lower()](https://www.runoob.com/python3/python3-string-lower.html) 转换字符串中所有大写字符为小写. |
| 22   | [lstrip()](https://www.runoob.com/python3/python3-string-lstrip.html) 截掉字符串左边的空格或指定字符。 |
| 23   | [maketrans()](https://www.runoob.com/python3/python3-string-maketrans.html) 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 |
| 24   | [max(str)](https://www.runoob.com/python3/python3-string-max.html) 返回字符串 str 中最大的字母。 |
| 25   | [min(str)](https://www.runoob.com/python3/python3-string-min.html) 返回字符串 str 中最小的字母。 |
| 26   | [replace(old, new [, max\])](https://www.runoob.com/python3/python3-string-replace.html) 把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。 |
| 27   | [rfind(str, beg=0,end=len(string))](https://www.runoob.com/python3/python3-string-rfind.html) 类似于 find()函数，不过是从右边开始查找. |
| 28   | [rindex( str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-rindex.html) 类似于 index()，不过是从右边开始. |
| 29   | [rjust(width,[, fillchar\])](https://www.runoob.com/python3/python3-string-rjust.html) 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串 |
| 30   | [rstrip()](https://www.runoob.com/python3/python3-string-rstrip.html) 删除字符串字符串末尾的空格. |
| 31   | [split(str="", num=string.count(str))](https://www.runoob.com/python3/python3-string-split.html) num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串 |
| 32   | [splitlines([keepends\])](https://www.runoob.com/python3/python3-string-splitlines.html) 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
| 33   | [startswith(substr, beg=0,end=len(string))](https://www.runoob.com/python3/python3-string-startswith.html) 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。 |
| 34   | **[strip([chars\])](https://www.runoob.com/python3/python3-string-strip.html) 在字符串上执行 lstrip()和 rstrip()** |
| 35   | [swapcase()](https://www.runoob.com/python3/python3-string-swapcase.html) 将字符串中大写转换为小写，小写转换为大写 |
| 36   | [title()](https://www.runoob.com/python3/python3-string-title.html) 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) |
| 37   | [translate(table, deletechars="")](https://www.runoob.com/python3/python3-string-translate.html) 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中 |
| 38   | [upper()](https://www.runoob.com/python3/python3-string-upper.html) 转换字符串中的小写字母为大写 |
| 39   | [zfill (width)](https://www.runoob.com/python3/python3-string-zfill.html) 返回长度为 width 的字符串，原字符串右对齐，前面填充0 |
| 40   | [isdecimal()](https://www.runoob.com/python3/python3-string-isdecimal.html) 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。 |

说明:
　(1)字符的编码与解码:**字符串对象通过encode编码成bytes对象,通过decode解码还原成字符串对象**

```
#字符串--`xx`
>>> b='xx'.encode()
>>> b.decode()
'xx'
#字节bytes对象b没有变(重点),
#解码部分最好使用指定变量来接收(相同变量b或者不同变量c接收都可以)
>>> b
b'xx'
>>> c=b.decode()
>>> c
'xx'
#正式部分,指定编码,读取的
#编码之后得到的是一个bytes对象,这个要注意
>>> b='xx'.encode(encoding='utf-8',errors='strict'/'ignore')
>>> b.decode(encoding='utf-8')
'xx'
>>> b.decode(encoding='gbk')
'xx'
>>> b.decode(encoding='utf-16')
'硸'
```
　(2)保留分隔符的拆分:(只能使用一个分隔符)
　　存在返回(分隔符左边子串,分隔符,分隔符右边子串),不存在返回(完整子串,"","")
```
>>> s1 = "I'm a good,sutdent"
>>> s1.partition(",")
("I'm a good", ',', 'sutdent')
>>> s1.partition(",good")
("I'm a good,sutdent", '', '')
>>> s1.partition("a,")
("I'm a good,sutdent", '', '')
```
## 注意
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用* 运算符重复。
3、Python中的字符串有两种索引方式，从**左往右以0开始**，从**右往左以-1开始**。具体看下图:
![python字符串索引](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190425165412.png)
4、Python中的  **字符串不能改变 **

5 . 反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。具体见下代码:
```
>>> a="""d
... dsds"""
>>> b='''dds
... sas'''
>>> a+b
'd\ndsdsdds\nsas'
>>> 
```
6 . Python  **没有单独的字符类型 **， **一个字符就是长度为1的字符串**。
7 .字符串的取整
```
var1 = "hello world";
#默认从尾部某一位置，开始向后截取
print(var1[-2: ]); # ld
```
# 字符编码与字节编码
## 字符编码
```
>>> chr(97)  #根据字符的编码返回字符
'a'
>>> ord('a') #根据字符解析成字符编码
97
```
ord(inal)--ord(),chr()
字符编码有:**整数编码**--可以用各个不同的进制形式表示--例如:
(1)'中文'-->'20013 25991 '-->`\u4e2d\u6587`(使用ord转换为整数,使用chr将整数还原为字符)
## 字节编码
encode,decode
字节编码有好多:utf-8,ascii等--注意各个编码所能表示的长度
bytes类型的数据用**带b前缀**的单引号或双引号表示:
```
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
```
如果bytes中包含无法解码的字节，decode()方法会报错：
```
>>> b'\xe4\xb8\xad\xff'.decode('utf-8')
Traceback (most recent call last):
  ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
```
如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
```
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中'
```
说明:在进行字节**编码**的时候,**无法用ascii编码编码**表示,**都是用\x##来代替**
　　(1)unicode是一个标准,把所有语言的编码都统一起来---读取--不会乱码--都是两个字节--把utf-8编码的文件,转换为unicode编码,读取到内存当中(unicode编码)
　　(2)utf-8:存储,传输(硬盘)的时候,省空间--英文一个字节,其余字符/语言两个字节
## 原因
　　因为数据之间的存储,传输,都是需要将字符转换为字节,(中文一个字符转换为utf-8编码占三个字节,英文一个字符转换为一个字节),因此从网络和硬盘上读取的字节流就是bytes/字节,
# 内置数据结构及其操作
[python四种内置数据类型](https://www.cnblogs.com/soaringEveryday/p/5044007.html)
　　array当中的元素的类型是需要相同的--numpy,数组,矩阵(因此需要数据类型相同);List则是不需要的,可变,数据类型可以不一致.
　　List-->不变的List(tuple)-->dict字典-->类似dict当中的key元素的组合(key)---set集合中的元素的数据类型相同.
　　Tuple:常用于数据返回值
　　set:判断元素在集合当中是否存在.
具体如下:![四种内置类型的区别](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190403222922.png)
## 类型转换
### 列表
#### 二维列表转换为一维列表
第一种:
```
nums = 
[[1,2],
 [3,4]]
a = sum(nums,[])  
```
第二种:
```
ab = [[1,2,3], [5,8], [7,8,9]]
print([i for item in ab for i in item])
```
第三种:
```
from tkinter import _flatten
a = [[1, 2], [3, 4]]
print(list(_flatten(a)))
```
第四种
```
from itertools import chain
a = [[1, 2], [3, 4]]
print(list(chain.from_iterable(a)))
```
chain.from_iterable(a)打印的是迭代器对象
#### 列表转换为字符串
　　"".join(list)
### 字符串
#### str与bytes对象互换
　　str转为bytes对象:a=str.encode(encoding="utf-8",errors="strict"/"ignore")
　　bytes对象转为str:a.decode(encoding="utf-8",errors="strict"/"ignore"),参数最好一一对应
#### str转换为列表,元组
list(str)tuple(str)
```
>>> var='菜鸟教程'
>>> tuple(var)
('菜', '鸟', '教', '程')
>>> list(var)
['菜', '鸟', '教', '程']
```
## 结构遍历
### 序列遍历
enumerate
### 字典遍历
dict.items
### 同时遍历多个序列
　　同时遍历两个或更多的序列，可以使用 zip() 组合：
```
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
>>> 可以构建字典:dict(q=a)
>>> 可以进行其他选择操作
```
## 结构推导式
　　提供了一种简明扼要的方法来创建对应的数据类型--常用**for循环进行创建(根据已有的数据)**--这个是重点--常用for循环快速创建
### 列表
#### for循环
```
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
```
#### 嵌套列表
实例将3X4的矩阵列表转换为4X3列表：
```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
### 集合选取
(1)set()
(2)for 循环创建集合--推导式
```
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```
### 字典构建
　　构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
#### (1)参数列表
```
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```
　　构造函数 dict() 直接**从键值对元组,列表中构建字典**。
#### (2)for循环--推导式
　　如果有固定的模式，列表推导式指定特定的键值对：
　　字典推导可以用来创建任意键和值的表达式词典：
```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
#### (3)参数等式式子创建
　　如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
```
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

# list
## list与Array的区别

|          | list                         | array                   |
| -------- | ---------------------------- | ----------------------- |
| 元素类型 | 可以不同,任意类型            | 类型要求一致,通常是数值 |
| 场景     | 存储数据                     | **数值计算**            |
| 长度     | 不固定,使用append,extend增加 | **固定**                |

　　array的出现主要是为了进行数值计算,因为numpy本身就是一个科学计算包,因此numpy库的基本的数据处理类型是array,metrics(矩阵)也是numpy的基本的数据处理类型,只不过是二维的array,我们通常叫他矩阵罢了.
　　array**可以通过list或者tuple或者其他类型转换而来,也可以自己创建.**
　　从下图,我们就可以看到**列表list无法直接进行数值计算(本质原因)**,需要把里面的元素取出来才能计算,而array则是可以直接运算,这就是array存在的必要性
```
x = [1,2,'a']   #x是一个list，list里面的元素的数据类型可以不同
print(x[0])     #可以根据索引取x的元素
y = x + x       #列表无法运算，+号只能将两个list拼接
print(y)        #拼接后的list

import numpy as np
a = np.array([1,2])  #a是一个数组
print(a[0])         #可以根据索引来取a中的元素
b = a + a           #数组可以运算 
print(b)            #运算后得到的数组
```
## 运算
### 插入
append将对象**直接插入**链表中, 比如:
```
x = [1, 2, 3]
x.append([4, 5])
print (x)
得到如下结果: 
[1, 2, 3, [4, 5]]
```
extend将**参数内部的元素拆分再插入**, 比如:
```
x = [1, 2, 3]
x.extend([4, 5])
print (x)
得到如下结果: 
[1, 2, 3, 4, 5]
```
指定位置插入:
```
>>>classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```
### 修改
list[i]=设置的值
### 删除
末尾删除:pop()
删除指定位置:pop(i)
list与tuple中的元素可以不同
## 注意
1、和字符串一样，list可以被索引和切片。
2、Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串,具体如下图:
![](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190426195107.png)
3、注意取出的类型是不一样的--因此我们在进行数值取值的时候,要特别小心
```
>>>list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
>>>list[2:3]
>>>[2.23]
>>>list[2]
>>>2.23
```
4 .python 的变量类型是动态的，**变量的类型由赋予它的当前时刻值**来决定，例如：
```
>>> a = 1
>>> a = 1.001
>>> a = "python"
>>> print(a)
python
```
  第一次为变量 a 赋值为整型，第二次赋值是浮点数，第三次是一个字符串，最后输出时只保留了**最后一次的赋值---这也就是我们常用变量进行本身覆盖的原因**--例如式子:`contentLength+=len(word)`.
5 .关于列表元素的删除
  [关于列表元素的删除](https://www.cnblogs.com/chuangming/p/8458966.html)
# tuple
1、不变的list,为了与(2),区分,使用(2,)进行区别;字符串是一种特殊的tuple,元组也可以被索引和切片，方法一样。
2、string、list 和 tuple 都属于** sequence（序列）**。--可以根据下标取值
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。(用逗号隔开)
```
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
```
4、元组也可以使用+操作符进行拼接
# 集合set
## 基本概率
集合有可变集合和不可变集合():
```
s = set('beginman')
t = frozenset('pythonman')  #不能CRUD
```
　　基本功能是进行**判断元素是否在内**和**去重**
　　可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
 　**set集合是无序的，不能通过索引和切片**来做一些操作
```
parame = {value01,value02,...}
或者
# 只有一个参数
set(value)
```
其中集合的元素类型可以不一样:
   ```
>>> set={"ds",2}
>>> print(set)
{2, 'ds'}
   ```
##    运算
### 交并差
   ```
>>> a - b                              # 集合a中包含而集合b中不包含的元素 --差集
{'r', 'd', 'b'}
>>> a | b                              # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 集合a和b中都包含了的元素
{'a', 'c'}
>>> a ^ b                              # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}
   ```
### 创建,删除,增加
set(),例子如下:
1. 单个值的创建:单个的时候,是**双括号,加上`,`才是整体创建**,否则会将**单词拆分创建集合**
2. 多个值的创建:**set(一个参数)--创建集合,因此当有多个值的使用,需要使用(),[]框起来**
```
>>> myset=set("apple",)
>>> myset
{'l', 'a', 'e', 'p'}
# 注意是双括号,加上`,`才是整体创建,否则会将单词拆分创建集合
>>> myset=set(("apple",))
>>> myset
{'apple'}
>>> myset=set(("apple"))
>>> myset
{'l', 'a', 'e', 'p'}
```
remove(x)-->指定删除;set.discard(value)
pop()-->随机删除
set.clear()-->清空集合
add():要传入的元素做为一个整个添加到集合中，**插入位置随机**--element
update():把要传入的元素拆分，做为个体传入到集合中,具体看一下代码:--s
```
>>> a=set("abc")
>>> a
{'b', 'a', 'c'}
>>> a.add('python')
>>> a
{'b', 'a', 'python', 'c'}
>>> a.update("python")
>>> a
{'a', 'python', 'p', 'y', 'b', 't', 'h', 'c', 'o', 'n'}
>>> a.remove("python")
>>> a
{'a', 'p', 'y', 'b', 't', 'h', 'c', 'o', 'n'}
```
## 注意
　　set对tuple,list的元素会进行排序---根据元素值排序,不根据地址排序,
　　set.pop(),是对去重,排序之后的值进行,从左到右依次进行删除---在数值元素当中比较明显,不是所谓的随机删除集合中的元素. 满足这要求,需要set集合当中的元素为全部为数值,不能包含其他类型的,但原则不变,还是对排序之后的集合元素从左到右删除.
具体例子如下:
```
>>> set1=set([9,9,4,4,5,2,6,7,1,8,])
>>> set1
{1, 2, 4, 5, 6, 7, 8, 9}
>>> print(set1.pop())
1
>>> set
<class 'set'>
>>> set1
{2, 4, 5, 6, 7, 8, 9}
>>> print(set1.pop())
2
>>> set1
{4, 5, 6, 7, 8, 9}
>>> set1=set((9,9,4,4,5,2,6,7,1,8,))
>>> set1
{1, 2, 4, 5, 6, 7, 8, 9}
>>> print(set1.pop())
1
>>> set1
{2, 4, 5, 6, 7, 8, 9}
>>> print(set1.pop())
2
>>> set1
{4, 5, 6, 7, 8, 9}
>>> 
```
set与list的索引号:具体见下图:
![set与list的索引号](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190504172643.png)
# 字典 
　　key与value要同时初始化,不能单独初始化;
　　找出字典中的最大值
　　列表是有序的对象集合，字典是**无序的对象集合**。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取(不能根据下标的变化来取值.
## 概念
　　字典是另一种可变容器模型，且可存储任意类型对象。
　　字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
1. 键必须是唯一的，但值则不必,值可以为任何类型。
2. **值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。**,数字其实也是不可变的字符串
## 运算
### 基本运算
(1)修改,增加:dict['Age'] = 8
(2)删除:
```
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
pop(删除,key)
```
(3)输出:str(dict)输出字典，以可打印的字符串表示。
(4)长度:len(dict)
### 子字典的打印及其输出
```
cities={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
```
可以使用如下方法进行列出
```
for i in cities['北京']:
    print(i)
```
将列出如下结果：(**这个输出是重点,没有输出全部,只是输出了key**)
```
朝阳
海淀
昌平
怀柔
密云
```
如果:
```
for i in cities['北京']['海淀']:
    print(i)
```
输出如下结果：
```
圆明园
苏州街
中关村
北京大学
```
### 字典k-v反转
reverse = {v: k for k, v in dic.items()}
### 获取字典中最大的值及其键
```
prices = {
    'A':123,
    'B':450.1,
    'C':12,
    'E':444,
}

max_prices = max(zip(prices.values(), prices.keys()))
print(max_prices) # (450.1, 'B')
```
### dict.keys()
在 **python2.x dict.keys 返回一个列表**，但是在在 Python 3.x 下，dict.keys 返回的是 **dict_keys 对象，若需要转换为列表**，请使用：
```
list(dict.values())
list(dict.keys())
```
修改上面实例：
```
>>> sites_link = {'runoog':'runoob.com', 'google':'google.com'}
>>> sides = sites_link.keys()
>>> list(sides)
['runoog', 'google']
```
否则直接使用,会出现TypeError：
`TypeError: 'dict_keys' object does not support indexing`

## 注意
　　字典类型也有一些内置的函数，例如clear()、keys()、values()等。
注意：
　　1、字典是一种映射类型，它的**元素**是键值对。
　　2、字典的关键字key必须为不可变类型，且不能重复。
　　3、**创建空字典使用 { }。**
　　4、输入 dict 的**键值对**(k,v)，可直接用 items() 函数：

```
dict1 = {'abc':1,"cde":2,"d":4,"c":567,"d":"key1"}
for k,v in dict1.items():
    print(k,":",v)
```
　　判断某个键是否在字典中-->`for key in dict`,
　　除了在字典上使用` items()` 函数,可以在`list,tuple`当中使用
　　`for index,data in enumerate(list列表)`,因为,set是无序的,因此不能使用索引
5 .其实d不一定必须为一个序列元组，如下：

```
>>> dict_1 = dict([('a',1),('b',2),('c',3)]) #元素为元组的列表
>>> dict_1
{'a': 1, 'b': 2, 'c': 3}
>>> dict_2 = dict({('a',1),('b',2),('c',3)})#元素为元组的集合
>>> dict_2
{'b': 2, 'c': 3, 'a': 1}
>>> dict_3 = dict([['a',1],['b',2],['c',3]])#元素为列表的列表
>>> dict_3
{'a': 1, 'b': 2, 'c': 3}
>>> dict_4 = dict((('a',1),('b',2),('c',3)))#元素为元组的元组
>>> dict_4
{'a': 1, 'b': 2, 'c': 3}
```
6 .无序和有序
　　(1). 无序：集合是无序的，所以不支持索引；字典同样也是无序的，但由于其元素是由键（key）和值（value）两个属性组成的键值对，可以通过键（key）来进行索引
　　(2). 元素唯一性：集合是无重复元素的序列，会自动去除重复元素；字典因为其key唯一性，所以也不会出现相同元素

７.切片设置步长

```
demo = [1,2,3,4,5,6]
new_demo = demo[1::2]  # 2 就是步长 意思是从索引为 1 的元素开始 每隔2个元素取一次元素
new_demo = [2,4,6]
```
　　注意是2,4,6,**步长是从下一位开始数**
8 .demo[x][y]与demo[x:y]
（１）demo[x][y]针对是**二维及其以上**(不同维度上选择)
（２）demo[x:y]是同一维度的选择,后面还可以加上步长
9 .布尔值的常量 True 和 False
　Python 中布尔值使用常量 True 和 False 来表示。
（１）在数值上下文环境中，True 被当作 1，False 被当作 0，例如

```
>>> True+3
4
>>> False+2
2
```
（２）其他类型值转换 bool 值时除了 ''、""、''''''、""""""、0、()、[]、{}、**None--可以表现为False**、0.0、0L、0.0+0.0j（复数形式）、False 为 False 外，其他都为 True 例如：----重点理解**（0，0.0，None，[],{},(),"")**
```
>>> bool(-2)
True
>>> bool('')
False
```

10 .Python2与Python3的区别--Bool类型
　　Python2 支持：int、float、long、complex（复数）
　　Python3 支持：int、float、bool(常量flase 和 true)、complex（复数）
　　Python3 废除了 long 类型，将 **0 和 1 独立出来**组成判断对错的 Bool 型，即 0 和 1 可以用来判断 flase 和 true。但是根本上并没有修改原则。**这里的 Bool 型依然是 int 型的一部分**--**这也就是为什么可以对bool的常量进行运算的原因**，所以依然能当做数字参与运算，所以 Python3 里的** Bool 型是 int 型的一个特例而不是一个独立的类型**

# 输入与输出
## 输出
　　Python两种输出值的方式: 表达式语句和 print() 函数。
　　第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
　　如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
　　如果你希望将**输出的值转成字符串**，可以使用 repr() 或 str() 函数来实现。
```
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
>>> s = 'Hello, Runoob'
>>> str(s)
'Hello, Runoob'
>>> repr(s)
"'Hello, Runoob'"
>>> str(1/7)
'0.14285714285714285'
```
　　repr(x*x).rjust(3)字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
　　还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
另一个方法 zfill(), 它会在数字的左边填充 0
```
'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:

>>> import math
>>> print('常量 PI 的值近似为： {}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793。
>>> print('常量 PI 的值近似为： {!r}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793
```
　　因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().
　　# 输出
### 格式化输出
```
print('%02d-%02d' % (3, 1))
03-01
```
### 字符串的输出
```
%10s——右对齐，占位符10位
%-10s——左对齐，占位符10位
%.2s——截取2位字符串
%10.2s——10位占位符，截取两位字符串---取出之后再对齐
```
具体形式见下图:
```
>>> print('%s' % 'hello world')  # 字符串输出
hello world
>>> print('%20s' % 'hello world')  # 右对齐，取20位，不够则补位
         hello world
>>> print('%-20s' % 'hello world')  # 左对齐，取20位，不够则补位
hello world         
>>> print('%.2s' % 'hello world')  # 取2位
he
>>> print('%10.2s' % 'hello world')  # 右对齐，取2位
            he
>>> print('%-10.2s' % 'hello world')  # 左对齐，取2位
he
```


## 输入
### 键盘输入
input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘
```
str = input("请输入：");
print ("你输入的内容是: ", str)
```
### 标准输入与输出
open(filename, mode)：
　　第一个参数为要打开的文件名。
　　第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容,所写的任何数据**都会被自动增加到末尾**,没有则**创建新的文件**. 'r+' **同时用于读写**。 **mode 参数是可选的; 'r' 将是默认值**,如果创建新文件,则说明需要模式w或者r+之类的写
具体例子如下:
```
# 打开一个文件
f = open("/tmp/foo.txt", "w")
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# 关闭打开的文件
f.close()
```
```
+:可读可写
W:可以覆盖和创建
r:只读,不覆盖,创建
a:文件内容追加与创建
```
![文件读写模式](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190507091147.jpeg)
input() 默认输入的为 str 格式，若用数学计算，则需要转换格式，例：

```
a=input('请输入数字:')
print(a*2)
```
假设输入数值为3，则上例中得出结果为：
```
33
```
若将代码修改为：
```
a=int(input('请输入数字:'))
print(a*2)
```
则结果为：`6`
## 参考文献
[python基础_格式化输出（%用法和format用法）](https://www.cnblogs.com/fat39/p/7159881.html)
# 文件读写
## f.read()
　　为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个**可选的数字类型的参数**。 当 **size 被忽略了或者为负**, 那么该文件的所有内容都将被读取并且返回。
## f.readline() 
　　f.readline() 会从文件中读取单独的一行,如果需要读取全部的内容,则需要进行for循环.f.readlines() 则不需要进行for循环,就可以读取文件的所有行(所有内容)
f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行;
## f.readlines()
　　f.readlines() 将返回该文件中包含的所有行。
## f.write()
　　如果要写入一些不是字符串的东西, 那么将需要先进行转换成字符串,才可以进行输入:
```
#!/usr/bin/python3
# 打开一个文件
f = open("/tmp/foo1.txt", "w")
#不是字符串
value = ('www.runoob.com', 14)
s = str(value)
f.write(s)
# 关闭打开的文件
f.close()
```
## f.close()
  　　在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
  　　当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。--**使用f.close()文件关闭之后,在进行调用该文件,就会出现异常**
 所以直接使用f.close()有两个弊端:
  　　(1)没有及时将缓存写入到文件当中,容易造成写入丢失;
 　　 (2)当关闭该文件的时候.在此调用会出现异常--`I/O operation on closed file`
具体见下面例子:

```
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: I/O operation on closed file
```
因此常使用with open读写文件,完成之后,会及时地关闭文件
(1)注意
　　将** mode 设置为 w+ 或 a+ 时，发现直接进行读操作，得到的内容都是空**，但原因不太相同：

　　如果 mode 设置为 w+，即使没有执行 write 操作，也会将文件内容清空，因此这个时候**直接进行读草稿**，读到的是空内容。
```
f = open("E:\\administrator\\Desktop\\test.txt", "w+")
```
　　如果 mode 设置为 a+，文件指针位置默认在最后面，因为读内容时，是按照指针的位置往后读，**所以如果指针位置在最后，那读出来的是空，在读之前，一定要注意确认好指针位置是对的**。
```
f = open("E:\\administrator\\Desktop\\test.txt", "a+")
f.write("append content")
print(f.tell())  #此时指针在文件字符末尾处
f.seek(0)
print(f.tell())  # 指针回到0的位置
str = f.read()
print(str)
f.close()f = open("E:\\administrator\\Desktop\\test.txt", "w+")
```
## 例子
以一个每两行生成一个文件为例子:
```
import sys
import os
result=[]
"""
with就是为了防止文件忘了关闭,导致数据只写入一部分,因为系统不是
'r':代表对文件的操作模式,读取出来的是字符串,
'rb':read binary :返回的是字节,w与wb类似,
r+则是读写都可以
encoding主要是为了以某种编码格式进行文件读取;
errors主要是为了文件以某件编码格式进行读取的时候,
文件有编码不规范的现象出现UnicodeDecodeError;
"""
with open("/Users/ivega/Desktop/xx/file/result.txt", 'r',encoding='utf-8',errors='ignore') as f1:
    for x in zip(f1.readlines()):
        result.append(x)
n=1
count=1
path='/Users/ivega/Desktop/xx/file/sep'
# 设置文件的存储路径
os.chdir(path)
# 新建一个文件
file=open(str(n)+'.txt','w')
for i in range(len(result)):#一行行的把数据从硬盘加载到内存里读出来
	if(count==1):
		# 将tuple数据转换为字符串str数据
		file.write(" ".join(tuple(result[i])).strip(' \u200b\u200b\u200b'))
		count=2
		print(result[i])
	else:
		file.write(" ".join(tuple(result[i])).strip('\u200b\u200b\u200b').strip('\n'))
		print(result[i])
		n+=1
		file=open(str(n)+'.txt','w')
		count=1
# 最后文件写完之后记得保存
file.close()
```
(1)read:一次性读取文件的所有内容,**适合文件比较小**的情况
(2)readline:**逐行读取:适合文件不知道多大的情况**,
(2)readlines:一次性读取文件的全部内容,**将每行的数据存储在List列表当中,适合配置文件**,**可以用list进行访问**.
至于三种方法读取的是什么,由读取的模式决定:
```
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'--字符
```
## open函数参数说明
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:
```
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:

mode 参数有：
模式	描述
t	文本模式 (默认)。
```

file.next()
　　Python 3 中的 File 对象不支持 next() 方法。
　　此外 w+ 的使用方法：不能直接 write() 后，在进行读取，这样试读不到数据的，因为数据对象到达的地方为文件最后，读取是向后读的，因此，会读到空白，应该先把文件对象移到文件首位

```
f = open("forwrite.txt", "w+",encoding='utf-8')
f.write("可以 ，你做的很好！ 6666")  # 此时文件对象在最后一行，如果读取，将读不到数据
s=f.tell()     # 返回文件对象当前位置
f.seek(0,0)    # 移动文件对象至第一个字符
str=f.read()
print(s,str,len(str))
```

# pyrhon序列化
## pickle
　　将变量转为可存储的数据的过程-->序列化,结果通常是二进制或者十六进制
```
pickle.dump(file,variable)
pickle.load(file)
```
pickle不同版本不怎么兼容,保存不怎么重要的值,不是全平台通用.
## pickle模块
　　数据序列:将程序中运行的对象存储在文件当中;
　　数据反序列化:从相应的pkl文件(序列化文件)加载上一次程序保存的对象.

```
pickle.dump(obj, file, [,protocol])
```
　　obj:对象名;file:保存的文件;[,protocol],说明协议是可选的.
```
#文件序列化
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
utput = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
#使用pickle模块从文件中重构python对象,加载
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
```
参数解释
```
protocol为序列化使用的协议版本，
0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；
1：老式的二进制协议；
2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为0。
-1:使用可用的最高协议来挑选列表
```

## JSON解析
### json特点
json数据全平台通用,且utf-8编码
json常用将变量序列化,很少直接使用dict:
json.dumps(student对象, default=lambda student: student.__dict__)--返回的是一个str,内容就是标准的JSON.
'{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str, object_hook=dict2student)
feel like object:类文件对象--变量
### 概念(数据类型和对象)
JSON (JavaScript **Object Notation(标记)**) 是一种**轻量级的数据交换格式**,对象是名称--值对构成的列表或集合，数组是值构成的列表或集合；还有一点就是**数组中所有的值应具有相同的数据类型**。在数组中虽然可以混合使用各种类型的数据，但是并不推崇这么做.**json的数据类型其实就是值对应的类型**,**对象则是指名称-值的组合**,**因此json的数据类型就是指json中各个对象的数据类型**.具体请看:
### python数据对象('')与json数据对象("")
Python对象数据类型与Json对象数据类型对比图:

| Python                                 | JSON   |
| -------------------------------------- | ------ |
| dict                                   | object |
| list, tuple                            | array  |
| str                                    | string |
| int, float, int- & float-derived Enums | number |
| True                                   | true   |
| False                                  | false  |
| None                                   | null   |

python-->json:叫做编码:json.dumps(python数据对象)
json-->python:叫做解码:json.loads(json对象)
具体式子如下:
```
import json
 
# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
#Python 字典之后可以使用key进行查询
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])
```
结果为:
```
Python 原始数据： {'name': 'Runoob', 'no': 1, 'url': 'http://www.runoob.com'}
JSON 对象： {"name": "Runoob", "no": 1, "url": "http://www.runoob.com"}
data2['name']:  Runoob
data2['url']:  http://www.runoob.com
```
### 参考文献
[JSON的数据类型](https://www.cnblogs.com/fengxiongZz/p/6683376.html)



# 运算符
## 算术运算符
1. *	乘 - 两个数相乘或是返回一个被**重复若干次**的字符串
2. /	除 - x 除以 y	
3. %	取模 - 返回除法的余数	
4. **	幂 - 返回x的y次幂	
5. //	取整除 - 向下取(注意)接近除数的整数，注意：
```
>>> 9//2
4
>>> -9//2
-5
```
## 赋值运算符

| 运算符 | 描述             | 实例                                  |
| ------ | ---------------- | ------------------------------------- |
| =      | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c |
| +=     | 加法赋值运算符   | c += a 等效于 c = c + a               |
| -=     | 减法赋值运算符   | c -= a 等效于 c = c - a               |
| *=     | 乘法赋值运算符   | c *= a 等效于 c = c * a               |
| /=     | 除法赋值运算符   | c /= a 等效于 c = c / a               |
| %=     | 取模赋值运算符   | c %= a 等效于 c = c % a               |
| **=    | 幂赋值运算符     | c **= a 等效于 c = c ** a             |
| //=    | 取整除赋值运算符 | c //= a 等效于 c = c // a             |

## 逻辑运算符（重点）
重点是and 与 or 的返回值

| 运算符 | 逻辑表达式 | 描述                                                         | 实例                    |
| ------ | ---------- | ------------------------------------------------------------ | ----------------------- |
| and    | x and y    | 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。**(一错就错，全对返回y的值)** | (a and b) 返回 20。     |
| or     | x or y     | 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。（**优先返回x对的值**） | (a or b) 返回 10。      |
| not    | not x      | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |
![逻辑运算符](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190429172809.png)
### And 和 Or巧记
　　and： **从左到右计算表达式**，若**所有值均为真，则返回最后一个值，若存在假，返回第一个假值**；
　　or：也是从左到有计算表达式，**返回第一个为真的值**；
　　优先级：not>and>or
## 位运算符

| &    | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100  |
| ---- | ------------------------------------------------------------ | --------------------------------------------- |
| \|   | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101 |
| ^    | 按位异或运算符：当两对应的二进位相异时，结果为1              | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001  |

## 成员运算符

| 运算符 | 描述                                                    | 实例                                              |
| ------ | ------------------------------------------------------- | ------------------------------------------------- |
| in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

## 身份运算符

比较**两个对象的存储单元**.

| 运算符 | 描述                                        | 实例                                                         |
| ------ | ------------------------------------------- | ------------------------------------------------------------ |
| is     | is 是判断两个标识符是不是引用自一个对象     | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(a) != id(b)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

 [id()](https://www.runoob.com/python/python-func-id.html) 函数用于获取对象内存地址,
### is 与 == 区别
is 用于判断两个变量**引用对象是否为同一个**， == 用于**判断引用变量的值是否相等**。
## 运算符优先级

| 运算符                   | 描述                                                   |
| ------------------------ | ------------------------------------------------------ |
| **                       | 指数 (最高优先级)                                      |
| ~ + -                    | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % //                 | 乘，除，取模和取整除                                   |
| + -                      | 加法减法                                               |
| >> <<                    | 右移，左移运算符                                       |
| &                        | 位 'AND'                                               |
| ^ \|                     | 位运算符                                               |
| <= < > >=                | 比较运算符                                             |
| <> == !=                 | 等于运算符                                             |
| = %= /= //= -= += *= **= | 赋值运算符                                             |
| is is not                | 身份运算符                                             |
| in not in                | 成员运算符                                             |
| and or not               | 逻辑运算符                                             |


# 变量管理机制
## 基本概念
```
>>> b = 5  
>>> a = 5  
>>> id(a)  
162334512  
>>> id(b)  
162334512  
>>> a is b  
True
```
![image-20190429213158839](/Users/ivega/Library/Application Support/typora-user-images/image-20190429213158839.png)
　　说明在python 中，**变量是以内容为基准**而**不是像 c 中以变量名为基准**，所以只要你的数字内容是5，**不管你起什么名字，这个变量的 ID 是相同的**，同时也就说明了 python 中**一个变量可以以多个名称访问**，因此当其中一个变量的指向发生了变化，其余的变量所指向的内容不会变化。--**这也就是为什么python不支持自增运算的原因,如果实现自增运算,变量的id会不间断的变化**,如上图那样。
　　上面的部分在脚本式编程环境（.py文件）中没有问题。但是在交互式环境中，编译器会有一个小整数池（共享的概念，该范围内的整数共享池的id）的概念，会把（-5，256）间的数预先创建好，而当a和b超过这个范围的时候，两个变量就会指向不同的对象了，因此地址也会不一样，比如下例:
```
>>> a=1000
>>> b=1000
>>> id(a);id(b)
2236612366224
2236617350384
```
　　Python3 无长整，整数长度原则上不限，所以不能以假定的 32 位处理
　　在 python 中，**类型属于对象，变量是没有类型的**,变量名仅仅是一个对象的引用（一个指针），可以是**指向 List 类型对象**，也可以是**指向 String 类型对象**。
## 删除变量
　　删除变量是只是删除指向某个对象的指针;其他变量不受影响
```
# 核心:变量存储的是指针,指针指向对应的对象
def delVariable():
    # 把将变量a指向int值对象12,变量a存储的是一条指针,也就是变量a的值(很重要),指向的是变量
    a=12
    # 变量a把值复制给b,其实就是复制给b一条指针,因为变量a的值就是一条指针
    b=a
    # 删除了a变量,也就是把a变量的值--指针也删除了,但是b变量的值没有删除,b还能指向int值对象12
    del a
    # 打印变量b中的指针所指向的值
    print(b)
    return b
    
# 删除函数变量
def delFunction():
    def hi(name="yasoob"):
        return "hi " + name
    print(hi())
    # output: 'hi yasoob'
    # 函数其实也是个对象---正好显现了,python当中万物都是对象
    # hi作为函数名其实也是一个变量,里面存储的是指针,该指针指向对应函数的地址
    # 因此greet=hi也就相当于:把指向函数地址的指针,通过值传递复制给greet
    # ,因此当删除函数变量/函数名hi的时候,greet指向对应函数的地址还是不会删除;
    # 因此,只需要greet()即可根据函数的地址读取并执行函数
    greet = hi
    print(greet())
```
## 多值初始化
　　`a,b=b,a+b`,多值初始化,先**初始化右边的式子**,之后对左边式子进行赋值,但是在两边的式子当中,**都是从左到右执行**的,就相当于:
```
n=b,
m=a+b
a=n
b=m
```
## 多个变量赋值
　　`a = b = c = 1`**先创建一个整型对象**，值为 1，**从后向前赋值**，三个变量被赋予相同的数值。
　　您也可以为多个对象指定多个变量。例如：`a, b, c = 1, 2, "runoob"`

# 条件循环
## 循环
Python的循环有两种，一种是for...in循环，**依次把list或tuple中的每个元素**迭代出来
range函数
当遍历的类型不是tuple或者list的时候,
for i in range(len(dictDD))
list,tuple有序---因此可以直接使用for循环,直接取值,不需要根据索引号:
```
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
```
set,dict无序,则需要使用range(len(,set/dict))来进行遍历:取数的时候,则需要根据key来取.
## break
break提前结束当前所在的循环--记住一个break对应一个循环,注意嵌套循环
```
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前if循环,直接打印END，程序结束
    print(n)
    n = n + 1
print('END')
```
continue:提前结束**本次**循环,进入下次记住一个continue对应一个循环
```
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        **continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行**
    print(n)
```
执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9。
## if条件语句
　　在Python中没有switch – case语句,Python中没有do..while循环,只有while 判断条件：
**括号限定代码域，加强代码可读性**。
```
if (name == "pag"):{
  print(name == "pag") # True
}
```
如果 **if 语句中的条件过长，可以用接续符 \ 来换行。**
例如：
```
if 2>1 and 3>2 and 4>3 and \
    5>4 and 6>5 and 7>6 and \
    8>7:
    print("OK")
注意: \ 后的一行要缩进
```
## 可更改对象,不可更改对象
　　在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
　　不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个** int 值对象 10**，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。(**也就是变量指向新的对象**)因为python 中一切都是对象(int型对象,list对象)，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
　　可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了.
　　要判断这个对象是不是可更改,则根据对象的类型进行说明,变量只是指向对象
## while
### 句子
```
while 判断条件：
    语句
```
　　无限循环:在while中我们可以通过设置条件表达式永远不为 false 来实现无限循环:
　　以上的无限循环你可以使用 CTRL+C 来中断循环。
### while … else与for.....else
在 while … else 在判断条件为 false 时执行 else 的语句块
```
#!/usr/bin/python3
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```

**while 循环语句和 for 循环语句使用 else 的区别**：
　　1、如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
　　2.如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行！
但是如果循环体中有break的时候则不会执行else语句,直接退出.(重点)
```
for i in range(10):
    if i == 5:
        print 'found it! i = %s' % i
        break
else:
    print 'not found it ...'
```
　　如果没有break,当i==5之后执行下面的语句,还是会继续执行i ==6之类的语句,然后直至遍历完,也就是穷尽列表,或者下面的if 一直不满足(还是会穷尽列表之后才知道最终不满足--即使if下面有break,但是不执行,也没用)  /或者**while条件为false**的时候,最后导致执行else.
### 简单语句组
　　类似if语句的语法，如果你的**while循环体中只有一条语句**，你可以将该语句与while写在同一行中，
```
while (flag): print ('欢迎访问菜鸟教程!')
```
## for 语句
　　Python for循环可以遍历**任何序列的项目**，如一个列表或者一个字符串
```
str_1="xian"
x="an"
if x in str_1:
    print("正确")
else:
    print("错误")  
正确
```
　　在交互式下,输入多行之后,使用ctrl+enter执行即可
### break
　　break用来跳出当前for循环,不管离这个最近的 for 循环有多少个if--else
```
#!/usr/bin/python3
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```
输出结果为:
```
循环数据 Baidu
循环数据 Google
菜鸟教程!
完成循环!
```

## pass语句
　　Python pass是空语句，是**为了保持程序结构的完整性**,为了防止语法错误.
```
if a>1:
    pass #如果没有内容，可以先写pass，但是如果不写pass，就会语法错误
```
　　pass 不做任何事情，**一般用做占位语句**,pass,后面的语句还是会执行
根据**索引号及其内容**进行遍历:`for i, j in enumerate(sequence)`
### range
　　使用range指定区间的值：
```
实例
>>>for i in range(5,9) :
    print(i)
```
　　range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):`for i in range(5,9,2)`

# 遍历
[Python 数据遍历](https://www.jianshu.com/p/6b0a1011ef63)
## 序列遍历
序列:**list,tuple,字符串**
(1)含有索引号及其内容的遍历:
  　 for index,value in enumerate(sequence):
   　for x in sequence:
  　 for i in range(len(sequence)):
##  集合遍历
　　for x in set:
## 字典遍历
```
#!/usr/bin/python 
dict={"a":"apple","b":"banana","o":"orange"} 
for k in dict: 
        print ("dict[%s]=" %k,dict[k])
for (k,v) in  dict.items(): 
#好好理解这个式子,dict.keys()返回的是迭代器对象
for k,v in zip(dict.keys(),dict.values()): 
        print ("dict[%s]=" % k,v)
```
判断:
```
if x in book
```
# 函数闭包
　　[函数的闭包理解](https://www.jb51.net/article/134752.htm)
```
# 闭包函数:外层函数+内层函数
# 闭包:破除函数的层级限制,在任何地方都可以调用函数的内层函数
#     想保持函数的状态,因为引用的变量,一直在闭包函数中
#     延迟计算:因为f1=foo()得到的是含有某种状态的函数,并没有执行该函数,需要执行则f1()即可
# 外层函数
def foo():
    # 外层函数局部变量--内层函数最多引用到这里
    name = 1
    # 内层函数
    def bar():
        # 内部函数的变量,没有往外层函数局部变量,
        # 这个可以使用f1.__closure__进行查询,到底引用了几个外层函数的局部变量
        print(name)
        print("hello world in bar")
    # 返回内层函数的地址
    return bar
# 得到的是1,和内层函数的内存地址
f1 = foo()
# 既然是内层函数的地址,可以使用()将函数读取,执行
g=f1()
# 内层函数引用的值
# (<cell at 0x10bf150a8: int object at 0x10be237c0>,)--可以看出是tuple类型
# <cell at 0x10bf150a8: int object at 0x10be237c0>是引用值的地址,
print(f1.__closure__)
# tuple类型,引用的元素为tuple的元素,没有`return 内层函数名`,也可以使用,但不是闭包函数
print(type(f1.__closure__))
# 根据索引号取出引用的值
print(f1.__closure__[0].cell_contents)
def example1():
    # 从这里我们就可以看到,name的值没有用到
    name="xsad"
    f1()
# 执行引用了闭包的example函数
# 输出:hello world in bar,可以看到name值是没有改变的
# 因为闭包函数的内层函数,最多引用闭包函数当中的外层函数的局部变量
example1()
```
说明:
　　其实闭包函数相对与普通函数会多出一个__closure__的属性，里面定义了一个元组用于存放所有的cell对象，每个cell对象一一**保存了这个闭包中所有的外部变量**。
# 迭代器与生成器
　　[迭代器 Iterator与生成器Generator，从dict.keys()说起](https://blog.csdn.net/Bismarckczy/article/details/80617531)
## 基本概念
1. **迭代**是是访问集合元素的**一种方式**。
2. **迭代器**是一个可以记住遍历的位置的**对象**。记住是一个对象,**迭代器只是迭代的一种方式,这各个要搞清楚.**
3. 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器**只能往前不会后退**。
4. 迭代器有两个基本的方法：**iter() 和 next()。**,
5. **字符串，列表或元组对象**都可用于**创建迭代器**：
## 原因
　　可迭代对象--list,tuple,dict,字符串,set这些都是**可迭代的对象**,因为她们都实现了`__iter__ ()`方法.
　　迭代器--不仅实现了`__iter__ ()`,而且实现了 next()方法的**对象**,这个next方法在深度学习进行批量读取数据的时候很有用,因为list,tuple,dict,字符串,set可能存储的数据量会非常大,因此将其转换成迭代器,就可以使用next()方法,进行批量读取,减少内存压力.例如用数组存取一个图片--:假设有5000张图片，一种比较笨拙的读取方法是，一次性将所有图片读入到一个数组中，这个数组大小可能是[5000, 128,128,3],数据量很大.
　　迭代器的出现,**本质上为了减少内存的压力(通过next()方法)**,
　　可迭代对象可以通过`iter(可迭代对象)`转换为迭代器,从而拥有`next(迭代器)`方法,方法如下:
```
>>> a={3:4,5:6}
>>> x=iter(a)
>>> next(x)
3
>>> next(x)
5
```
　　因为**迭代器都拥有__iter()__ 和next方法,并且可以在for当中的遍历(重点)**,因此当我们自定义类的时候,需要定义 __iter() __和next方法,很麻烦,这时候我们就可以使用yield这个关键字进行**生成迭代器---由生成器返回生成的**,此时**yield会暂停并保存ield所在函数当前所有的运行信息**， 然后通过yield返回当前函数的值, 并在下一次执行 next() 方法时,**当前函数还是会从当前位置继续运行**.也就是后面所说的生成器.具体代码如下:
```
#!/usr/bin/python3
import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        #保存当前函数的运行状态,之后返回当前的值,当使用next()方法时,
        #当前函数会继续从上次保存的状态执行
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
```
结果:
```
0 1 1 2 3 5 8 13 21 34 55
```
## 迭代器在for当中的遍历
```
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
```
## 迭代器在类中的构建
　　主要应用,是在对数据进行读取,因此我们可以**构建一个类,构建一个自定义的迭代器**:
　　那么创建一个返回数字的迭代器，初始值为 1，逐步递增 1：在 20 次迭代后停止执行,**返回StopIteration---也就迭代结束的标志--至于何时结束**,可以自定义：
```
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)
```
## 生成器的应用场景
生成器的应用场景,主要是:
　　1. 当一个函数的**返回值很大**时,我们就可以逐个时刻对其进行读取.这样就能**节省内存,**--基于性能的考虑
 或者
　　1. 我们**需要函数在某个阶段时刻的值**,之后**对其进行判断**,并做出相应的操作.
# 装饰器
## 概念
[Python 函数装饰器](https://www.runoob.com/w3cnote/python-func-decorators.html)
　　装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。**插入日志、性能测试、事务处理、缓存、权限校验**等场景。
装饰器的说明:
　　(1)减少核心代码改动风险,增强扩展性.核心代码改动风险较大;
        (2)减少代码冗余,提高代码复用率.
## 原因:
函数的地址可以被复用
## 例子
```
from functools import wraps
# 业务方法装饰器
def serviceDecorate(level):
    def decoratoring(func):  # -->1
        @wraps(func)
        # 当不知道有多少个函数的时候才会用这个,平常需要进行函数嵌套的时候会指定对应的参数
        # def Wrapper(*args,**kwargs):
        def Wrapper(x, y):
            # (1)这个判断放在Wrapper之前,之后都可以,哪个简洁用哪个
            if (level == "time"):
                # 借助functools.wraps将(wraps也是一种装饰器:帮助传入函数的元信息:(函数名,文档注释:参数,及其输出,函数描述))
                # 实验证明,不用functools.wraps也行
                print("打印函数名称:")
                print(func.__name__)
                print("打印文档注释:")
                print(func.__doc__)
                # 一般就会在这里对输入的参数进行加工,之后处理之后的参数变为func的参数
                # 这就是实现了装饰器的作用
                x = x + y
                y = x
                # 一般最后是返回被装饰函数,其实就是嵌套函数的升级版.参数只能多,不能少
                return func(x, y)
                # return func(*args,**kwargs) #这个是最后一步
            elif (level == "percent"):
                x = y
                y = x + 1
                return func(x, y)
            else:
                x = y
                y = x + 2
                return func(x, y)
        return Wrapper  # 下一步是Wrapper
    # 如果加入业务装饰器,需要返回decoratoring,逐级返回-->向上看一行便知
    return decoratoring
```

```
# 相当于下面两行:
# beDecorated=serviceDecorate("time")(beDecorated)
@serviceDecorate(level="time")
def beDecorated(a, b):
    """
    被装饰函数
    :param a:
    :param b:
    :return:
    """
    print("进入被装饰函数:")
    c = a + b
    print(c)

@serviceDecorate(level="percent")
def beDecorated1(a, b):
    c = a * b
    print(c)
    return c

@serviceDecorate(level="money")
def beDecorated2(a, b):
    c = a * b
    print(c)
    return c
```

```
# 用类写装饰器并非什么特别的技巧，
# 一般情况下确实没必要这么写，不过这样就可以用一些类的特性来写装饰器，
class Foo(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, x, y):
        x = float(x)
        y = float(y)
@Foo
def beDecorated3(a, b):
    c = a // b
    print(c)
    return c


if __name__ == '__main__':
    # 把函数传入
    # 当执行beDecorated的时候,调用装饰器的时候,会自动进行
    beDecorated(2, 3)
    beDecorated1(2, 3)
    beDecorated2(2, 3)
    beDecorated3(2, 3)
```

# 数据结构
## 堆栈
　　使用append(末尾添加),使用pop()末尾排出,
```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
## 队列
　　末尾进队,前头出队---->效率不高,**因为前头元素出队,需要后面的元素往前移动**
```
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```
# 函数
## 返回多个值
**函数返回值多个值,可以是元组和list列表**,说明:下面式子**本质上还是返回一个值,返回一个list类型的值**
```
>>> def example(a,b):
...     return [a,b]
... 
>>> type(example(3,4))
<type 'list'>
```
下面这个才是返回多个值--tuple类型组成:
```
>>> type(example(3,4))
<type 'tuple'>
>>> def example(a,b):
...     return a,b
>>> type(example(3,4))
<type 'tuple'>
```
（１）不仅函数可以返回多个值,并且参数还可以拥有多个值,使用arg *来接收
（２）print(c不一定是 string类型，所以 用+ 号会出问题,因此会出现 加号.例子:`print("结果为"+c)`这个很容易出错
## 函数的参数
　　[Python之可变参数，*参数，**参数，以及传入*参数，进行解包](https://blog.csdn.net/cadi2011/article/details/84871401)
注意事项:
　　a .* 参数--将多个(一个及其以上)对象打包成tuple对象(（注意：就算传递一个元素，也会最终变为tuple）)--可传可不传,不传不报错.
　　b .** 参数--将多个(一个及其以上)对象打包成dict对象--也是可传可不传,不传不报错.
首先只要是可变参数（无名参数或者关键字参数），可以传0个参数，也可以传1个，同样也可以传多个
　　c、只要是可变参数（元组参数或者字典参数），一定要在普通参数（也称位置参数）的后面
　　d、`*`参数一定必须在`**`参数的前面（元组参数与字典参数同时存在时，元组参数一定在前）
```
#位置参数(普通参数),元组参数,字典参数(关键字参数)
#可变参数:元组参数,字典参数(关键字参数),参数的元素个数:0个及其以上
def printStr(参数，*参数，**参数):
    pass
```
例子如下:
```
def printStr(first,*tuple,**dict):
    print (str(first))
    print(tuple)
    print (dict)
    #不是print(\n)
    print("\n")
print(">>>first:")
printStr(100,200,name="zxp",age="24")
print(">>>second:")
# 注意没有**,但有*,但还是看成两个元素的tuple
printStr(100,(200,),{"name":"zxp","age":"24"})
print(">>>third:")
# 注意有 **,就能区分*与**对应的参数
printStr(100,200,**{"name":"zxp","age":"24"})
print(">>>fourth:")
print_dict={"name":"zxp","age":"24"}
printStr(100,200,**print_dict)
```
打印结果为 :
```
>>>first:
100
(200,)
{'name': 'zxp', 'age': '24'}
>>>second:
100
((200,), {'name': 'zxp', 'age': '24'})
{}
>>>third:
100
(200,)
{'name': 'zxp', 'age': '24'}
>>>fourth :
100
(200,)
{'name': 'zxp', 'age': '24'}
```
### 位置参数/必须参数
　　位置参数:对参数的位置比较敏感
### 默认参数
　　定义默认参数要牢记一点：默认参数必须指向不变对象！(字符串,或者其他的不变的 :**str、None**)
　　不变对象的好处,在多任务的情况下,不必加锁,因此只能读取,不能改变,因此我们劲量把对象设计成不变对象,
### 字典/关键字参数
　　**参数赋值的位置不要求**.因为 Python 解释器  能够  用参数名匹配参数值
　　(1)关键字参数允许函数调用时参数的顺序与声明时不一致，以下实例中演示了函数参数的使用不需要使用指定顺序,因为 Python 解释器  能够  用参数名匹配参数值。
```
#!/usr/bin/python3 
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
#调用printinfo函数
printinfo( age=50, name="runoob" )
```
　　(2)如果单独出现星号 * 后的参数必须用关键字传入。因为*代表是可变参数,
```
>>> def f(a,b,*,c):
...     return a+b+c
>>> f(1,2,3)   # 报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
>>> f(1,2,c=3) # 正常
6
```
### 参数组合
　　**必选/位置参数(a,c)、默认参数、元组/可变参数、字典/关键字参数**,--**重点**
`def func(a,c,b=0,*arg,**kw):`
初始化为:
`func(1,2,b=8,*(2,), **{"xx":"xx"})`--**标准形式**
　　可变参数--用于表单填写的的可选项
 　　虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
## 匿名函数/lambda函数
 函数名.__doc__ 的方式来显示函数的说明文档
1. lambda 只是一个表达式，函数体比 def 简单很多。
2. lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装**有限的逻辑**进去。
3. lambda **函数拥有自己的命名空间**，且**不能**访问自**己参数列表之外**或**全局命名空间里的参数**。
4. 虽然**lambda函数看起来只能写一行**，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
5. lambda表达式:
`lambda [arg1 [,arg2,.....argn]]:expression`
`middle_result_l=sorted(middle_result_l, key=lambda s:s[0],reverse=True)`
6. 可写函数说明
```
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print (sum( 10, 20 ))
print (sum( 20, 20 ))
>>> g= lambda x=0,y=0 : x**2+y**2
>>> g(2,3)
13
>>> g(2)
4
>>> g(y=3)
9
```
## return语句
　　return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式
## 数学函数
abs(x):绝对值函数
ceil(x):向上取整
(x>y)-(x<y)
fabs(x) 返回值的是浮点数的绝对值
round(x,保留小数点的个数).除非对精确度没什么要求，否则尽量避开用round()函数,向上取整,向下取整都有对应的函数--Decimal 数据类型用于浮点数计算，拥有更高的精度

| 函数                                                         | 返回值 ( 描述 )                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [abs(x)](https://www.runoob.com/python3/python3-func-number-abs.html) | 返回数字的绝对值，如abs(-10) 返回 10                         |
| [ceil(x)](https://www.runoob.com/python3/python3-func-number-ceil.html) | 返回数字的上入整数，如math.ceil(4.1) 返回 5                  |
| cmp(x, y)                                                    | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 **Python 3 已废弃，使用 (x>y)-(x<y) 替换**。 |
| [exp(x)](https://www.runoob.com/python3/python3-func-number-exp.html) | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045         |
| [fabs(x)](https://www.runoob.com/python3/python3-func-number-fabs.html) | 返回数字的绝对值，如math.fabs(-10) 返回10.0                  |
| [floor(x)](https://www.runoob.com/python3/python3-func-number-floor.html) | 返回数字的下舍整数，如math.floor(4.9)返回 4                  |
| [log(x)](https://www.runoob.com/python3/python3-func-number-log.html) | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0            |
| [log10(x)](https://www.runoob.com/python3/python3-func-number-log10.html) | 返回以10为基数的x的对数，如math.log10(100)返回 2.0           |
| [max(x1, x2,...)](https://www.runoob.com/python3/python3-func-number-max.html) | 返回给定参数的最大值，参数可以为序列。                       |
| [min(x1, x2,...)](https://www.runoob.com/python3/python3-func-number-min.html) | 返回给定参数的最小值，参数可以为序列。                       |
| [modf(x)](https://www.runoob.com/python3/python3-func-number-modf.html) | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 |
| [pow(x, y)](https://www.runoob.com/python3/python3-func-number-pow.html) | x**y 运算后的值。                                            |
| [round(x [,n\])](https://www.runoob.com/python3/python3-func-number-round.html) | 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。 |
| [sqrt(x)](https://www.runoob.com/python3/python3-func-number-sqrt.html) | 返回数字x的平方根。                                          |

### 随机数函数
1. choice(seq):从序列随机选择一个元素,seq=range(10)
2. random()随机生成一个**[0,1)的实数**(左闭右开)
3. shuffle(seq)—将有序序列打乱
4. uniform(x,y)—在**[x,y]**区间生成下一个实数---这也就是为什么我们**不用uniform(0,1)生成概率,因为都是闭区间**

| 函数                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [choice(seq)](https://www.runoob.com/python3/python3-func-number-choice.html) | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
| [randrange ([start,\] stop [,step])](https://www.runoob.com/python3/python3-func-number-randrange.html) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1 |
| [random()](https://www.runoob.com/python3/python3-func-number-random.html) | 随机生成下一个实数，它在[0,1)范围内。                        |
| [seed([x\])](https://www.runoob.com/python3/python3-func-number-seed.html) | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
| [shuffle(lst)](https://www.runoob.com/python3/python3-func-number-shuffle.html) | 将序列的所有元素随机排序                                     |
| [uniform(x, y)](https://www.runoob.com/python3/python3-func-number-uniform.html) | 随机生成下一个实数，它在[x,y]范围内。                        |

### 数学常量
pi-圆周率
e-自然数
### 注意
1. 一个变量可以通过赋值指向**不同类型**的对象。
2. 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
3. 在混合计算时，Python会把整型转换成为浮点数。
4. Decimal 数据类型用于浮点数计算，拥有更高的精度
5. 复数转换为实数:
```
>>> a = 4.1+0.3j
>>> a
(4.1+0.3j)
>>> a.real
4.1
>>> a.imag
0.3
```
6. Franction提供分数类型的支持:Fraction(分子,分母),分母不为0
```
from fractions import Fraction
>>> x=Fraction(1,3)
>>> y=Fraction(4,6)
>>> x+y
Fraction(1, 1)
```
7. str转换为list(注意是拆分转换),要实现整体转换:新建list,采用append/extend
```
>>> var='1234'
>>> list(var)
['1', '2', '3', '4']
```
## 常用函数
### print函数当中的end,file
　　python2是叫print语句
　　python3当中把其变为print函数了,其中print参数当中有end这个属性,默认是'\n',因此我们在进行直接输出print函数的时候,输出完之后,总会换行.
# 变量作用域
```
L （Local） 局部作用域
E （Enclosing） 闭包函数的外层函数,
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
以 L –> E –> G –>B 的规则查找
```
内置作用域的查看:
```
import builtin
dir(builtin)  #查看好多作用域
```
### 各种函数的作用域
1. 普通函数:按照LEGB方式进行,局部找不到，在函数执行过程中查找变量的顺序是一层一层向外找，再找不到就会去全局找，再者去内置中找。
2. 闭包函数,截止(包含)到E （Enclosing） 闭包函数的外层函数这个阶段.
### 产生新变量作用域的场景
　　(1)产生新的变量作用域:模块(module),类(class)以及函数(def,lambda),也就是说,在此范围产生的变量只能在对应的范围内进行使用,不能被外部使用.代码如下:
如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
```
>>> def test():
...     msg_inner = 'I am from Runoob'
... 
>>> msg_inner
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'msg_inner' is not defined
```
　　从报错的信息上看，说明了 msg_inner 未定义，无法使用，因为它是局部变量，只有在函数内可以使用。
　　(2)不产生新的作用域: `if/elif/else/、try/except、for/while`.--条件循环语句,也就是说这些语句内定义的变量，外部也可以访问，如下代码：
```
>>> if True:
...  msg = 'I am from Runoob'
... 
>>> msg
'I am from Runoob'
```
和
![](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190505150725.png)
实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
### 局部变量与全局变量
(1)典型错误
　　下面式子会报错:因为在进行执行的时候,没有将全局变量a传入进去(最好明确传入变量),就会导致引用之前没有分配.这个是我们常常会犯的一个错误:**以为是全局变量,没有必要在函数的参数中进行明确引入**.实际上这就会导致参数中对应的变量就是局部变量并且没有进行初始化定义.--报错`Unbound-LocalError`
```
a = 10
def test():
    a = a + 1
    print(a)
test()
```
下面这个式子就不会报错,**因为有明确将全局变量,作为函数参数,**
```
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)
```
(2)修改全局变量
```
x=10
def gd():
    global x
    x+=1
    return x
print(gd())
print(x)
```
输出:11,11
　　global 关键字会跳过中间层直接将嵌套作用域内的局部变量变为全局变量:
```
num = 20
def outer():
    num = 10
    def inner():
        global num
        print (num)
        num = 100
        print (num)
    inner()
    print(num)
outer()
print (num)
```
结果为:
```
20
100
10
100
```
# 模块
　　一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
## import
1. 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
2. import 模块1.子模块1
3. 最后导入的一定是模块(文件)
4. 文件夹当中含有__init__.py 的文件夹才会被认作是一个包
5. ` from sound.effects import *`,自定义导入需要的sound.effects包下的子模块/文件.那么我们可以在sound.effects包下的__init__.py 添加如下代码:
```
__all__ = ["echo", "surround", "reverse"]
```
即可,此时就会导入对应的子模块
## from...import name/*
　　**`from...import`最后导入的可以是子模块,函数,全局变量.但是import 方式最后导入的是子模块(子文件).**
　　Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，
```
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，
```
　　把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
```
from modname import *
```
　　这个可以一次性的把模块中的所有（函数，变量）名称
　　除非是你要导入的子模块有可能和其他包的子模块重名--全局变量(原先在同一文件编辑的函数,便于调用,减少修改)。因为系统会优先使用导入的**模块变量和函数**
## __name__ 与 __main__ 
　　每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
　　说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格

## dir() 函数
　　内置的函数 dir() 可以找到模块内定义的所有名称.以一个字符串列表的形式返回:
```
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
```
　　dir() # 得到一个当前模块中定义的属性列表
　　如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
```
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir() # 得到一个当前模块中定义的属性列表
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
>>> a = 5 # 建立一个新的变量 'a'
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'sys']
>>>
```
## python提示符
`>>>`->提示符
'... '--<副提示符
```
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Runoob!')
Runoob!
C>
```
# 正则表达式
## 要点
`\A,\Z,\b,\B,\d,\D,\s,\S,\w.\W` 用法
`<?=>,<?!>`
`re.sub 那个用法`
`^[] [^]`
`^$`
## 一般步骤
　　使用re的一般步骤是先使用re.compile()函数，将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。
　　compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。**该对象拥有一系列方法用于正则表达式匹配和替换。**
## 基本函数
### re.match
re.match(pattern,string,flags=0)
 .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
```
#!/usr/bin/python3
import re
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
```
以上实例执行结果如下：
```
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```

`AttributeError: 'NoneType' object has no attribute 'group'`,说明没有匹配成功,也就是`re.match()`的值为`None`,因此会报错,一般会报错的函数,其函数值不要作为if判断语句,我们可以使用`re.match()`,因为其值不报错,最坏就是None
### re.search
re.search 扫描**整个字符串**并**返回第一个成功的匹配**。
函数语法：`re.search(pattern, string, flags=0)`
```
print(re.search('com', 'www.runoob.com.com').group(0)) 
com
```
### re.match与re.search的区别
　　re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
```
#!/usr/bin/python3
import re
line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
```
结果为:
```
No match!!
search --> matchObj.group() :  dogs
```
除非match当中的正则匹配了含有通配符的正则
### re.sub替换
`re.sub(pattern, repl, string, count=0)`,参数如下:
```
pattern : 正则中的模式字符串。--模式--条件
repl : replace简写,替换的字符串，也可为一个函数。--new
string : 要被查找替换的原始字符串。--在string中
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
```
具体例子:
```
import re
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
 # 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
```
结果:
```
电话号码 :  2004-959-559 
电话号码 :  2004959559
```
### re.compile
　　compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，**供 match() 和 search() 这两个函数使用**,该对象有自己的调用match,search函数的形式,用例如下:
```
>>>import re
>>> pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
>>> m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
>>> print m
None
>>> m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
>>> print m                                         # 返回一个 Match 对象
<_sre.SRE_Match object at 0x10a42aac0>
>>> m.group(0) /m.groups() /m.group() # **可省略 0** 
'12'
>>> m.start(0)   # 可省略 0
3
>>> m.end(0)     # 可省略 0,这就是为什么在函数中可以省略的原因,索引返回的是字符在整个字符串的位置
5
>>> m.span(0)    # 可省略 0
(3, 5)
```
在上面，当匹配成功时返回一个 Match 对象，其中：
　　group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
　　start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），**参数默认值为 0**；---**整个匹配到的字符串**的初始位置
　　end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
　　span([group]) 方法返回 (start(group), end(group))
下面一个例子
```
>>>import re
>>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
>>> m = pattern.match('Hello World Wide Web')
>>> print m                               # 匹配成功，返回一个 Match 对象
<_sre.SRE_Match object at 0x10bea83e8>
>>> m.group(0)                            # 返回匹配成功的整个子串
'Hello World'
>>> m.span(0)                             # 返回匹配成功的整个子串的索引
(0, 11)
>>> m.group(1)                            # 返回第一个分组匹配成功的子串
'Hello'
>>> m.span(1)                             # 返回第一个分组匹配成功的子串的索引
(0, 5)
>>> m.group(2)                            # 返回第二个分组匹配成功的子串
'World'
>>> m.span(2)                             # 返回第二个分组匹配成功的子串索引
(6, 11)
>>> m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
('Hello', 'World')
>>> m.group(3)                            # 不存在第三个分组
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
```
### group()与groups()
一个是返回str,一个返回tuple
```
import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
m.groups()
Out[14]: ('Hello', 'World')
m.group()
Out[15]: 'Hello World'
type(m.group())
Out[16]: str
type(m.groups())
Out[17]: tuple
```
### re.findall
　　在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
　　注意： **match 和 search 是匹配一次符合要求, findall 匹配所有符合要求的。**
语法格式为：
`findall(string[, pos[, endpos]])`
参数：
```
string 待匹配的字符串。
pos 可选参数，指定字符串的起始位置，默认为 0(也就是开头)。---开始位置
endpos 可选参数，指定字符串的结束位置，默认为字符串的长度---结束位置
```
### re.finditer
　　和 findall 类似，在字符串中找到正则表达式所匹配的**所有子串**，并把它们**作为一个迭代器**--findall返回的是一个列表返回。例子如下:
```
import re
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
print(it)
12
32
43
3
<callable_iterator object at 0x110016940>
```
### re.split
　　split 方法按照能够匹配的子串将字符串分割后**返回列表**--不保留分隔符，它的使用形式如下：
```
re.split(pattern, string[, maxsplit=0, flags=0])
```
　　maxsplit是分割次数,默认是0,说明是无限制.
```
>>> re.split('\W+', ' runoob, runoob, runoob.', 1) 
['', 'runoob, runoob, runoob.']
>>> re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割(重要)
['hello world']
```
## 正则表达式对象
　　re.RegexObject-->正则表达式对象--re.compile生成,其可以使用match,findall方法
　　re.MatchObject-->匹配表达式对象--re.match生成
```
* group() 返回被 RE 匹配的字符串。
* start() 返回匹配开始的位置
* end() 返回匹配结束的位置
* span() 返回一个元组包含匹配 (开始,结束) 的位置
```
## 修饰符--可选
```
re.I     -->insensitive ignoreCase:不敏感  大小写不敏感 
re.M  -->multiline  多行匹配,影响 ^ 和 $  re.MULTILINE
re.S  -->String  使得通配符 .  匹配包括换行符所有的字符
re.L -->当前的语言设置
re.U  -->Unicode  根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
```
相对应：
```
Locale：本地化的，某个具体的地区的；
Unicode：全球通用的，统一的；
```
如果添加了re.LOCALE这个标志，则：`\w,\W,\b,\B,\s,\S`的含义，和具体的locale相关
## 模式符
### 注意事项
　　字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串
**标点符号只有被转义**时才匹配自身(例如.,)，否则它们表示特殊的含义
　　反斜杠本身需要使用反斜杠转义。
　　**由于正则表达式通常都包含反斜杠**，所以你最好使用**原始字符串**来表示它们。模式元素(如** r'\t'，等价于 \\t **)匹配相应的特殊字符
　　`re *` 就是代表类似\d* ,\d就是属于re
　`（aa| bb）`	匹配aa或bb**(有括号就没有拆分)**
　　`(re)`匹配括号内的表达式，也表示一个组
　　`[amk] `匹配 'a'，'m'或'k
　　`o{2,}`不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o**。**"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。** 普通字符也可以加上匹配长度
　　`\s`	匹配任意空白字符，等价于 [\t\n\r\f]。
　　`\S`	匹配任意非空字符
　　`\d`	匹配任意数字，等价于 [0-9]。
　　`\D`	匹配任意非数字

| ^            | 匹配字符串的开头(就是限定了提取的内容)                       |
| ------------ | ------------------------------------------------------------ |
| $            | 匹配字符串的**末尾****。(就是限定了提取的内容)**             |
| .            | 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。 |
| [...]        | 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'          |
| [^...]       | 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。             |
| re*          | 匹配0个或多个的表达式。                                      |
| re+          | 匹配1个或多个的表达式。                                      |
| re?          | 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式         |
| re{ n}       | 匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。 |
| re{ n,}      | 精确匹配n个前面表达式。例如，**"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o**。**"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。** |
| re{ n, m}    | 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式         |
| a\| b        | 匹配a或b                                                     |
| (re)         | 匹配括号内的表达式，也表示一个组                             |
| (?imx)       | 正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。 |
| (?-imx)      | 正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。     |
| (?: re)      | 类似 (...), 但是不表示一个组                                 |
| (?imx: re)   | 在括号中使用i, m, 或 x 可选标志                              |
| (?-imx: re)  | 在括号中不使用i, m, 或 x 可选标志                            |
| (?#...)      | 注释.                                                        |
| (?= re)      | 前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。 |
| (?! re)      | 前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。 |
| (?> re)      | 匹配的独立模式，省去回溯。                                   |
| \w           | 匹配数字字母下划线                                           |
| \W           | 匹配非数字字母下划线                                         |
| \s           | 匹配任意空白字符，等价于 [\t\n\r\f]。                        |
| \S           | 匹配任意非空字符                                             |
| \d           | 匹配任意数字，等价于 [0-9]。                                 |
| \D           | 匹配任意非数字                                               |
| \A           | 匹配字符串开始(字母表从A开始)                                |
| \Z           | 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。 |
| \z           | 匹配字符串结束(字母表到z结束)                                |
| \G           | **匹配最后匹配完成的位置。**                                 |
| \b           | **匹配一个单词边界，也就是指单词和空格间的位置**。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。 |
| \B           | **匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'**，但不能匹配 "never" 中的 'er'。 |
| \n, \t, 等。 | 匹配一个换行符。匹配一个制表符, 等                           |

常用特殊字符串:
实例	描述
`.`匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]'  的模式。
`\d`	匹配一个数字字符。等价于 [0-9]。**decimal**
`\D`	匹配一个**非数字**字符。等价于 [^0-9]。
`\s	`匹配**任何空白**字符，包括空格、制表符、换页符等等。等价于 **[ \f\n\r\t\v]**。space
`\S	`匹配任何**非空白**字符。等价于 [^ \f\n\r\t\v]。
`\w`	匹配包括下划线的任何单词字符。等价于'**[A-Za-z0-9_]**'--普通字符下划线(中英文都可以)。特殊符号(标点符号之类的除外)例子如下:(重点)
```
re.findall('\w+',"现在")
Out[20]: ['现在']
re.findall('\w+',".现在")
Out[21]: ['现在']
re.findall('\w+',"=现在")
Out[22]: ['现在']
re.findall('\w+',"+现在")
Out[23]: ['现在']
re.findall('\w+',"(现在)")
Out[24]: ['现在']
```
`\W`	匹配任何**非单词字符**(其实就是匹配那些特殊符号)。等价于 '[^A-Za-z0-9_]'。
### (?<name>exp)
　　(?<name>exp) 匹配 exp,并捕获文本到名称为 name 的组里，也可以写成 (?'name'exp)。
　　**但是在Python中，为 (?P<name>exp)**--**这个要注意**,exp:expression  也就是为这个正则表达式命名,P就是Python 环境下的正则表达式。 简单例子：
```
import re
pattern = re.compile(r'(?P<here>[a-z]+) (?P<he>[a-z]+)', re.I)
m = pattern.match('Hello World word helo')
print (m.group('here'))
print (m.group(1))
print(m.group('he'))
print(m.group(2))
Hello
Hello
World
World
```
　　**命名组()是便于使用的**，可以**替代需要记住组的数字**，**可以进行扩展使用(调用匹配到的数据)**,因为默认获取每个组匹配的数据都是使用0,1,2,不好记,容易记错,其实组的作用就是,根据不同的需要,设置不同的组获取不同的值
### re.sub
　　re.sub 使用实例：改变日期的格式，如中国格式 2017-11-27 改为美国格式 11/27/2017:
```
>>> s = '2017-11-27'
>>> import re
>>> print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1', s))
11/27/2017
```
　　用 () 来划定原字符串的组，{} 中表示数字的个数，r 即后面的字符串为原始字符串，防止计算机将 \ 理解为转义字符，2，3，1 为输入的字符串三段的序号。
　　Macth**只会从开头哦你匹配**，如果**不是开头的字符串**，那么将不会匹配成功，而search**可以匹配任意位置**的字符串，会对整个匹配对象进行扫描，sub方法类似于字符串的replace方法，**sub是对所有匹配到的内容进行替换**，而不仅仅是替换第一个匹配到的对象(全部替换)--**很重要**
　　compile是将str类型的对象编译成re类型
### \b与\B
　　\B匹配非单词边界，跟\b相反
获得边界的变量
　　\b 的用法也可以很灵活，在给定的字符串中，找到以小写字母开头的单词和单词数量。
```
import re
s="i Am a gOod boy  baby!!"
result=re.findall(r'\b[a-z][a-zA-Z]*\b',s)
print(result)
print("小写字母开头的单词个数：",len(result))
```
　　\b 是指匹配一个单词边界，也就是指单词和空格间的位置。但事实上，\b 可以匹配的边界**包括单词和特殊字符边界**，比如 $，#… 等。
例如:
```
import re
re.findall(r"\boone"," oone oone")
Out[8]: ['oone', 'oone']
```
　　其实\b就是空格 ,`\boone`就是空格+oone的匹配,因此加起来就有两项符合
### \A与\Z的用法
```
re.findall(r"\Aoone.*\Z","oone oone")
Out[10]: ['oone oone']
input: "Google\nApple"           Regex: \AGoogle\nApple\z`  匹配到:` "Google\nApple"
```

## 注意
　　?=是零断言，配合?<和?>用的。？!是不包含
　　^从行开始处匹配，$从行结束处开始匹配。
　　\A从字符串开始处匹配，\Z从字符串结束处匹配
　　^[a-z] 匹配**不包含以小写字母 开头** 的文本串 
　[^a-z] 表示匹配**不包含 小写字母**的字符
　　这个叫断言，只匹配一个位置(?=.*[a-z])\d
比如，你想匹配一个“国”字，但是你只想匹配中国的国，不想匹配美国的国就可以用以下表达式:(?=中)国,括号里面是一个条件,外面是我们想要获取的结果,但是**这个表达式与其他通配符连用才能起到效果**
　　`(?=.*[a-z])\d+`:这个就表示 匹配以“任意长度( *代表0及其以上长度)字符连着一个小写字母”开头的数字，只匹配数字
   　　使用 `* `字符代替 ? 字符扩大了找到的文件的数量
    　`*`、`+`限定符都是贪婪的，因为它们会尽可能多的匹配文字，只有在它们的后面加上一个?就可以实现非贪婪或最小匹配。:通过在`*`、`+`或 `?` 限定符之后放置` ?`，该表达式从"贪心"表达式转换为"非贪心"表达式或者最小匹配
    　定位符:`^` 和 `$ `分别指字符串的开始与结束，`\b` 描述单词的前或后边界，`\B` 表示非单词边界,`\A,\Z`,单词边界是单词和空格之间的位置。非单词边界是任何其他位置
    　长度限定符:有 * 或 + 或 ? 或 {n} 或 {n,} 或 {n,m} 共6种
    　用圆括号将所有选择项括起来，相邻的选择项之间用|分隔。但用圆括号会有一个副作用，使相关的匹配会被缓存可以使用非捕获元字符,使用 ?:、?= 或 ?! 来重写捕获，忽略对相关匹配的保存
　　[.] 只会匹配 .字符，等价于 \.
    　x|y:匹配 x 或 y。例如，'z|food' 能匹配 "z" 或 "food"。'(z|f)ood' 则匹配 "zood" 或 "food"。
　　[xyz]:字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
　　[^xyz]:负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'。
## 运算符优先级
巧记式子:(\. \d+ [|])+
| 运算符                          | 描述                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| \                               | 转义符                                                       |
| (), (?:), (?=), []              | 圆括号和方括号                                               |
| *, +, ?, {n}, {n,}, {n,m}       | 限定符                                                       |
| ^, $, \任何**元字符**、任何字符 | 定位点和序列（即：位置和顺序）\d                             |
| \|                              | 替换，"或"操作 字符具有高于替换运算符的优先级，使得"m\|food"匹配"m"或"food"。若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m\|f)ood"。 |




## 匹配规则
### ^与$
　　`^once`:表示该模式只匹配那些以once开头的字符串,例如该模式与字符串"once upon a time"匹配，与"There once was a man from NewYork"不匹配。正如如^符号表示开头一样，**$符号用来匹配那些以给定模式结尾的字符串**
　　`bucket$`：这个模式与"Who kept all of this cash in a bucket"**匹配**，与"buckets"**不匹配**。字符 ^ 和 $ 同时使用时，**表示精确匹配（字符串与模式一样）**
　　`^bucket$`:只匹配字符串"bucket"。如果一个模式不包括^和$，那么它与任何包含该模式的字符串匹配检测一个字符串是否以制表符开头，可以用这个模式：`^\t `,用\n表示"新行"，\r表示回车。其他的特殊符号，可以用在前面加上反斜杠，如反斜杠本身用\\表示，句号.用\.表示，以此类推。
### (),[],{}
　　()-->表示要提取的内容,里面装的是一个表达式--表示的是一组
　　[]-->匹配的模式:[aa|bb]  :需要匹配aa或者bb,如果没有长度符号,说明至少要匹配
　　{}-->{}表示匹配的长度,{1:3}-->说明至少一次,至多三次,除了这种方式还可以为:`?`,`*`,`+`,{n,m}可以灵活使用，它表示匹配n次到m次
　　因此一般式子为:(固定字符[]){}或者([])?/ * /+或者(表达式)
　　如果没有(),说明整个是表达式
　　至于**其他的\d之类的只是表达式**,(0-9)只是说明匹配0-9的任意数字,因为没有说明匹配长度,加上要根据不同的匹配函数,得到不同的匹配个数
### []与\
　　比如"z2"、"t6"或"g7"，但不是"ab2"、"r2d3" 或"b52"的话，用这个模式：`^[a-z][0-9]$`  ^表示字符串的开头，但它还有另外一个含义。当在一组方括号里使用 ^ 时，它表示"非"或"排除"的意思，常常用来剔除某个字符
```
[^a-z] //除了小写字母以外的所有字符 
[^\\\/\^] //除了(\)(/)(^)之外的所有字符 
[^\"\'] //除了双引号(")和单引号(')之外的所有字符
特殊字符 .(点，句号)在正则表达式中用来表示除了"新行"之外的所有字符
```
综合:
```
^[-]?[0-9]+\.?[0-9]+$   // 所有的浮点数
```
　　最后一个例子不太好理解，是吗？这么看吧：以一个可选的负号 ([-]?) 开头 (^)、跟着1个或更多的数字([0-9]+)、和一个小数点(\.)再跟上1个或多个数字([0-9]+)，并且后面没有其他任何东西($)-因为$前面没有通配符了:例如
```
^[-]?[0-9]+(\.[0-9]+)?$ // 所有的浮点数
```
　　`/a/  /7/  /M/ ` :可以将许多单字符组合起来以形成大的表达式。例如，以下正则表达式组合了单字符表达式：`a`、`7` 和 `M`。[a7M]表示的是匹配`a`、`7` 和 `M`中的任意字符
　　下面的正则表达式匹配 aac、abc、acc、adc 等等，以及 a1c、a2c、a-c 和 a#c：a.c,其中. 没有说明匹配长度,我们默认将其匹配长度设置为1
　　字符簇:类似a-z A-Z 0-9之类(开始字符+连字符+结束字符)
### 连字符
　　若要使用范围代替字符本身来表示匹配字符组，请使用连字符 (-) 将范围中的**开始字符和结束字符**分开
　　下面的正则表达式匹配1、2、3、4 或 5 之外的任何数字和字符：`Chapter [^12345]`-->`Chapter [^1-5]`
### []--本质上就是一个匹配
**本质上返回[]中已经存在的自己,**
### ()的目的---匹配+替换(重点)
　　()-->先根据式子进行匹配,之后将匹配的式子装进(),进行保存.
举个例子如下:
`/^Chapter|Section [1-9][0-9]{0,1}$/`
　　很遗憾，上面的正则表达式要么匹配行首的单词 Chapter，要么匹配行尾的单词 Section 及跟在其后的任何数字。如果输入字符串是 Chapter 22，那么上面的表达式只匹配单词 Chapter。如果输入字符串是 `Section 22`，那么该表达式匹配 `Section 22`。
　　`^(Chapter|Section) [1-9][0-9]{0,1}$`
重点:
　　为了便于使正则表达式**更易于控制**，
　　可以使用括号来**限制替换的范围**，即，**确保它只应用于两个单词 Chapter 和 Section**。
　　括号也用于**创建子表达式**，并且**捕获它们以供以后使用**
　　尽管这些表达式正常工作，但 Chapter|Section 周围的括号还将捕获两个匹配字中的任一个供以后使用。由于在上面的表达式中**只有一组括号**，因此，只有一个被捕获的"**子匹配项"**,同时会进行保存--因为对部分模式或者全部模式添加圆括号将导致相关匹配存储到一个临时缓冲区中,匹配顺序是从左到右进行匹配,最多可存储 99 个捕获的子表达式,缓冲区的编号是从1开始,0是全部匹配项,(索引号可以作为很多方法的参数:group(1),start(1),end(1)之类的),每个缓冲区都可以使用 \n 访问，其中 n 为一个标识特定缓冲区的一位或两位十进制数,也就是之前re.sub的参数情况.
  ```
  >>> s = '2017-11-27'
>>> import re
>>> print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1', s))
11/27/2017
>>> 
  ```
　　 `\2`->\n的一种具体情况,就是第二个子匹配项的内容也就是(\d{2})匹配到的内容.具体参考函数:
 `def sub(pattern, repl, string, count=0, flags=0):`
 　　re.sub("匹配模式",匹配到的内容作为替换,需要替换的问文本,替换的次数,匹配的方式)
  　　因此在对进行很大文本进行匹配的时候,缓存内存数量有限.因此我们使用(?!,?:?=)三种方式不获取捕捉位置(也就是不将匹配到的内容送到缓存区当中)
  ![?:](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190515012659.png)
  　　open the qq”，“open qq”。“qq”是我想要得到的内容˙,使用如下式子:
  `open (?:the)? ([A-Za-z]+[0-9]*) `
  　　当我输入是“open qq”的时候，实际上中间只有一个空格字符，所以是无法与正则匹配的。然后我就把第二个空格改成了“\s?”,这次完整的正则就是 
`open (?:the)?\s?([A-Za-z]+[0-9]*)`因此我们需要对匹配到的子匹配项进行
### 匹配不包含
^((?!不包含的字符串|不包含的字符串).)+$
date_exception_pattern=r"^((?!万元|元).)+$"
?!则是-->不是的含义.
## 断言正则表达式
###  ?= ?! ?:
　　其实上面几个式子就是作为查找某个内容的条件(有符合条件和不符合条件的情况),只不过**查找之后的内容保留有区别.**--不同的?Pattern使用的位置需要记牢
　　?!pattern:若字符串**符合 pattern 则将其过滤掉**。在分析日志时很有用，例如想过滤掉包含 info 标记的日志可以写 ^(?!.*info).*$。--过滤条件
　　?=pattern:
　　(?:pattern):这条规则主要是为了优化性能，对匹配没有影响。对匹配到的内容不会送入缓存区,它表示括号内的子表达式匹配的结果不需要返回.
　　**re.findall,finditer,match都支持序号访问,只不过形式不一样**
### (?:pattern):**保留式子**
(?:pattern):例子如下:(重点)
```
#我们明显看到(?:98|95|97)的匹配内容没有保留,因为(window)是(pattern),而(?:Pattern)匹配到的内容不会保存
re.findall("(window)(?:98|95|97)","98window window98 window95 window97")
#我们可以看到,(?:98|95|97)被作为一个条件:匹配后面为98|95|97-->记住是(),不是[],任意数值的window.符合条件,但是window没有被框起来
Out[38]: ['window', 'window', 'window']
re.findall("window(?:98|95|97)","98window window98 window95 window97")
Out[39]: ['window98', 'window95', 'window97']
```
　　(?:pattern)：匹 配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。**这在使用 “或” 字符 (|) 来组合一个模式的各个部分是很有用**。例如， ‘industr(?:y|ies) 就是一个比 ‘industry|industries’ 更简略的表达式。
### (?<=pattern)--前面
　　查找前面为98|95|97的window
```
re.findall("(?<=98|95|97)(window)","98window window98 window95 window97")
Out[37]: ['window']
```
### (?!pattern)--后面
　　查找后面不为|98|95|97的window,符合(?!pattern)的window将会剔除
```
re.findall("window(?!98|95|97)","98window window98 window95 window97")
Out[45]: ['window']
```
说明`98window`中的`window`符合
　　(?!pattern)：负向预查，在任何不匹配 pattern 的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如‘**Windows (?!95|98|NT|2000)’ 能匹配 “Windows 3.1〃 中的 “Windows”**，**但不能匹配 “Windows 2000〃 中的 “Windows”**。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始.
### (?=Pattern)--后面
　　查找后面为|98|95|97的window,我们可以看到有三个符合要求的window
```
re.findall("window(?=98|95|97)","98window window98 window95 window97")
Out[46]: ['window', 'window', 'window']
```
　　(?=pattern)：正 向预查，在任何匹配 pattern 的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，**该匹配不需要获取供以后使用**。例如，‘Windows (?=95|98|NT|2000)’ 能匹配 “Windows 2000〃 中的 “Windows” ，但不能匹配 “Windows 3.1〃 中的 “Windows”。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后**立即开始下一次匹配**的搜索--**也就是下一个()**，而不是从包含预查的字符之后开始。
  ```
  ^(?:Chapter|Section) [1-9][0-9]{0,1}$
  ```
  
##  资料
[正则表达式，^和$到底怎么用？](https://bbs.csdn.net/topics/391907864)
[正则表达式的()  {} ](https://www.cnblogs.com/richiewlq/p/7307581.html)
[正则表达式30分钟入门教程](http://deerchao.net/tutorials/regex/regex.htm)
[?:](https://blog.csdn.net/ledavince/article/details/80339009)
[正则表达式－－ (?:pattern)与(?=pattern)的区别](https://blog.csdn.net/u010506876/article/details/82837533)
[正则表达式中?=和?:和?!的理解](https://blog.csdn.net/csm0912/article/details/81206848)
# 多线程
## Python3 多线程
　　线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。
　　每个线程都有他自己的**一组CPU寄存器**(一组)，**称为线程的上下文**，该上下文反映了线程上次**运行该线程的CPU寄存器的状态**。
　　**指令指针和堆栈指针寄存器**是线程上下文中**两个最重要的寄存器**，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存.
## 线程模块
　　thread 模块已被废弃。用户可以使用 threading 模块代替。所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。
　　Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
　　_thread 提供了**低级别的、原始的线程**以及一个**简单的锁**，它相比于 threading 模块的功能还是比较有限的。threading 模块除了包含 _thread 模块中的所有方法外


## 产生线程的两种方式:
　　使用线程有两种方式：函数式或者**用类生成来包装线程对象**。
　　函数式：调用 _thread 模块中的start_new_thread()函数来产生新线程
　　类方法:使用 threading 模块创建线程
　　我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
函数式方法:_thread模块式子为:
`_thread.start_new_thread ( function, args[, kwargs] )`
```
function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数。
```
(1)函数式生成线程
```
#!/usr/bin/python3
import _thread
import time
# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")
while 1:
   pass
```
结果如下:
```
Thread-1: Wed Apr  6 11:36:31 2016
Thread-1: Wed Apr  6 11:36:33 2016
Thread-2: Wed Apr  6 11:36:33 2016
Thread-1: Wed Apr  6 11:36:35 2016
Thread-1: Wed Apr  6 11:36:37 2016
Thread-2: Wed Apr  6 11:36:37 2016
Thread-1: Wed Apr  6 11:36:39 2016
Thread-2: Wed Apr  6 11:36:41 2016
Thread-2: Wed Apr  6 11:36:45 2016
Thread-2: Wed Apr  6 11:36:49 2016
```
(2)类方法---threading模块(同步,队列)
```
#!/usr/bin/python3
import queue
import threading
import time
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)
        
def process_data(threadName, q):
    while not exitFlag:
     # 获取锁，用于线程同步
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            # 释放锁，开启下一个线程
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
        # 释放锁，开启下一个线程
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
```
# python异常处理
try..except Exception as e...else...finally
```
def checke_date(time_str):
    """
    递归检查日期格式,直至格式输入正确
    :param year:
    :param month:
    :param day:
    :return:
    """
    # print(type(datetime.datetime(year=year, month=month, day=day)))
    # (type(datetime.datetime(year=year, month=month, day=day)) == datetime.datetime)
    # 因为try语句是每次都会执行的语句,因此如果发生异常,甚至连print语句都会报错
    # 因此try语句中只用一个判断的语句即可(好好理解下),其他不会报错的句子
    try :
        time_l=re.findall("\d+",time_str)
        check_result_l = datetime.datetime(year=int(time_l[0]), month=int(time_l[1]), day=int(time_l[2]))
    # try语句执行的时候,出现错误,出发了异常,就会执行except语句
    # except 异常名称 as 变量 ,变量e是用来接收异常的,Exception表示可以接收任何异常
    except Exception as e:
        print(e)
        input_date_str = input("输入格式错误,重新输入正确的日期格式:")
        # 这个递归函数,执行期间,如果正常执行,还是会走try...else语句,这个注意
        # try语句还是执行不正常的话,会一直执行try...except语句,直至正常执行走try...else语句
        # 因此保险起见,即使在else语句有返回值,也添加return,因为函数中里面虽然有 return,但是只是返回值
        # 没有在本函数进行返回,只是得到了一个值
        return checke_date(input_date_str)
    # 这个是try语句执行正常时的语句,
    else:
        print(check_result_l)
        return check_result_l
    finally:
        # 无论try语句执行时,是否是错的还是对的,最后都会执行,
        # 前提是except中的语句要执行完,如果except语句是递归主函数的,
        # 那么就需要直至递归函数完成执行才会finally当中的句子.否则finally语句会被拦截,错误几次就会输出几次
        # 因此finally语句根据情况决定是否需要
        print("程序结束")
if __name__ == '__main__':
    c=checke_date("2019年2月22日")
    print(c)
```
## 用户自定义异常
　　单个异常类的时候（整个模块（不单单是一个文件）只会出现一种异常的时候）
　　你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:
```
>>>class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
   
>>> try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)
   
My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'oops!
```
## Python3 内置异常类型的结构:
```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```
# 类
## 概念
### init
　　实例化类 MyClass，对应的 __init__() 方法就会被调用:`x = MyClass()`
　　当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。例如
```
#!/usr/bin/python3
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
```
　　一般来说，realpart应该和self.realpart，这样就为对应的类定义对应的属性，实例化类的时候，通过属性来赋予。
### 类的方法
　　类**的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照**惯例它的名称是 self。
```
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()
以上实例执行结果为：
<__main__.Test instance at 0x100771878>
__main__.Test
```
　　从执行结果可以很明显的看出，**self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。（我们也可以看到调用方法的时候，如果只有self参数，不用写上self直接调用即可，self说明，该方法，可以用被类的实例调用。不一定要用self，其他名称也可以，相当于一个标记，self更好记而已）
　　self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的**:
```
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
t = Test()
t.prt()
以上实例执行结果为：
<__main__.Test instance at 0x100771878>
__main__.Test
```
## 多继承
　　`class DerivedClassName(Base1, Base2, Base3)`:需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，**从左到右查找父类中是否包含方法**。
```
print (counter.__secretCount)  # 报错，实例不能访问私有变量
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
```
```
#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
```
## 类的专有方法：
　　当用该类的实例进行运算的时候,自动调用该方法--也就是后买呢运算符重载
```
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
```
## 运算符/函数的重载
　　不能重载内置类型的运算符
　　不能新建运算符，只能重载现有的,某些运算符不能重载——is、and、or 和 not（不过位运算符&、| 和 ~ 可以）
　　以双下划线__开头的类函数在Python中称为特殊函数。 这是因为，它们是有特殊含义。 
```
# 结构化输出,
# 或者
# 对不同的数据进行比较的时候
# 会用到类
class Axis:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Point:
    # x = 0, y = 0是默认值,设置默认值不是必须的
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    # 实例自身self和传入的实例other--不一定是该类,但是有对应的属性,这样才能进行比较,
    # 使用第一个实例对应的类的比较方法
    # 类似__lt__是python的类中所使用的特殊函数,比较,格式化输出等会优先调用类里面的方法
    # __eq__对应==
    def __eq__(self, other):
        result=self.x==other.x
        return result
    def __lt__(self, other):
        result=self.y<other.y
        return result
    # 调用的时候--Point.toString(Point)
    def toString(self):
        str="{}-{}".format(self.x,self.y)
        return str
if __name__ == '__main__':
    p1=Point(3,3)
    p2=Axis(3,4)
    # 打印的是Point实例p1的内存地址:<__main__.Point object at 0x10b197a90>
    print(p1)
    # print(p1+p2)
    # p1<p2会优先调用类的自定义的比较方法---__lt__.
    print(p1<p2)
    # 调用类的结构化输出-Point.toString(Point实例名)
    print(Point.toString(p1))
```
[Python 函数如何实现“重载”](https://blog.csdn.net/weixin_43773093/article/details/88535763)
## 类方法,普通方法,静态方法
　　1. **静态方法**: 用 `@staticmethod` 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。---**只可以被类直接调用**
　　2. **普通方法**: 默认有个self参数(对象实例)，--且**只能被对象**调用。
　　3. 类方法: 默认有个** cls 参数**，可以被类和对象调用，需要加上 `@classmethod `装饰器。---**类和对象都可以直接调用**--类方法
```
class Classname:
    @staticmethod
    def fun():
        print('静态方法')
    @classmethod
    def a(cls):
        print('类方法')
     #普通方法
    def b(self):
        print('普通方法')
Classname.fun()
Classname.a()
C = Classname()
C.fun()
C.a()
C.b()
```
## __name__与__main__方法

　　当这个 pcRequests.py 作为模块被调用时，则它的 __name__ 就是它自己的名字：
`import pcRequestspcRequestsc=pcRequestsc.__name__`
结果：
```
'pcRequests'
```
　　看到这里应该能明白，自己的 `__name__` 在自己用时就是 `main`，当自己作为模块被调用时就是自己的名字
　　最新的 Python3.7 中(2018.07.13)，对类的构造函数进行了精简。
```
3.7 版本：
from dataclasses import dataclass
@dataclass
class A:
  x:int
  y:int
  def add(self):
    return self.x + self.y
```
相当于以前的：
```
class A:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def add(self):
    return self.x + self.y
```





