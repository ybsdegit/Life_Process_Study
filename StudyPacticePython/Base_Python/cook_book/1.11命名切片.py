#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/22 16:07
# @author: Paulson●Wier
# @file: 1.11命名切片.py
# @desc:

# 1.11 命名切片
'''
问题
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。

解决方案
假定你有一段代码要从一个记录字符串中几个固定位置提取出特定的数据字段
（比如文件或类似格式）：
'''

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# 内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。
# 比如：

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,4)
items[2:4]

b = items[a]
print(b)
items[a] = [10,11]
items
del items[a]
items

# 如果你有一个切片对象 a，你可以分别调用它的 a.start , a.stop , a.step 属性来获取更多的信息。
# 比如：

a = slice(5,50,2)
a.start
a.stop
a.step

'''
另外，你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序
列上，这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以
满足边界限制，从而使用的时候避免出现 IndexError 异常。比如：
'''

s = 'HelloWorld'
a.indices(len(s))