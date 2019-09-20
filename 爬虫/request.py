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
print(type(r.json()))#需要注意的是如果返回的不是JSON格式的话就会报错

###抓取网页
import requests
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrmoe/52.0.2743 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers=header)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
print(r.text)
titles = re.findall(pattern, r.text)
print(titles)

###抓取二进制文件
import requests
r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
    
#添加headers
import requests
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrmoe/52.0.2743 Safari/537.36'
}
r = requests.get('http://www.zhihu.com/explore', headers = header)
print(r.text)

#POST请求
import requests
data = {'name':'germey', 'age':'22'}
r = requests.post