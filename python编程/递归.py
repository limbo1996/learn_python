# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 菲波那切数列
def bad_fibonacc(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacc(n - 2) + bad_fibonacc(n - 1))
# 这样的算法得到的结果是指数级的增长

# 递归求和 O(n)
def linear_sum(S, n):
    if n == 0:
        return 0 
    else:
        return linear_sum(S, n - 1) + S[n - 1]


S = [1, 2, 3, 4, 5]

linear_sum(S, 5)

# 递归逆序列 O(n)
def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)
        
D = reverse(S, 0, 5)
# 计算幂
# 计算幂分两种情况， 幂上是0是不管底数是什么都是1
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    
power(11, 0)


# 二路递归
# 二路递归求和 O(log n)
def binary_sum(S, start, stop):
    if start > stop:
        return 0  # 没有元素
    if start = stop - 1:
        return S[start] # 一个元素
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
        
