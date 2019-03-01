#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/28 15:03
# @author: Paulson●Wier
# @file: 获取对象信息.py
# @desc:

# isinstance
'''
使用dir()
如果要获得一个对象的所有属性和方法，
可以使用dir()函数，它返回一个包含字符串的list，
比如，获得一个str对象的所有属性和方法：

'''

# lower()返回小写的字符串：
# >>> 'ABC'.lower()
# 'abc'


'''
过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

sum = obj.x + obj.y
就不要写：

sum = getattr(obj, 'x') + getattr(obj, 'y')
'''