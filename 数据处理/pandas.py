# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:40:13 2020

@author: limbo
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
##########################################################Series
# 数组 由一组数据以及数据的索引组成
obj = Series([4,5,6])
obj
'''
0    4
1    5
2    6
dtype: int64
'''
# 类似于字典，可以使用value和index访问相关信息
obj.values
obj.index

# 指定index
obj2 = Series([4,5,6,7], index=['a','b','v','d'])
obj2
'''
a    4
b    5
v    6
d    7
dtype: int64
'''
# 通过索引来访问值，以及重新赋值
obj2['a']
obj2['b'] = 6


# 选出一组值
obj2[['v', 'a', 'd']]

# 数组计算
obj2
obj2[obj2 > 4]
obj2 * 2
np.exp(obj2)

# 如果数组在一个字典中，那这个字典可以直接用来创建Series
sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 = Series(sdata)
obj3 
# 字典原来的键自动变成Series的index

# Series本身和index都有一个name属性
obj3.name = 'population'
obj3.index.name = 'state'
obj3
'''
state
Ohio      35000
Texas     71000
Oregon    16000
Utah       5000
Name: population, dtype: int64
'''
###########################################################dataframe
# 创建dataframe
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)
frame
# 会自动加上行索引

# 如果指定列索引顺序，就会按照索引顺序排列
DataFrame(data, columns = ['year', 'state', 'pop'])
'''
>>> frame
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
>>> DataFrame(data, columns = ['year', 'state', 'pop'])
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
'''
# 排序十如果传入的列在数据中找不到，就会产生NA值
# 同样可以使用索引来访问值
frame['state']
frame.year
# 返回的与原来的dataframe相同的索引， name属性也被设置好了
# 添加列
frame['debt'] = 16.5
frame
'''
>>> frame
    state  year  pop  debt
0    Ohio  2000  1.5  16.5
1    Ohio  2001  1.7  16.5
2    Ohio  2002  3.6  16.5
3  Nevada  2001  2.4  16.5
4  Nevada  2002  2.9  16.5
'''
#或者
frame['debt'] = np.arange(5.)

frame
'''
    state  year  pop  debt
0    Ohio  2000  1.5   0.0
1    Ohio  2001  1.7   1.0
2    Ohio  2002  3.6   2.0
3  Nevada  2001  2.4   3.0
4  Nevada  2002  2.9   4.0
'''
# 将列表或者数组赋值给某个列时，需要保证长度相同，如果赋值的是一个Sreies，那会严格匹配dataframe的索引，没有的用NA值填充
val = Series([-1.2, -1.5, -1.7])
frame['debt'] = val
frame
'''
    state  year  pop  debt
0    Ohio  2000  1.5  -1.2
1    Ohio  2001  1.7  -1.5
2    Ohio  2002  3.6  -1.7
3  Nevada  2001  2.4   NaN
4  Nevada  2002  2.9   NaN
'''
val = Series([-1.2, -1.5, -1.7], index = [2, 3, 0])
frame['debt'] = val
frame
'''
    state  year  pop  debt
0    Ohio  2000  1.5  -1.7
1    Ohio  2001  1.7   NaN
2    Ohio  2002  3.6  -1.2
3  Nevada  2001  2.4  -1.5
4  Nevada  2002  2.9   NaN
'''
