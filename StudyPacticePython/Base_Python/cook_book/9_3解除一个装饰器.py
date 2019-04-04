#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/3 11:30
# @author: Paulson●Wier
# @file: 9_3解除一个装饰器.py
# @desc:

"""
问题
一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函
数。
解决方案
假设装饰器是通过 @wraps (参考 9.2 小节) 来实现的，那么你可以通过访问
__wrapped__ 属性来访问原始函数：
"""

from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y
