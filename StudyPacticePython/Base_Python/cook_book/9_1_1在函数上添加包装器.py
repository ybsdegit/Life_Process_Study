#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/3 10:40
# @author: Paulson●Wier
# @file: 9_1在函数上添加包装器.py
# @desc:

"""
问题
你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文
档字符串、注解和参数签名都丢失了。
解决方案
任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来
注解底层包装函数。例如：
"""

import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(start)
        result = func(*args, **kwargs)
        end = time.time()
        print(end)
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n):
    """
    Counts down
    :param n:
    :return:
    """
    while n > 0:
        n -= 1


# countdown(100000)

"""
讨论
一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数。当你像下面这样写
"""
