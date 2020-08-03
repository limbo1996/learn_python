# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:30:08 2020
实例 淘宝商品比价
@author: limbo
"""
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        "连接错误"

def parsePage(ilt, html):

    try:
        plt = re.findall(r'\"view_price\"',
                         html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',
                         html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])# eval 将最外风的引号去掉
            title = eval(tlt[i].split(":")[1])
            ilt.append([title, price])
    except:
        print("错误")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for i in ilt:
        count = count + 1
        print(tplt.format(count, i[0], i[1]))
       
    
    
    
def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
        
    printGoodsList(infoList)
    
main()



##################更新，已失效
# 需要模拟登录