#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/26 20:42
# @author: Paulson●Wier
# @file: python_有用的技巧.py
# @desc:

'''
 01 简洁的表达式
'''

# 快速构成一个字典序列

print(dict(zip('abc',range(4))))

# 推导列表生成字典
list1 = {(1,'a'),(2,'b')}
print({x[0] : x[1]} for x in list1)
print({x:y for x in range(4) for y in range(10,14)})

print([x/2 for x in range(10) if x%2 == 0])

print([x/2 for x in range(30) if x%2 == 0 and x%6 == 0])