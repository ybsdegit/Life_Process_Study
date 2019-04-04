#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/3 11:38
# @author: Paulson●Wier
# @file: 9_4定义一个带参数的装.py
# @desc:

"""
问题
你想定义一个可以接受参数的装饰器

解决方案
我们用一个例子详细阐述下接受参数的处理过程。假设你想写一个装饰器，给函数
添加日志功能，同时允许用户指定日志的级别和其他的选项。下面是这个装饰器的定义
和使用示例：
"""

from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    添加日志功能
    :param level:
    :param name:
    :param message:
    :return:
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x: int, y: int) -> int:
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print("Spam!")
