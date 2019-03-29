#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/27 14:27
# @author: Paulson●Wier
# @file: 4_8 跳过可迭代对象的开始部分.py
# @desc:

'''
问题
你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
解决方案

itertools 模块中有一些函数可以完成这个任务。首先介绍的是 itertools.
dropwhile() 函数。使用时，你给它传递一个函数对象和一个可迭代对象。它会返
回一个迭代器对象，丢弃原有序列中直到函数返回 Flase 之前的所有元素，然后返回后
面所有元素。
'''
# 为了演示，假定你在读取一个开始部分是几行注释的源文件。比如

# with open('1_3.txt', encoding='utf-8') as f:
#     for line in f:
#         print(line,end='')

# 如果你想跳过开始部分的注释行的话，可以这样做：
from itertools import dropwhile
with open('1_3.txt', encoding='utf-8') as f:
    for line in dropwhile(lambda line: line.startswith('#'),f):
        print(line,end='')

