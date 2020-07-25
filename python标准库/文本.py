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
# 编译正则表达式
regexes = [
    re.compile(p) #此函数可以把p保存为一个RegexObject 对象
    for p in ['this', 'that']]

text = 'Does this text match pattern?'

print('Texe: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern))
    if regex.search(text):
        print('match!')
    else:
        print('not match')