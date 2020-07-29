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

# 遍历标签
# 遍历子节点
# 
soup = BeautifulSoup(demo, "html.parser")

soup.head

soup.head.contents
soup.body.contents

for i in soup.body.children:
    print(i)

# 上行遍历
# .parent/.parents

soup.title.parent


# 平行遍历
soup.a.next_sibling
soup.a.next_sibling.next_sibling

soup.a.previous_sibling


# 格式输出
demo

soup.prettify()
print(soup.prettify())

######################
# 信息提取
from bs4 import BeautifulSoup
import re
# 解析标签
soup = BeautifulSoup(demo, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))

soup.find_all('a')

soup.find_all(['a', 'b'])

# 找到b开头的标签

for tag in soup.find_all(re.compile('b')):
    print(tag.name)
# 搜索属性
    
soup.find_all('p', 'course')

soup.find_all(id = 'link1')
soup.find_all(id = 'link')# 空

soup.find_all(id = re.compile('link'))


# 子父节点
soup.find_all('a')
soup.find_all('a', recursive=False)# 空

soup
soup.find_all(string = "Basic Python")
soup.find_all(string = re.compile('Python'))


# 简写
soup('a')












