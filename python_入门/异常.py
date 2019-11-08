# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#文件和异常
#异常是python创建的特殊对象
#用于管理系统出现的错误


#读取数据
#首先创建文件

with open('C:/Users/Limbo\Documents/GitHub/learn_python/python_入门/pi_digits.txt') as file_objects:
    contents = file_objects.read()
    print(contents)
    

#逐行读取
filename = 'C:/Users/Limbo\Documents/GitHub/learn_python/python_入门/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
#或者
filename = 'C:/Users/Limbo\Documents/GitHub/learn_python/python_入门/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#创建一个包含文件各行内容的列表
filename = 'C:/Users/Limbo\Documents/GitHub/learn_python/python_入门/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print(lines)


#使用文件内容
filename = 'C:/Users/Limbo\Documents/GitHub/learn_python/python_入门/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()#rstrip用于删除行末的换行符,strip用于删除位于循环每行左边的空格
    
print(pi_string)
print(len(pi_string))


#检测文件中是否包含特定数据
#首先产生一个包含一百万位的大型文件
#死机警告
#文件在ituring.cn/book/1861

#检查
#之前只是将pi保存为字符串，所以这里只需要输入你的生日保存为字符串，比较一下就好了



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#写入文件
filename = 'C:/Users/Limbo\Documents/GitHub/learn_python/python_入门/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")
    
#写入多行
#函数write不会在结尾添加换行符，所以如果想让字符串单独占一行，需要自己加换行符
filename = 'C:/Users/Limbo\Documents/GitHub/learn_python/python_入门/programming.txt'

with open(filename, 'w') as file_object:#需要传递实参'w'('r'读取, 'w'写入, 'a'附加),注意w模式下会清空原来的文件,写入这次的内容
    file_object.write("I love programming.\n")
    file_object.write("I LOVE creating new games.\n")
with open(filename) as read_file:
    contents = read_file.read()
    print(contents)

##附加到文件
#将写入的行添加到末尾
with open(filename, 'a') as add_file:
    add_file.write("I also love finding meaning in large datasets.\n")
    add_file.write("I love creating apps that can run in a browser.\n")


with open(filename) as read_file:
    contents = read_file.read()
    print(contents)


