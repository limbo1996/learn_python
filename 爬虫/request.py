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



#测试
import json
from requests.exceptions import RequestException
import re
import time
import requests

def get_one_page(url): #获取页面信息
    try:
        headers = {
            'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36(KHTML, like Gecko)Chrmoe/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
    
def parse_one_page(html):#分析第一页
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name".*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:

        yield{
            'index' : item[0],
            'image' : item[1],
            'title' : item[2],
            'actor' : item[3].strip()[3:],
            'time' : item[4].strip()[5:],
            'score' : item[5] + item[6]
        }
    
def write_to_file(content):#写入文件
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dump(content, ensure_ascii=False) + '\n')

def main(offset):#读取其余页面
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i * 10)
        time.sleep(1)







def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()

