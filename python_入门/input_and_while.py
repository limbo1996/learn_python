# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:32:16 2019

@author: Limbo
"""

#输入和while循环
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

#当提示很长是可以先将提示存储到一个变量里
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, " + name + "!")
#int()获取数值输入
#input()会使输入作为字符串
age = input("How old are you?")
age
#使用函数Int()将字符串转换为数字
age = input("How old are you?")
age = int(age)
age > 18
#判断是否满足身高需求
height = input("How tall are you,in inches?")
height = int(height)
if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you are a little older.")
#while循环
#可以选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    if(message) != 'quit':
        print(message)
#使用标志
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

activate = True
while activate:
    message = input(prompt)
    
    if message == 'quit':
        activate = False
    else:
        print(message)
#使用break退出循环
prompt = "\nPlease enter a name of city you have visited: "
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd like to go to " + city.title() + "1")
#使用continue
#返回循环开头
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#########practice
prompt = "\nPlease enter something you want to put it in your pizza: "
prompt += "\n(Enter 'quit' when you are finished)"

while True:
    something = input(prompt)
    
    if something == 'quit':
        break
    else:
        print("\nFine, we will put " + something + " in your pizza !")

############practice
prompt = "\nPlease input your age and I'll tall you how much about movie"
prompt += "(\nEnter 'quit' when you are finish )"
age = input(prompt)
age = int(age)
if age <3:
    print("free!")
elif age <= 12:
    print(10)
else:
    print(15)


#用while循环处理列表和字典
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)


print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
#删除列表中的包含特定值的列表元素
pets = ['dog', 'cat' ,'cat', 'cat', 'dog']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

for pet in pets:
    if pet == 'cat':
        pets.remove(pet)
print(pets)

#使用用户输入来填充字典
responses = {}
polling_activate = True#设定一个标志

while polling_activate:
    #提示输入
    name = input("\nWhat is your name?")
    response = input("Which mountation would you like to climb someday?")
    #将答案储存在字典中
    responses[name] = response
    
    repeat = input("\nWould you balabalabal?")
    if repeat == 'no':
        polling_activate = False
#显示结果
print("\n----------POLL RESULTS----------")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".") 

#practice
sandwich_orders = ['green', 'yellow', 'blue']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("\nI made you order " + finished_sandwich + ".")
    finished_sandwiches.append(finished_sandwich)

print("\n-------result-------")
for sandwich in finished_sandwiches:
    print(sandwich.title())

































































