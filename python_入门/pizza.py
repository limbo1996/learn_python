# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:58:04 2019

@author: Limbo
"""
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)