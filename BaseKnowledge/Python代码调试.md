# 代码调试
## ValueError: invalid literal for int() with base10: '80.790'
　　字符串含有float型数值,不能直接用int,需要先转换成float,再转换成int
```
percent_str=百分之80.790
percent_str=int(re.search('\d+\.?\d*',percent_str)[0])/100
```
会报错:
```
ValueError: invalid literal for int() with base 10: '80.790'
```
[ValueError: invalid literal for int() with base10](https://www.cnblogs.com/ddpeng/p/9759145.html)
## 调试
### 可以运行但是不能调试
(1)出现 can't from base64 import encode64
  　　新建了一个base64文件,但是你有base64库,这样就会容易造成冲突,因此修改base64文件名即可.
## 包的导入
　　千万不可递归导入
## 全局变量两种
　　同一个文件当中,全局变量需要用global进行声明:
```
global sentenceAndScope
sentenceAndScope = []
```
　　在不同文件当中,则只需要把其放在当前文件的全局变量即可,之后进行导入
　　全局变量在传递的过程当中,如果在另一个函数当中进行调用,则需要将其作为参数,并且,需要将全局变量作为返回值进行返回.例子如下:
```
# 元素值时间类型的提取
def elementAbstractByType(element_type=None, element_value=None):
    result_l = []
    global element_type_str
    element_type_str = ""
    if (element_type == TIME):
        result_l,element_type_str = elementTimeAbstract(element_type,element_type_str)
    if (element_type == MONEY):
        result_l,element_type_str = elementMoneyAbstract(element_value,element_type_str)
    return result_l
```
　　然后需要在被传递的函数当中,作为参数传递并进行返回:`result_l,element_type_str = elementMoneyAbstract(element_value,element_type_str)`
## 函数添加参数
　　`def elementAbstractByType(element_type=None,element_value)`定义成这样在运行的时候会报错
　　除非参数都定义为None：`def elementAbstractByType(element_type=None,element_value=None):`
## return None 与except
　　返回None,不会执行except,可以手动设置异常Exception()里面到话,遇到异常肯定会打印出,因此我们,如果单纯打印异常,可以设置内容,如果有其他操作,最好不要设置内容
## 可变参数
　　如果在主函数,需要对可变参数进行操作,我们就要先进行判断,如下面这样.
```
def ValueCompare(element_char, operation, element_value_l, input_value_l,*time_type_l):
    if time_type_l:
        if time_type_l[0] == 'region':
            element_value_l = [int(x) for x in element_value_l]
            # 转换之后,最好排下序,['18144000', '5184000']--可能受之前175行排序的影响
            element_value_l=sorted(element_value_l)
            input_value_l = [int(x) for x in input_value_l]
            input_value_l=sorted(input_value_l)
```
## if与报错
　　`AttributeError: 'NoneType' object has no attribute 'group'`,说明没有匹配成功,也就是`re.match()`的值为`None`,因此会报错,一般会报错的函数,其函数值不要作为if判断语句,我们可以使用`re.match()`,因为其值不报错,最坏就是None
　　`IndexError: no such group`:说明有匹配到,只是下标错误
## ValueError: too many values to unpack (expected 2)
　　说明返回值有多个,不匹配
## p.checkVector(2, CV_32S) >= 0 in function 'polylines'
  说明在画框的时候,copylines只能精确到整数(因为图像就是由像素组成),因此
  ` cv2.polylines(img, [box[:8].astype(np.float64).reshape((-1, 1, 2))], True, color=(0, 255, 0),thickness=2)`
  则是错误的 
## TypeError: 'float' object cannot be interpreted as an integer
  说明 需要整数,在python3中`/`的结果是浮点数,我们要求得整数,则需要将其转换成整数,我们可以使用`//` 或者使用`int()`.
  因此错误就出现在:`point = np.reshape(point, newshape=(len(point) / 4, 8))`,改成:
  `int(len(point) / 4`或`int(len(point) // 4`即可
  
## 二维list 无法转为二维的numpy.array?
  [二维列表转数组的特殊情况](https://blog.csdn.net/qq_31785005/article/details/78460757)

## cv2.imwrite写入的图片为0kb
   有可能是坐标没有按照对角线的坐标进行排序的后果.首先用正常数值的正确顺序进行排查




　　

