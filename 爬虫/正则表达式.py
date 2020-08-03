# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

# 0-99
# [0-9]?\d
# 100 -199
# 1\d{2}
# 200 - 249
# 2[0-4]\d
# 250 - 255
# 25[0-5]

import re
# search 匹配第一个位置

match = re.search(r'[1-9]\d{5}', 'BIT 100081')

if match:
    print(match.group(0))
# match
'''
match从字符串开头开始匹配
'''
match = re.match(r'[1-9]\d{5}', 'BIT 100081')

if match:
    print(match.group(0))# 空
match = re.match(r'[1-9]\d{5}', '100081 BIT')
match.group(0)

# findall 返回所有匹配列表

ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
ls

# split 将匹配的部分排除，然后分割后返回列表
ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
ls # ['BIT', ' TSU', '']

ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
ls


# finditer 返回匹配结果的迭代类型
for i in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if i:
        print(i.group(0))

# sub 替换匹配的字符串
ls = re.sub(r'[1-9]\d{5}', 'a', 'BIT100081 TSU100084', count=2)
ls     

# 编译方法的使用
pat = re.compile(r'[1-9]\d{5}')# 将正则表达式编译为对象
rst = pat.findall('BIT100081 TSU100084')
rst


# 最小匹配
match = re.search(r'PY.?N', 'PYANBNCNDN')
match.group(0) 
