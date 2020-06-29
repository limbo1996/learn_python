# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:58:39 2020

@author: baba
"""
# 文本库
# 将字符串转换为大写
import string

s = 'The quick brown fox jumped over the lazy dog'

print(s)
print(string.capwords(s))

# re 正则表达式


import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)
s = match.start()
e = match.end()

print('Found "{}"\nin "{}\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))


