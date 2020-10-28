<!--
 * @Author: limbo1996
 * @Date: 2020-10-28 19:42:32
 * @LastEditTime: 2020-10-28 22:30:32
 * @FilePath: /learn_python/流畅的python/data_model.md
-->
# Python 数据模型
python 解释器碰到一些特殊的句法时，会使用特殊方法去激活一些基本的对象操作，这些特殊方法的名字以两个下划线开头，以两个下划线结尾(`__init__`)。
`obj[key]`的背后是`__getitem__`方法。如果想求得`my_collection[key]`的值，解释器会调用`my_collection.__getitem__`方法。

## 简单的例子实现特殊方法
```{python}
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
```
`namedtuple`用于构建只有少量属性但是没有方法的对象。


`reversed`可以反向迭代

```{python}
for i in reversed(deck):
	print(i)
```

`hypot`函数返回欧几里得范数 `sqrt(x * x + y * y)`， 也就是勾股定理的值

```{python}
import math

math.hypot(x, y)
```

`bool`函数用于将给定参数转换为布尔类型，如果没有参数，返回`False`

```{python}
>>>bool()
False
>>> bool(0)
False
>>> bool(1)
True
>>> bool(2)
True
>>> issubclass(bool, int)  # bool 是 int 子类
True
```

只有0会返回False， 是空时也返回0

## 数据结构

### 序列组成的数组

python标准库用C实现了很多数据类型

* 容器序列
  * list
  * tuple
  * collections.deque
* 扁平序列
  * str
  * bytes
  * bytearrary
  * array

扁平序列其实是一段连续的内存空间，但是只能放字符、字节、数值这种基础类型。



### 列表推导式

`ord`返回对应的ASCII数值或者Unicode数值。

通常只用列表推导式来创建新的列表。尽量简短，不超过两行。
平常模式
```{python}
symbols = "$cRsadsa%"

codes = []

for symbol in symbols:
    codes.append(ord(symbol))
    
>>> codes
[36, 99, 82, 115, 97, 100, 115, 97, 37]
```
列表推导式
```
codes_2 = [ord(symbol) for symbol in symbols]
>>> codes_2
[36, 99, 82, 115, 97, 100, 115, 97, 37]
```
列表推导式的优点
不会再有变量泄露的问题
python3中，列表推导，生成器表达式，以及集合或者字典推导式，
都有局部作用.

```{python}
x = "ABC"

dummy = [ord(x) for x in x]
>>> x
'ABC'
>>> dummy
[65, 66, 67]
```
x的值并没有被替换。
`filter`和`map`也有类似的作用。

### 列表推导式和`filter`以及`map`的比较

```{python}
symbols = "$%#@@*@#&"
# 列表表达式
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 30]
beyond_ascii
# filter
beyond_filter = list(filter(lambda c: c > 30, map(ord, symbols)))
beyond_filter
>>> beyond_ascii
[36, 37, 35, 64, 64, 42, 64, 35, 38]
>>> beyond_filter
[36, 37, 35, 64, 64, 42, 64, 35, 38]
```

#### 笛卡尔积
比如需要一个列表，列表中是3种不同尺寸的衬衫，每种衬衫有2种不同的颜色。
```{python}
colors = ['black', 'white']
sizes = ["S", "M", "L"]


tshirts = [(color, size) for color in colors for size in sizes]

>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
```
等价于
```{python}
>>> for color in colors:
...     for size in sizes:
...         print((color, size))
... 
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')
```
列表推导式的作用就是生成列表。
如果要生成其他类型的序列，要用到生成器表达式


### 生成器表达式
虽然列表推导式也能用来初始化元组，数组或者其他的序列类型。但是用生成器表达式是更好的选择。因为会节省内存

生成器表达式的语法和列表推导式的语法相似，只是把方括号换成圆括号。
```{python}

tuple(ord(symbol) for symbol in symbols)

(36, 37, 35, 64, 64, 42, 64, 35, 38)
# 笛卡尔积
((c, s) for c in colors
        for s in sizes)
```
笛卡尔积返回的是生成器

```{python}
>>> for tshirt in ((c, s) for c in colors
...                         for s in sizes):
...     print(tshirt)
... 
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')
```
生成器会逐个的产生元素，而不是一次产生含有6个元素的列表

### 元组不仅仅是不可变的列表
把元组简单理解成“不可变的列表”并没有完全概括元组的全部特征。
元组还可以作为没有字段名的记录。
#### 元组和记录
元组其实是对数据的记录：元组中的每一个元素都存放了记录中一个字段的数据，外加这个字段的位置。

#### 元组拆包
最好辨认的元组拆包就是**平行赋值**
```{python}
>>> lax_coordinates = (33.9425, -118.408)
>>> latitude, longitude = lax_coordinates
>>> latitude
33.9425
>>> longitude
-118.408
```
还可以使用`*`运算符来把一个可迭代对象拆开作为函数的参数
```{python}
>>> divmod(20, 8) # return (x//y, x%%y)
(2, 4)
>>> t = (20, 8)
>>> divmod(*t)
(2, 4)
>>> x, y = divmod(*t)
>>> x
2
>>> y
4
>>> x, y
(2, 4)
```

元组拆包的另一个用法就是让函数以元组的形式返回多个值，然后调用函数的代码接受这些值
```{python}
>>> import os
>>> os.path.split("~/test/test.py")
('~/test', 'test.py')
>>> _, file = os.path.split("~/test/test.py")
>>> file
'test.py'
```
通过占位符`_`抛弃不用的元素。
除此之外，元组拆包中使用`*`也可以帮助我们关注元组的部分元素。
#### 用`*`来处理剩下的元素
```{python}
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
```
类似于函数用`*arg`来获取不确定参数
`*`只能在一个变量前面，但是这个变量可以在赋值表达式的任意地方




