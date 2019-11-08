# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:11:26 2019

@author: Limbo
"""

#导入类
#可以将类储存在模块中
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['wang'] = 'c'
favorite_languages['xuan'] = 'python'


for name, language in favorite_languages.items():
    print(name.title() + "'s facorite language is " + 
          language.title() + '.')
