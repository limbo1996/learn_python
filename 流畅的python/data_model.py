'''
Author: limbo1996
Date: 2020-10-21 20:56:10
LastEditTime: 2020-11-03 15:39:54
FilePath: /learn_python/流畅的python/data_model.py
'''

'''
简单的例子实现python的特殊方法
'''
import collections

# 建立一个Card类
# namedtuple用来快速创建一个类，属性不可变
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
    
beer_card = Card('7', 'diamonds')    
    
beer_card



symbols = "$cRsadsa%"

codes = []

for symbol in symbols:
    codes.append(ord(symbol))
    
codes

# 列表推导式

codes_2 = [ord(symbol) for symbol in symbols]
codes_2


# 列表推导式的局部作用

x = "ABC"

dummy = [ord(x) for x in x]
x
dummy

# 列表推导式与filter和map比较

symbols = "$%#@@*@#&"
# 列表表达式
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 30]
beyond_ascii
# filter
beyond_filter = list(filter(lambda c: c > 30, map(ord, symbols)))
beyond_filter

#### 笛卡尔积
# 3种不同的衬衫，每个有2种颜色
colors = ['black', 'white']
sizes = ["S", "M", "L"]


tshirts = [(color, size) for color in colors
                        for size in sizes]

tshirts

# 等价于两层for循环
for color in colors:
    for size in sizes:
        print((color, size))
        
        

## 生成器表达式

tuple(ord(symbol) for symbol in symbols)

# 笛卡尔积
((c, s) for c in colors
        for s in sizes)

for tShirt in ((c, s) for c in colors
                        for s in sizes):
    print(tShirt)


# 元组和记录

lax_coordinates = (33.9425, -118.408)
latitude, longitude = lax_coordinates
latitude
longitude


divmod(20, 8) # return (x//y, x%%y)

t = (20, 8)
divmod(*t)

x, y = divmod(*t)
x
y
x, y


import os
_, file = os.path.split("~/test/test.py")
file

# 用*来处理不确定的元素

a, b, *rest = range(5)

a, b, rest


s = 'bicycle'

s[::3] #bye
s[::-1]# elcycib
s[::-2]# eccb


# 对对象进行切片
invoice = """
0.....6.................................40...........52..55........
1909  Pimoroni PiBrella                 $17.50       3   $52.50    
1489  6mm Tactile Switch *20             $4.85       2    $9.90    
1510  Panavise Jr. - PV-201             $28.00       1   $28.00    
1601  PiTFT Mini Kit 320*240            $34.95       1   $34.95
"""
    
line_items = invoice.split('\n')[2:]

UNIT_PRICE = slice(40, 52)
DESCRIPTION = slice(6, 40)

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])
    
    
    
# 给切片赋值

l = list(range(10))

l

l[2:5] = [20, 30]
l
l[6:8] = [100]
l


# 列表推导式的应用
board = [['_'] * 3 for i in range(3)]

board
# 以上代码等同于
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
    
board
board[1][2] = '0'
board

# 与之相反，错误的是
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
    
board
board[1][2] = '2'
board
'''
虽然board的结果相似，但是第二个是追加同一个对象三次到board
单第一个是每次创建一个列表对象到board, 从更改某一行的某一个元素的结果就可以看出来
'''


>>> t = (1, 2, [20, 40])
>>> t[2] += [30, 50]

test = ['a', 'c', 'd', 'b']

sorted(test)
test
test.sort()
test