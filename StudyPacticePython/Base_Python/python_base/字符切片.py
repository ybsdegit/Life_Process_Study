#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/1/29 10:33
# @author: Paulson●Wier
# @file: 字符切片.py
# @desc:利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(s):
    # for i in s:
    #     if i == ' ':
    #         r = s[i:]


    r = s[:2]
    if r == "  ":
        return s[2:]
    t = s[-2:]
    if t == '  ':
        return s[0:-2]



# 测试:
s = trim("hello  ")
print(s)
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')