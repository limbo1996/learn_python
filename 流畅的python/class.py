# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:25:33 2019

@author: Limbo
ref:《流畅的python》
"""

import collections
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

deck = FrenchDeck()
len(deck)#len函数可以查看有多少张牌

#特定抽取特定的牌
deck[0]
deck[-1]
#随机抽取
from random import choice
choice(deck)
choice(deck)
#查看最上面三张
deck[:3]
#只看牌面是A的牌
deck[12::13]
#因为python索引是从0开始的所以A是第12张
#然后每13张取一张

#迭代
for card in deck:
    print(card)



Card('Q', 'hearts') in deck
Card('Q', 'bearts') in deck
#排序（按照点数大小2-A，花色黑桃， 红桃， 方块， 梅花）
#所以从小到大梅花2是0， 黑桃A是51
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
for card in sorted(deck, key = spades_high):
    print(card)
 
    
####################################################################
#特殊方法
#特殊方法是隐式的
#比如for i in x 其实使用的是iter(x), 而这背后其实是x.__iter__()
#自己不要随意创造特殊方法


#例子
from math import hypot
class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    