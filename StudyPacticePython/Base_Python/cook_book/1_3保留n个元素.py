#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 21:49
# @Author  : Paulson
# @File    : 1_3保留n个元素.py
# @Software: PyCharm
# @define  : function

'''
问题
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

解决方案
保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码 在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行：
'''

from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

#Example use on a file
if __name__ == '__main__':
    with open('1_3.txt',encoding='utf-8') as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)