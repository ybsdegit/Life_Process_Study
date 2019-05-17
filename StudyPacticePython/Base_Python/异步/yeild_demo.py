#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/16 9:42
# @author: Paulson●Wier
# @file: yeild_demo.py
# @desc:

# def gene():
#     for c in 'AB':
#         yield c
#     for i in range(3):
#         yield i

def gene():
    yield from 'AB'
    yield from range(3)

def chain(*args):
    for i in args:
        # for m in i:
        #     yield m
        yield from i

if __name__ == '__main__':
    p = list(chain("1234", "AB", [1, 2, 3, 4, 5]))
    print(p)