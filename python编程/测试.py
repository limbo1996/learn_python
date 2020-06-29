#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:50:22 2020

@author: limbo
"""

if __name__ = '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman',
                             'California Savings',
                             '5390 0375 9387 5309',
                             2500))
    wallet.append(CreditCard('John Bowman',
                             'California Federal',
                             '3485 0399 3395 1954',
                             3500))
    wallet.append(CreditCard('John Bowman',
                             'California Finance',
                             '5391 0375 9387 5309',
                             5000))
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
        
    wallet[0].get_account()
    
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())    
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
            
            
            

