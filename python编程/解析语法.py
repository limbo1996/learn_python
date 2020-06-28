# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# print('hello, world')
# print('hello')

# 解析语法
# [expression for value in interable if condition]列表解析

# 例如求平方
# 传统的循环方式
def test(n):
    squares = []
    for k in range(1, n+1):
        squares.append(k*k)
    return(squares)

test(10)
# 使用列表解析
def test2(n):
    squares = [k*k for k in range(1, n+1)]
    return squares
test2(10)
# 其他解析式
# {k*k for k in range(1, n+1)}集合解析
# (k*k for k in range(1, n+1))生成器解析
# {k*k for k in range(1, n+1)}字典解析


squares = [k*(k+1) for k in range(0, 10)]
squares
