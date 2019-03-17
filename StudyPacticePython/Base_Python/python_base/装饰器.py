#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/25 17:11
# @author: Paulson●Wier
# @file: 装饰器.py
# @desc:在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
'''
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
'''

def log1(func):
    def wrapper(*args, **kw):  #wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# -*- coding: utf-8 -*-
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t1 = time.time()
        r = fn(*args,**kw)
        print('%s excute in %s ms' %(fn.__name__, 1000*(time.time()-t1)))
        return r
    return wrapper

@metric
def fast(x,y):
    return x*y

fast(3,5)

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
#
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 请编写一个decorator，
# 能在函数调用的前后打印出'begin call'和'end call'的日志。

def log3(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begin call %s():"%func.__name__)
        res=func(*args,**kw)
        print("the result of the program is {}".format(res))
        print("end call %s():"%func.__name__)
        #resturn res
    return wrapper

#########################################
@log3
def f():
    pass

@log3
def f3(x,y):
    return x+y


f3(4,6)
print("the name of the function is :"+f3.__name__)
