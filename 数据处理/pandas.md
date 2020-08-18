# pandas入门
## pandas数据结构 
主要有两个数据结构`Series` 和 `DataFrame`
### Series
是一种类似于一维数组的对象，由一组数据和索引组成
```
In [1]: import pandas as pd                                                                                                                                          

In [2]: obj = pd.Series([4, 7, -5, 3])                                                                                                                               

In [3]: obj                                                                                                                                                          
Out[3]: 
0    4
1    7
2   -5
3    3
dtype: int64
```
Series的表现形式是：索引在左边，值在右边。
可以通过Series的`values`和`index`属性获取相应的值
```
In [4]: obj.values                                                                                                                                                   
Out[4]: array([ 4,  7, -5,  3])
In [5]: obj.index                                                                                                                                                    
Out[5]: RangeIndex(start=0, stop=4, step=1)
```
也可以自定义索引。
```
In [6]: obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])                                                                                                  

In [7]: obj2                                                                                                                                                         
Out[7]: 
d    4
b    7
a   -5
c    3
dtype: int64

In [8]: obj2.index                                                                                                                                                   
Out[8]: Index(['d', 'b', 'a', 'c'], dtype='object')
```
可以通过索引来选取单个或者一组值
```
In [9]: obj2['a']                                                                                                                                                    
Out[9]: -5

In [10]: obj2['d'] = 6                                                                                                                                               

In [11]: obj2                                                                                                                                                        
Out[11]: 
d    6
b    7
a   -5
c    3
dtype: int64
```
如果数据存放在一个字典里，可以直接用字典来创建Series
```
In [12]: sdata = {'d':211, 's':42343, 'w':3232}                                                                                                                      

In [13]: obj3 = pd.Series(sdata)                                                                                                                                     

In [14]: obj3                                                                                                                                                        
Out[14]: 
d      211
s    42343
w     3232
dtype: int64
```
索引就是原来字典的键
重新定义索引
```
In [15]: obj3.index = ['q', 'e', 'r']                                                                                                                                

In [16]: obj3                                                                                                                                                        
Out[16]: 
q      211
e    42343
r     3232
dtype: int64
```
判断是否是缺失值的函数`isnull()`, `notnull`.
```
In [17]: obj3.isnull()                                                                                                                                               
Out[17]: 
q    False
e    False
r    False
dtype: bool
```
Series对象本身与其索引都有一个`name`属性
```
In [23]: obj3.name = 'test'                                                                                                                                          

In [24]: obj3.index.name = 'name'                                                                                                                                    

In [25]: obj3                                                                                                                                                        
Out[25]: 
name
q      211
e    42343
r     3232
Name: test, dtype: int64
```