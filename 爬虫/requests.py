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
    
    
    
    
    

    
def newHTMLtext(url):
    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error!")
        
if __name__ == "__main__":
    url = 'http://www.baidu.com'
    print(newHTMLtext(url))
        
        
    
    
    
r = requests.head('http://httpbin.org/get')
r.headers        
r.text        
        

        
        
        
        
        
        
        
        
        
        
        
        
        

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrmoe/52.0.2743 Safari/537.36'
}

r = requests.get('http://www.zhihu.com/explore', headers = header)

r.text
import requests
r = requests.get("https://github.com/favicon.ico")# 获取GITHUB图标
print(r.text)
print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)

    