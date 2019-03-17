#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/6 16:15
# @author: Paulson●Wier
# @file: 异常处理.py
# @desc:
import math
from functools import reduce

def str2num(s):
    if '.' in s:   #判断 是否有小数点
        return float(s)
    return int(s)

def calc(exp):
    if isinstance(exp,str):
        ss = exp.split('+')
        ns = map(str2num, ss)
    if isinstance(exp,float):
        ss = math.modf(exp)
        ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()