#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/14 14:30
# @author: Paulson●Wier
# @file: 线程1让线程2去调用一个函数.py
# @desc:


import threading


def func1(t2):
    print('正在执行函数func1')
    t2.start()


def func2():
    print('正在执行函数func2')


if __name__ == '__main__':
    t2 = threading.Thread(target=func2)
    t1 = threading.Thread(target=func1, args=(t2,))
    t1.start()
