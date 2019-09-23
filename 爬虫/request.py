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
r = requests.post('http://httpbin.org/post', data = data)
print(r.text)

#响应
import requests
r = requests.get('https://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
#状态码常用来判断请求是否成功
#requests内置了requests.codes这个对象方便用来检查状态码
#requests.codes.ok为成功，状态码为200
#requests.codes.not_found为404


#cookies
import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)

for key, value in r.cookies.items():
    print(key + '=' + value)

#会话维持
#使用Session对象
import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)#这样并没有保留cookies
#使用Session
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
#这样就保留了登录信息


#超时设置
#同样是timeout参数
r = requests.get('http://taobao.com', timeout=1)
print(r.status_code)

#身份认证
import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost:5000', auth = HTTPBasicAuth('username', 'passwprd'))






