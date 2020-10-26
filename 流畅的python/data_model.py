'''
Author: limbo1996
Date: 2020-10-21 20:56:10
LastEditTime: 2020-10-26 09:30:11
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