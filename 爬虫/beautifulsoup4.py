# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:45:42 2020

@author: baba
"""
import requests
from bs4 import BeautifulSoup 

url = "http://python123.io/ws/demo.html"

r = requests.get(url)
r.status_code
r.encoding

r.text
demo = r.text

soup = BeautifulSoup(demo, "html.parser")

print(soup.prettify())
# 标签的名字
soup.a.name # a
soup.a.parent.name # p

soup.p.parent.name # body

# 标签的属性
tag =  soup.a
type(tag) # bs4.element.Tag
tag.attrs # 字典
tag.attrs['class']# ['py1']
type(tag.attrs) # dict
# 取出字符串
soup.a
soup.a.string

# 注释
soup.b
soup.p
# 注意判断是否是注释类型
# comment 类型就是注释
























