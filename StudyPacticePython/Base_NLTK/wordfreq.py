#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/4 11:51
# @author: Paulson●Wier
# @file: wordfreq.py
# @desc:
'''
统计一段文字中的字符频率
'''

import sys

def wordfreq(mystring):
    print(mystring)
    word_freq= {}
    for tok in mystring.split():
        if tok in word_freq:
            word_freq [tok] += 1
        else:
            word_freq [tok] = 1
    print(word_freq)

if __name__ == '__main__':
    str = ' this is my first python program, and this is a python job'
    wordfreq(str)

