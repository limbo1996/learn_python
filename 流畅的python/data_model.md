# Python 数据模型
python 解释器碰到一些特殊的句法时，会使用特殊方法去激活一些基本的对象操作，这些特殊方法的名字以两个下划线开头，以两个下划线结尾(`__init__`)。
`obj[key]`的背后是`__getitem__`方法。如果想求得`my_collection[key]`的值，解释器会调用`my_collection.__getitem__`方法。

## 简单的例子实现特殊方法
```
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
