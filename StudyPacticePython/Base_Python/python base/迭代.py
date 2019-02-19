#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/1/29 10:59
# @author: Paulson●Wier
# @file: 迭代.py
# @desc: 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。


# d = {'a': 1, 'b': 2, 'c': 3}
# for k,v in d.items():
#     print(k,':',v)


# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# from collections.abc import Iterable
# isinstance('abc',Iterable)
# print(isinstance('abc',Iterable))
#
#
# for x,y in {(1,1),(2,4),(3,9)}:
#     print(x,y)


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if L!=[]:
        min = L[0]
        max = L[0]
        for i in L:
            if max < i:
                max = i
            if min > i:
                min = i
        return min,max
    else:
         return (None,None)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')