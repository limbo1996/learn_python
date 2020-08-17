# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:40:13 2020

@author: baba
"""

from pandas import Series, DataFrame
import pandas as pd

# 数组
obj = Series([4,5,6])
obj
obj.values
obj.index

obj2 = Series([4,5,6,7], index=['a','b','v','d'])
obj2

obj2['a']
obj2['b'] = 6
obj2


obj2[['v', 'a', 'd']]

# 