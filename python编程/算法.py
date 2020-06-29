#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:17:45 2020

算法

@author: limbo
"""
from time import time

start_time = time()

end_time = time()

run = end_time - start_time

# 递归
## 阶乘的递归实现
def factoria(n):
    if n == 0:
        return 1
    else:
        return n * factoria(n - 1)      #重复调用自身
s
## 二分查找
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]: # low 和 high 都是data的索引
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


data = [1, 2, 3, 4, 5, 6,7,8]
