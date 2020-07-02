#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:41:59 2020

@author: limbo
"""
def find_max(S, n):
    if n == 1:
        return S[0]
    elif S[n] < find_max(S, n - 1): 
        return find_max(S, n - 1)
    else:
        return S[n]

def harmonic_mean(S, n):
    if n == 0:
        return (1 / S[n])
    else:
        return harmonic_mean(S, n - 1) + (1 / S[n])
    
    
def mean(S, n):
    if n == 0:
        return S[n]
    else:
        return (mean(S, n - 1) + S[n])
    
# 仅使用加法和减法，用递归算两数相乘
def x(a, b):
    if a | b == 0 :
        return 0
    elif a == 1:
        return b
    elif b == 1:
        return a
    else:
        return x(a - 1, b) + b

#  递归输出所有列表的子集
#  循环来求子集
def subsets(nums):
    result = [[]]
    for num in nums:
        for element in result[:]:
            x=element[:]
            x.append(num)
            result.append(x)        
    return result

S = [1, 2]

subsets(S)
s# 递归
def subsets_two(nums):
   if nums ==[]:
       return [[]]
   else:
       return subsets_two(nums[:-1]) + [i+[nums[-1]] for i in subsets_two(nums[:-1])]

subsets_two(S)
