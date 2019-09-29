# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:54:52 2019
ref = 《python3网络爬虫实战》
@author: Limbo
"""
#URL异常
#URLError处理url的异常
from urllib import request, error
try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)
#HTTPError
#用来处理http错误，比如认证请示求败
from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')


#URLError是HTTPError的父类，所以可以现捕获子类的错付，再捕获父类的
from urllib import request, error
try:
    response = request.urlopen('https://baidu.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request successfully')

#有时候reason返回的不一定是字符串而是一个对象
import socket
import urllib.request
import urllib.error
try:
     request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
#######################
#解析链接
#使用urllib中的parse模块
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')

#相对立的方法urlunparse
from urllib.parse import urlunparse
    
data = ['https', 'www.baidu.com', 'index.html', 'users', 'a=6', 'comment']
print(urlunparse(data))#这样就完成了url的构造，此函数的需要的长度为6

#urlsplit
from urllib.parse import urlsplit
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0])#返回的result也是一个元组

#urlunsplit

#同样是用来构建url的，只不过参数长度必须为5

from urllib.parse import urlunsplit
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))

###urlencode
#同样是用来构建url的一个方法
from urllib.parse import urlencode
params = {
    'name': 'germy',
    'age': '22'
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
#与urlencode相对应的反序列化
from urllib.parse import parse_qs
query = 'name=germy&age=22'
print(parse_qs(query))

#########################################

#quote
#将内容转化为URL编码格式
#比如内容包括中文的时候会引起乱码，使用此函数转换为URL编码

from urllib.parse import quote
keyword = "壁纸"
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url)


#unquote
#与上面相反是用来解码的
from urllib.parse import unquote
url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))




















