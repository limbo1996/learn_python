# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:22:14 2020

@author: limbo
"""
# 实例一， 爬取京东页面商品
import requests

# 使用框架
def getHTML(url):
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)       
    except:
        print("链接未成功")
    
url = "https://item.jd.com/2967929.html"
getHTML(url)

# 亚马逊商品页边的爬取
url3 = "https://www.amazon.cn/dp/B0757JL763/ref=pd_sim_351_2/457-2539420-7800638?_encoding=UTF8&pd_rd_i=B0757JL763&pd_rd_r=d72404c7-f758-48c8-9a4e-765ffa7c527d&pd_rd_w=Z5PTg&pd_rd_wg=jB3WB&pf_rd_p=7ed9834e-1f9f-4a98-9257-6a91ef62505c&pf_rd_r=3P5BJ7ZZQV32VKC4BGEE&psc=1&refRID=3P5BJ7ZZQV32VKC4BGEE"
getHTML(url3)# 链接未成功 ？？？

r = requests.get(url3)
r.status_code # 503
r.encoding
r.apparent_encoding 
r.encodingd = r.apparent_encoding
r.text
r.request.headers # python request 

# 模拟浏览器
kv = {"User-Agent" : "Mozilla/5.0"}
r = requests.get(url3, headers=kv)
r.status_code
r.text[:1000]
r.request.headers

# 整合代码
def getHTMLmodel(url):
    try:
        kv = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[1000:2000])
    except:
        print("链接未成功")

##################
# 百度搜索关键词提交

wd = {"wd" : "python"}
r = requests.get("http://www.baidu.com/s", 
                 params=wd)
r.status_code
r.request.url
len(r.text) # 564276 返回地很大

# 整合代码
def getHTMLkv(url, keyword):
    try:
        kv = {"wd" : keyword}
        r = requests.get(url, params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print("链接未成功")

# 网络图片的爬取和储存

import requests

# 网络图片的爬取
# 基本格式
# http://www.example.com/picture.jpg

# 以国家地理网站为例
# https://www.nationalgeographic.com/content/dam/animals/2020/07/glacier-bear/glacier-bear-111dscf0068.adapt.945.1.jpg

path = "D:/abc.jpg"
url = 'https://www.nationalgeographic.com/content/dam/animals/2020/07/glacier-bear/glacier-bear-111dscf0068.adapt.945.1.jpg'

r = requests.get(url)

r.status_code # 返回码是200， 访问成功

with open(path, "wb") as f:
    f.write(r.content) # r.content 返回地是二进制内容， 所以直接写入， 因为图片就是二进制格式的

f.close()

# 代码整理

import requests
import os

url = 'https://www.nationalgeographic.com/content/dam/animals/2020/07/glacier-bear/glacier-bear-111dscf0068.adapt.945.1.jpg'
root = "D://pics//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("链接失败")

# ip地址归属地自动查询
import requests

# 借助网站
# Ip138这个网站可以

# https://www.ip138.com/iplookup.asp?ip=ip

url = "https://www.ip138.com/ip.asp?ip="

r = requests.get(url + "180.167.19.87")

r.status_code

r.text[-500:]































