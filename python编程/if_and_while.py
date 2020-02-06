
spam = 0
if spam < 5:
    print("hello, world")
    spam = spam + 1

spam = 0
while spam < 5:
    print('hello, world')
    spam = spam + 1


print('My name is')
for i in range(5):
    print('Jimmy Five Time (' + str(i) + ') ' )
    
# python的字典中有一个函数get，可以检测键是否在字典中

a = {'apples':5,  'cups' : 2}

print('I am binging ' + str(a.get('cups', 0)) + ' cups')

print('I am binging ' + str(a.get('eggs', 0)) + ' eggs')
