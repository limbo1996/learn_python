# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 10:56:52 2019

@author: Limbo
"""

#函数
def greet_user():
    """显示简单的问候语"""
    print('hello')

greet_user()
#向函数传递信息
def greet_user(username):
    print("Hello, " + username.title() + "!")
greet_user('wangxuan')
#practice
def favorite_book(title):
    print("One of my favorite book is " + title.title() + ".")
favorite_book('Alice in Wonderland')
#传递实参的顺序
#位置实参
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("hamster", "harry")
#关键字实参
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='harry', animal_type='hamster')
#默认值
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='whillie')
#虽然有默认值但是当只给出一个实参而有默认值的形参没有输入时，python会将其是为位置实参，所以pet_name需要放在前面
def describe_pet(pet_name, animal_type='dog'): 
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='whillie')



#返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('wang', 'xuan')
print(musician)
#让实参变成可选的
#可以使用默认值来让实参变得可选
def get_formatted_name(first_name, last_name, middle_name = ' '):
    #判断有没有中间名
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name+ ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
#返回字典
def build_person(first_name, last_name):
    """返回包含一个人信息的字典"""
    person = {'first':first_name, 'last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
#储存年龄
def build_person(first_name, last_name, age = ''):
    """返回包年龄的人的信息字典"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'henderix')
print(musician)
musician = build_person('jimi', 'henderix', 17)
print(musician)
#函数结合while循环
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name =  get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
#practice 
def musics(singer_name, music_name):
    music = {'singer_name':singer_name, 'music_name':music_name}
    return music

while True:
    print("\nPlease tell me your favorite singer and the song ")
    print("(Enter 'q' at any times to quit)")
    s_name = input("singer name: ")
    if s_name == 'q':
        break
    m_name = input("music name: ")
    if m_name == 'q':
        break
    full_informate = musics(s_name, m_name)
    print(full_informate)
    for s, m in full_informate.items():
        print("\nThe " + s + "is: " + m)
        
    
#向函数传递列表
def greet_users(names):
   for name in names:
        msg = "\nHello, " + name.title() + "!"
        print(msg)
usernames = ['wang', 'xuan', 'he', 'pei']
greet_users(usernames)


#在函数中修改列表
#不使用函数
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_desgins = unprinted_designs.pop()
    print("\nPrinting models : " + current_desgins)
    completed_models.append(current_desgins) 
print("\nThe folowing models have been printde: ")
for completed_model in completed_models:
    print(completed_model)
    
    
    
#使用函数
def print_models(unprinted_desigens, completed_models):
   while unprinted_designs:
    current_desgins = unprinted_designs.pop()
    print("\nPrinting models : " + current_desgins)
    completed_models.append(current_desgins)
   print("\nThe folowing models have been printde: ")
   for completed_model in completed_models:
    print(completed_model)
 
       
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)    
    
#禁止函数更改列表
#即保留原来的列表而不是清空， 可以向函数传递列表的副本
def print_models(unprinted_desgens, completed_models):
   while unprinted_desgens:
        current_desgin = unprinted_desgens.pop()
        print("\nPrinting models: " + current_desgin)
        completed_models.append(current_desgin)
   print("\nThe folowing models have been printed: ")
   for completed_model in completed_models:
      print(completed_model)  
 
b = ['iphone case', 'robot pendant', 'dodecahedron']
c = []
print_models(b[:], c)  


#传递任意数量的实参
def make_pizza(*topping):
    print(topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#也可以添加循环
def make_pizza(*toppings):
    print("\nMake a piza with the following toppings: ")
    for topping in  toppings:
        print("- " + topping) 
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#结合位置实参和任意数量实参
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni")
make_pizza(12, "mushroom", "green pepper")

#使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', lacation = 'princeton', field = 'physics')
print(user_profile)



############################
#将函数储存在模块中
import pizza


pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    