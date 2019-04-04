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
你想写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器
行为。
解决方案
引入一个访问函数，使用 nonlocal 来修改内部变量。然后这个访问函数被作为一
个属性赋值给包装函数。

"""

from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


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

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
        return  wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x: int, y: int) -> int:
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print("Spam!")
