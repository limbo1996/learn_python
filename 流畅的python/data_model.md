<!--
 * @Author: limbo1996
 * @Date: 2020-10-28 19:42:32
 * @LastEditTime: 2020-10-28 20:39:14
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