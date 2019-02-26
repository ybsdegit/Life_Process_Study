#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/25 16:30
# @author: Paulson●Wier
# @file: 匿名函数.py
# @desc:当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

'''
关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''


# 请用匿名函数改造下面的代码：

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print(L)


a = list(filter(lambda x:x%2==1,range(1,20)))
print(a)