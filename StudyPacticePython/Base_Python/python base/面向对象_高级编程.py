#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/28 16:38
# @author: Paulson●Wier
# @file: 面向对象_高级编程.py
# @desc:

'''
使用__slots__
如果我们想要限制实例的属性怎么办？
比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，
Python允许在定义class的时候，
定义一个特殊的__slots__变量，
来限制该class实例能添加的属性：
'''
# class Student(object):
#     __slots__ = ('name','age')  # 用tuple定义允许绑定的属性名称



'''
使用@property
在绑定属性时，如果我们直接把属性暴露出去，
虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
'''

# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must be 0~100')
#         self._score = value



'''
但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？
对于类的方法，装饰器一样起作用。
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
'''


# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must be 0~100')
#         self._score = value



# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    pass
