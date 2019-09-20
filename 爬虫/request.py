# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:54:52 2019
ref = 《python3网络爬虫实战》
@author: Limbo
"""

#使用requests
import requests
r = requests.get('http://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

#GET请求
r = requests.get('http://httpbin.org/get')
print(r.text)

#附加额外信息
import requests
data = {
    'name': 'germy',
    'age': '22'
}
r = requests.get('http://www.httpbin.org/get', params=data)
print(r.text)#可以看到url中的链接添加了信息

#解析结果得到字典格式
print(r.json())
print(type(r.json()))