#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/22 17:32
# @author: Paulson●Wier
# @file: 返回函数.py
# @desc:
'''
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

'''

# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax +n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum



# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    s = [0]
    def counter():
        s[0] = s[0] + 1
        return  s[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')