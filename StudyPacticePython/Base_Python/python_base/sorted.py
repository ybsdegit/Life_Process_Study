#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/22 17:20
# @author: Paulson●Wier
# @file: sorted.py
# @desc:

'''
排序算法

1. Python内置的sorted()函数就可以对list进行排序：
sorted([36, 5, -12, 9, -21])


2. sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
sorted([36, 5, -12, 9, -21], key=abs)

key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：




'''

# 假设我们用一组tuple表示学生名字和成绩：
#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)    # 请用sorted()对上述列表分别按名字排序：
L3 = sorted(L, key=by_score)   # 请用sorted()对上述列表分别按分数排序：
print(L2)
print(L3)