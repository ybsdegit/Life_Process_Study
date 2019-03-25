#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 20:46
# @Author  : Paulson
# @File    : 匹配邮箱.py
# @Software: PyCharm
# @define  : function
import re


def main():
    email = input('Please input a email address: ')
    # 如果在正则表达式中需要用到了某些普通的字符，比如 . ? 等，需要在他们前面加上反斜杠\,表示转义
    ret = re.match(r'[a-zA-Z_0-9]{4,20}@(163|126|foxmail|gmail|qq)\.com$',email)
    if ret:
        print('%s符合要求...',email)
    else:
        print('%s不符合要求...',email)


if __name__ == '__main__':
    while True:
        main()