#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/26 20:38
# @author: Paulson●Wier
# @file: 类和实例_习题.py
# @desc:

'''
练习
请把下面的Student对象的gender字段对外隐藏起来，
用get_gender()和set_gender()代替，并检查参数有效性
'''

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender


    def get_gender(self):
        return self.__gender


    def set_gender(self,gender):
        self.__gender = gender



# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

