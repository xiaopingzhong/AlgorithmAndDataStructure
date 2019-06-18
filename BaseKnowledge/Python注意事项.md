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
`file_path = "/Volumes/软件/OCR数据集/弱标注大规模街景文字识别竞赛LSVT/train/train_gt/" + "{}".format(x) + ".txt"`
没有加上`\`,就说明只会存储在`/Volumes/软件/OCR数据集/弱标注大规模街景文字识别竞赛LSVT/train`的目录下.具体如图下:
![保存路径](https://blog-1-1256491104.cos.ap-chengdu.myqcloud.com/20190531103422.png)
# 终端执行 sudo 命令提示无法解析主机
![终端执行 sudo 命令提示无法解析主机](https://www.jianshu.com/p/2c71408bbe1c)
　主机名就是@后面的名字
# UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in position 3131: ordinal not in range(128)
以rb的模式进行读写
# tensorflow.python.framework.errors_impl.InternalError: Failed to create session.
程序太多，杀除即可
# 加载预训练模型出错
Data loss: not an sstable (bad magic number): perhaps your file is in a diff
```
variable_restore_op = slim.assign_from_checkpoint_fn(FLAGS.pretrained_model_path,
                                                             slim.get_trainable_variables(),
                                                             ignore_missing_vars=False)
```
## ignore_missing_vars
   ignore_missing_vars 非常重要，一定要将其设置为 True，也就是说，一定要忽略那些在定义的模型结构中可能存在的而在预训练模型中没有的变量，因为如果自己定义的模型结构中存在一个参数，而这些参数在预训练模型文件 xxx.ckpt 中没有，那么如果不忽略的话，就会导入失败（这样的变量很多，比如卷积层的偏置项 bias，一般预训练模型中没有，所以需要忽略，即使用默认的零初始化）。最后一个参数 reshape_variabels 指定对某些变量进行变形，这个一般用不到，使用默认的 False 即可。
## 数组列表
```
if __name__=='__main__':
    list_name=['xiaoming','zhangsan','wangwu','lisi']
    for n in list_name:
        user_name.insert_one({'_id':getNextValue('name'),'myname':n})
    for i in user_name.find():
        print(i)
```
# MongDB
[MongoDB简易教程](https://blog.csdn.net/weixin_37272286/article/details/79899788)
安装MongDB：
```
#安装最新开发版本
sudo brew install mongodb --devel
brew services start mongodb
```
```
To have launchd start mongodb now and restart at login:
  brew services start mongodb
Or, if you don't want/need a background service you can just run:
  mongod --config /usr/local/etc/mongod.conf
```
CRUD：
[MongoDB教程](http://www.runoob.com/mongodb/mongodb-dropdatabase.html)
`db.createUser({user:'user', pwd:'passwd', roles:[{role:'userAdminAnyDatabase', db:'admin'}]})`
[mongodb连接问题:257:13](https://www.jianshu.com/p/edc858a1a334)
```
sudo mongod —dbpath=/usr/local/var/mongodb
sudo find / -name mongod.conf
```
# python类中自定义方法的参数self
```
class Foo(object):  
#类中方法加入了self参数   
    def say_someThing(self,str):  
        print(str)
#类外方法不需要加入self参数   
def say_hello():  
    print（'hello'）  

#类外函数使用
say_hello()

#类内函数使用，不需要加入self相关参数 
foo=Foo()
foo.say_someThing("hi")
```
其中self指的是类的实例，因此在调用该方法的时候，我们需要先实例化，因此之后的参数当中，也就没有必要添加self这个参数，因为系统会自动加入类的实例

# 安装pyltp 系统版本问题
出现:
```
error: $MACOSX_DEPLOYMENT_TARGET mismatch: now "10.12" but "10.14" during configure
```
`MACOSX_DEPLOYMENT_TARGET=10.14 pip3 install pyltp`
## python 中的[:-1]和[::-1]切片知识
a='python'
[x:y:z]切片索引,x是左端,y是右端,z是步长,在[x,y)区间从左到右每隔z取值,默认z为1可以省略z参数.
步长的负号就是反向,从右到左取值.
python的b=a[::-1]那就是'nohtyp'

当i,j都缺省时，a[:]就相当于完整复制一份a
```
a='python'
b=a[::-1]
print(b) #nohtyp
c=a[::-2]
print(c) #nhy
#从后往前数的话，最后一个位置为-1
d=a[:-1]  #从位置0到位置-1之前的数
print(d)  #pytho
e=a[:-2]  #从位置0到位置-2之前的数
print(e)  #pyth
```
记住：[::-1]，[:-1]与[:,::-1]要清楚
```
import numpy as np
a=np.random.rand(5)
print(a)
[ 0.64061262  0.8451399   0.965673    0.89256687  0.48518743]
 
print(a[-1]) ###取最后一个元素
[0.48518743]
 # 
print(a[:-1])  ### 除了最后一个取全部
[ 0.64061262  0.8451399   0.965673    0.89256687]
 # 反转取得
print(a[::-1]) ### 取从后向前（相反）的元素
[ 0.48518743  0.89256687  0.965673    0.8451399   0.64061262]
 # 注意，是从2向前取。
print(a[2::-1]) ### 取从下标为2的元素翻转读取
[ 0.965673  0.8451399   0.64061262]
```
[:,::-1]--》有逗号说明是二维的数据（行，列）
```
n [33]: t = np.array([[1,2,3],[4,5,6],[7,8,9]])
In [34]: y = t[:,::-1]
In [35]: y
Out[35]: 
array([[3, 2, 1],
       [6, 5, 4],
       [9, 8, 7]])
```


## super方法
python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx : 其中Class是子类的名称
```
class A:
    pass
class B(A):
    def add(self, x):
        super().add(x)
```
python2当中
```
class A(object):   # Python2.x 记得继承 object
    pass
class B(A):
    def add(self, x):
    #因此super(MyModel, self).__init__(name='my_model')是为MyModel的父类定义别名
        super(B, self).add(x)
```
[super方法 调用父类的方法](https://www.cnblogs.com/zhaojingyu/p/9038899.html)
# cannot connect to X server
  X server是图形用户界面的应用程序
linux 上图像界面不起作用,因为使用了`cv.imshow("demo", re_im)`
[cannot connect to X server](https://www.jianshu.com/p/74b902950c4b)

# Flag duplicate
Delete all flags before declare
```
####Delete all flags before declare#####

def del_all_flags(FLAGS):
    flags_dict = FLAGS._flags()    
    keys_list = [keys for keys in flags_dict]    
    for keys in keys_list:
        FLAGS.__delattr__(keys)

del_all_flags(tf.flags.FLAGS)
```
或者
```
FLAGS.remove_flag_values(FLAGS.flag_values_dict()) 
```


