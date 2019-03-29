#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/26 19:59
# @author: Paulson●Wier
# @file: 4.py
# @desc:

def manual_iter():
    with open('1_3.txt',encoding='utf-8') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

def manual_iter1():
    '''
    通常来讲，StopIteration 用来指示迭代的结尾。然而，如果你手动使用上面演示
    的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None 。下面是
    示例：
    :return:
    '''
    with open('1_3.txt',encoding='utf-8') as f:
        while True:
            line = next(f,None)
            if line is None:
                break
            print(line,end="")

'''
讨论
大多数情况下，我们会使用 for 循环语句用来遍历一个可迭代对象。但是，偶尔也
需要对迭代做更加精确的控制，这时候了解底层迭代机制就显得尤为重要了。
'''
# manual_iter1()

# 4.6 带有外部状态的生成器函数
'''
问题
你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值。
解决方案
如果你想让你的生成器暴露外部状态给用户，别忘了你可以简单的将它实现为一
个类，然后把生成器函数放到 __iter__() 方法中过去。比如：
'''

from collections import deque


class linehistory:

    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('1_3.txt', encoding='utf-8') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}{}'.format(lineno, hline), end='')
