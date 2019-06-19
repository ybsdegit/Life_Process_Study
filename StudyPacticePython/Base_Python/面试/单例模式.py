#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/13 11:18
# @author: Paulson●Wier
# @file: 单例模式.py
# @desc:

# 1. 使用 __new__ 方法：
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instace = orig.__new__(cls, *args, **kwargs)
        return cls._instace

class Myclass(Singleton):
    a = 1


# #  2. 使用闭包的方式：
#  def singleton(cls, *args, **kw):
#     instances = {}
#     def getinstance():
#         if cls not in instances:
#             instances[cls] = cls(*args, **kw)
#         return instances[cls]
#     return getinstance
#
#   @singleton
#   class MyClass:
#     pass