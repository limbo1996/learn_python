# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:06:28 2020

@author: limbo
"""
import requests
# 访问百度网页
r = requests.get('http://www.baidu.com')
# 查看状态码
r.status_code # 200 代表成功
 
r.encoding
r.apparent_encoding

r.encoding = 'utf-8'

r.text
 

# 通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
    
if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))