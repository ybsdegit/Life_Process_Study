#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/7 10:18
# @author: Paulson●Wier
# @file: io.py
# @desc:

with open('userdict.txt','r',encoding='utf-8') as f:
    print(f.read())

# StringIO是在内存中读写str

# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。


import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
