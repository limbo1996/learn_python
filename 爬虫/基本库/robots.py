# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:54:52 2019
ref = 《python3网络爬虫实战》
@author: Limbo
"""
#分析robots协议
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
#从而可以判断哪些可以抓取，那些不可以抓取



