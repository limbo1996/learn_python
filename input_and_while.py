# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
print('hello, world')
#求模运算符
#即两数相除返回余数
4 % 3
#可以判断奇偶性
number = input("Enter a number, and I'll tell you it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odds.")

#while循环
#for循环适合对于集合中的每个元素的代码块，而while循环会不断循环，知道指定的条件不满足为止
#用while数数
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#while循环可以选择什么时候退出
