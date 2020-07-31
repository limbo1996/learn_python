# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:33:38 2020
中国大学排名定向爬虫
@author: limbo
"""
import requests
from bs4 import BeautifulSoup
import bs4


url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'

def getHTMLText(url): # 获取url链接内容
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "简介失败"



def fillUnivList(ulist, html): # 解析HTML内容
    soup = BeautifulSoup(html, "html.parser")
    '''
    查看网页源代码可以发现所有的大学信息放在
    tbody中
    每个大学都有一个专属的 tr，是tbody的子标签
    另外tr下的子属性是td，存储了大学的具体信息，如排名，姓名，省市等
    所以首先提取所有的tbody
    在tbody中检索tr和td即可
    '''
    for tr in soup.find('tbody').children: #遍历所有tr
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')# 在每个tr中检索td，存储为list
            ulist.append([tds[0].string, 
                          tds[1].string,
                          tds[2].string])

def printUnivList(ulist, num):
    '''
    因为中文输出的对齐问题
    产生这个问题的原因是因为，在中文字符输出完成但是没有占满时，系统自动用
    西文字符填充，导致不对其，使用chr(12288)代表中文中的空格
    '''
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}" #格式化输出信息，第二个替换中添加{3}代表使用format的第三个参数替换
    print(tplt.format("排名", 
                      "学校名称",
                      "总分",
                      chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],
                          u[1],
                          u[2],
                          chr(12288)))

    
def main():
    uinfo = []
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

  
main()