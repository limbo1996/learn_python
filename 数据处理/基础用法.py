import pandas as pd
import numpy as np
from pandas import Series, DataFrame

index = pd.date_range('1/1/2000', periods=8)
s = pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame(np.random.randn(8, 3), index = index,
                  columns=['A', 'B', 'C'])
df
'''
                   A         B         C
2000-01-01  1.327162  0.455742 -0.161866
2000-01-02  0.982357  0.249684 -1.271651
2000-01-03 -0.311862  0.106956 -0.653332
2000-01-04  1.315401  1.371467  0.462123
2000-01-05 -0.230576 -0.230266  0.054890
2000-01-06  0.872861 -0.942211 -0.556294
2000-01-07 -0.293750  0.193073  0.390720
2000-01-08 -0.733031 -0.024738  0.844523
'''
# head and tail 
# 默认显示5条
df.head()
df.tail()

# 属性和底层数据
# 输出轴的维度
df.shape
# 轴标签
df.index
df.columns
df.columns = [x.lower() for x in df.columns]
#提取Series或者index中的数据
s
s.array
s.index.array
df.index.array
df.columns.array