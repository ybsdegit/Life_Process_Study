#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/22 11:39
# @author: Paulson●Wier
# @file: 函数式编程.py
# @desc:

'''
高阶函数(变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。)

1. 函数本身也可以赋值给变量，即：变量可以指向函数。
f = abs
'''

#一个最简单的高阶函数
def add(x,y,f):
    return f(x) + f(y)
s = add(-5,6,abs)
print(s)

'''
x = -5
y = 6
f = abs
f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
return 11
'''

'''

编写高阶函数，就是让函数的参数能够接收别的函数。

小结
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

'''


