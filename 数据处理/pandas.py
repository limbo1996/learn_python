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
# 为不存在的列赋值会创建新列
# del 可以用来删除列
frame['debt'] = 15.7
frame
del frame['debt']
frame
'''
    state  year  pop  debt
0    Ohio  2000  1.5  15.7
1    Ohio  2001  1.7  15.7
2    Ohio  2002  3.6  15.7
3  Nevada  2001  2.4  15.7
4  Nevada  2002  2.9  15.7
>>> del frame['debt']
>>> frame
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
'''
# 注意索引返回的只是元数据的视图，并不是副本，对其的操作都会反映在元数据上，想要赋值，可以使用copy
# 创建dataframe的另一个方法是使用嵌套字典
# 嵌套字典的外部键会作为列名，内部键作为行名

pop = {'Nevada' : {2001 : 2.4, 2202: 2.9},
       'Ohio' : {2000 : 1.45, 2001 : 1.7, 2002 : 3.6}}
pop

frame2 = DataFrame(pop)
frame2


############################################################## 索引对象
# 索引对象不可修改
obj = Series(range(3), index = ['a', 'b', 'c'])

index = obj.index

index
index[1:]

index[1]= 'd'
'''
>>> index[1]= 'd'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/limbo1996/miniconda3/lib/python3.8/site-packages/pandas/core/indexes/base.py", line 4075, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations
'''

index = pd.Index(np.arange(3))

obj = Series([1.5, -2.5, 0], index = index)
obj

#################################################基本功能
# 重新索引
# reindex
obj = Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
obj
'''
d    4.5
b    7.2
a   -5.3
c    3.6
'''
# 调用reindex会根据新索引重新排序，如果不存在数据，会引入NA
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2
'''
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN
dtype: float64
'''
# method
obj3 = Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])

obj3.reindex(range(6), method = 'ffill') # 前向填充， 后向填充bfill
'''
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
'''

# 使用reindex时，传入一个序列，默认重新索引行
# 使用关键字， columns可以重新索引列

frame = DataFrame(np.arange(9).reshape((3, 3)), index = ['a', 'c', 'd'],
                  columns = ['Ohio', 'Texas', 'California'])

frame

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2
'''
>>> frame
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8
>>> frame2 = frame.reindex(['a', 'b', 'c', 'd'])
>>> frame2
   Ohio  Texas  California
a   0.0    1.0         2.0
b   NaN    NaN         NaN
c   3.0    4.0         5.0
d   6.0    7.0         8.0
'''
states = ['Texas', 'Utah', 'California']
frame2 = frame2.reindex(columns = states)
frame2
'''
   Texas  Utah  California
a    1.0   NaN         2.0
b    NaN   NaN         NaN
c    4.0   NaN         5.0
d    7.0   NaN         8.0
'''
frame.index = ['b', 'c', 'd']
frame.reindex(index = ['a', 'b', 'c', 'd'])
frame.columns
for col in frame.columns:
    print(col)
frame
# 数据选取
# 按标签选择
frame.loc['c'] #提取一行
frame.loc[:, ['Ohio', 'Texas']] # 提取多列
frame.loc['b':'c', ['Ohio', 'Texas']] # 提取行和列
frame.loc['b', ['Ohio', 'Texas']] # 返回数据降维
'''
Ohio     0
Texas    1
Name: b, dtype: int64
'''
frame.loc['b', 'Ohio'] # 提取标量
frame.at['b', 'Ohio'] # 与上面等效，快速读取

# 按位置选择
frame
frame.iloc[2] #选取第3行
df = frame
df.iloc[0:2, 1:3] # 用整数切片 
df.iloc[[0, 2], [0, 2]]# 用整数列表切片
# 整行和整列的切片和R不同，注意要有：
df
df.iloc[:, [0, 2]]# 获取1，3列的所有行
# 列同理
# 提取值
df.iloc[1,1]
# 快速访问标量，效果同上
df.iat[1,1]

# 布尔值索引

df
# 按照某一列来筛选数据
df[df.Ohio > 1]
# 选择整个数据中符合要求的值
df[df > 4]

# 用isin()筛选
df2 = df.copy()
df2
df2['E'] = ['one', 'two', 'three', 'four', 'five']
df2
df2[df2['E'].isin(['two', 'four'])]
# 赋值
# 按照标签赋值
df.at[1, 'state'] = 0
df
# 按照位置赋值
df.iat[0, 1] = 0
df
df.loc[:, 'E'] = np.array([5] * len(df))
df



df2 = df.copy()
df2
test = df2.loc[:, ['pop', 'E']]
test
# 将大于3的取负号
test[test > 3]  = -test
test

# 缺失值
# 用 np.nan来表示缺失值
test = test[test > 3]
test
# 删除含有NA的行
test.dropna(how = 'any')
# 填补缺失值
test.fillna(value = 5)
# 判断是否是NA
pd.isna(test)

# 运算
# 计算列的平均值
test.mean()
# 计算行的
test.mean(1)
test
# apply函数
# 计算累积
test.apply(np.cumsum)

test.apply(lambda x: x.max() + x.min())


s = pd.Series(np.random.randint(0, 7, size = 10))
s
# 计算每个值出现了多少次
s.value_counts()
'''
5    3
3    3
2    3
0    1
dtype: int64
'''
# 字符串
 s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
 s
 # 转化为小写
 s.str.lower()


#########################################
#数据连接
df = pd.DataFrame(np.random.randn(10, 4))
df
# 分解
pieces = [df[:3], df[3:7], df[7:]]
pieces

pd.concat(pieces) #类似于R中的rbind

# join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})


right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})


left
right
pd.merge(left, right, on = 'key')
# 注意一样的key会两两结合所以会产生四行
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

pd.merge(left, right, on = 'key') # 这样就产生两行


# append追加
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
df
s = df.iloc[3] #第三行
s

df.append(s, ignore_index = True) # 忽略index追加到最后一行，否则最后的index就是3
# 分组
# 有分割 应用 组合
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                       'C': np.random.randn(8),
                       'D': np.random.randn(8)})

df

# 分组后求和
df.groupby('A').sum()
# 按照多种分组
df.groupby(['A', 'B']).sum()

# 透视
# 长宽列表转换
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                       'B': ['A', 'B', 'C'] * 4,
                       'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       'D': np.random.randn(12),
                       'E': np.random.randn(12)})


df
'''
        A  B    C         D         E
0     one  A  foo -0.355625 -0.074833
1     one  B  foo  1.172245 -0.499640
2     two  C  foo -0.511366 -0.502507
3   three  A  bar  0.833089  1.452084
4     one  B  bar  0.536015 -0.318708
5     one  C  bar  0.739397  0.321931
6     two  A  foo -0.659834 -2.460920
7   three  B  foo  0.876201  0.630652
8     one  C  foo -1.109514  1.074370
9     one  A  bar  0.009602  0.991574
10    two  B  bar  0.441308  1.174960
11  three  C  bar  1.066730 -0.624623
'''
pd.pivot_table(df, values = 'D', index = ['A', 'B'], columns = ['C'])
'''
C             bar       foo
A     B                    
one   A  0.009602 -0.355625
      B  0.536015  1.172245
      C  0.739397 -1.109514
three A  0.833089       NaN
      B       NaN  0.876201
      C  1.066730       NaN
two   A       NaN -0.659834
      B  0.441308       NaN
      C       NaN -0.511366
'''
