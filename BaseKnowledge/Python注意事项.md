# 注意
## replace
　　关于 string 的 replace 方法，需要注意 **replace 不会改变原 string 的内容**。
实例：
```
temp_str = 'this is a test'
b=temp_str.replace('is','IS')
print(b)
print(temp_str)
```
结果为：
```
thIS IS a test
this is a test
```
要使得其本身实现替换可以`temp_str=temp_str.replace('is','IS')`
sorted函数也是，最好是如下这样形式：
```
last_result_l=sorted(last_result_l, key=lambda s:s[0],reverse=True)
```
## 方法与函数
函数和方法的区别
1. 与类和实例无绑定关系的function都属于函数（function）；
2. 与类和实例有绑定关系的function都属于方法（method）
## continue与break
```
    for sentence in document_l:
        sentence_set=set(generator2List(sentence[2:]))
        # 求A,B列表之间的交集
        if(query_set&sentence_set):
            recall_result.append(sentence[0:2]+list(sentence_set))
        else:
            # 不存在交集，则进行for sentence in document_l的下一轮
            continue
            # 则进行 for sentence in document_l的下一轮，停止对for sentence in document_l的循环。停止离其最近的一个循环
            break 
```
## sort与sorted
　　sorted(L)**不改变原始的数据**，适用于**任何可迭代容器**，**有返回值**；
　　list.sort()仅支持list（sort（）本身就是list的一个方法）,因此仅支持list，会改变list本身数据，没有返回值。
　　`a=sorted(a,key=lambda x:(条件a，条件b))`
[list中的sort()方法](https://www.cnblogs.com/dyl01/p/8563550.html)

## 进制
**2** 进制是以 **0b** 开头的: 例如: 0b11 则表示十进制的 3---bin（）
**8** 进制是以 **0o** 开头的: 例如: 0o11 则表示十进制的 9—oct（）
**16** 进制是以 **0x** 开头的: 例如: 0x11 则表示十进制的 17--hex（）
## sum(x,y)
sum(x,y)需要x是序列,y是相加之后,再加上几-->不是单个元素;
`c = sum([2], 1)`
## remove,pop,del
|          | remove                                              | pop                                                 | del                |
| -------- | --------------------------------------------------- | --------------------------------------------------- | ------------------ |
| 形式     | list.remove(值)                                     | list.pop(索引)/list.pop()                           | del(索引)          |
| 功能     | 删除的是首个符合要求的值(如果有多个,则需要进行循环) | 根据索引删除列表中的元素,入无指定则删除列表末尾元素 | 删除指定索引的元素 |
| 返回结果 | 删除后的列表                                        | 被删除的值(适用于使用之后进行删除)                  | 删除后的列表       |

## 各个进制的符号
%o 八进制 oct
%d 十进制 dec
%x 十六进制 hex。
## 多个and,每个判别条件(有顺序的)
每个判别条件,最好使用if,然后输出相应的判断结果,或者错误结果
## python 一个key映射多个值
　　[Python3 - 字典中的键映射多个值](https://www.jianshu.com/p/b2edfa790a11)
## 文件路径编写
`save_path = './upload_data/'`--存储在文件夹,末尾的'/'一定不能少;
