# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:30:45 2019

@author: Limbo
"""

#类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('whille', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old")

#调用方法
my_dog = Dog('wille', 6)
my_dog.sit()
my_dog.roll_over()


#创建多个实例
my_dog = Dog('wille', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")


#Car类
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#给类指定默认值
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
    
#修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


#通过方法修改属性的值

#在类中添加一个方法可以修改特定属性

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        #修改里程值
        self.odometer_reading = mileage
        
my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#对方法扩展，防止回调
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        #修改里程值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll it back")

my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(22)
my_new_car.read_odometer()


my_new_car.update_odometer(24)
my_new_car.read_odometer()



#通过方法堆属性的值进行递增

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        #修改里程值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll it back")
            
    def increment_odometer(self, mile):
        """将里程增加相应的量"""
        self.odometer_reading += mile


my_new_car = Car('audi', 'a4', 2016)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

##########################################
#继承
class Car():#父类
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        #修改里程值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll it back")
            
    def increment_odometer(self, mile):
        """将里程增加相应的量"""
        self.odometer_reading += mile

class ElectricCar(Car):#子类
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
            
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())            
            

#给子类定义属性和方法
class Car():#父类
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        #修改里程值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll it back")
            
    def increment_odometer(self, mile):
        """将里程增加相应的量"""
        self.odometer_reading += mile

class ElectricCar(Car):#子类
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describle_battery(self):
        """在子类中新添加一个描述电池的属性"""
        print("This car has a " + str(self.battery_size) + "-kwh battery")
 
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())   
my_tesla.describle_battery()





#将实例用作属性
#将一个大类分成好多小类
class Car():#父类
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        #修改里程值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll it back")
            
    def increment_odometer(self, mile):
        """将里程增加相应的量"""
        self.odometer_reading += mile

            
class Battery():#新类，没有继承任何类
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
        
        
    def describle_battery(self):
        print("This car has a " + str(self.battery_size) + "-keh battery")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles an a full charge."
        print(message)
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model,year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())   
my_tesla.battery.describle_battery()   
my_tesla.battery.get_range()







































