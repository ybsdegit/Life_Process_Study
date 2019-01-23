#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 22:41
# @Author  : Paulson
# @File    : 字符识别.py
# @Software: PyCharm
# @define  : function

import string

text = open('字符识别.txt').read()
print(text)

def my_solution(text):
    s = list(filter(lambda x: x in string.ascii_letters,text))
    print(s)

if __name__ == '__main__':
    my_solution(text)