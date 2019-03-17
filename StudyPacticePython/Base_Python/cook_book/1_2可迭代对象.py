#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 21:31
# @Author  : Paulson
# @File    : 1_2可迭代对象.py
# @Software: PyCharm
# @define  : function

records = [ ('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4), ]

def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

items = [1, 10, 7, 4, 5, 9]


# 递归
def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head


if __name__ == '__main__':
    url = ''
    s = sum(items)