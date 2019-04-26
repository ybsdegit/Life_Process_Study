#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/19 11:52
# @author: Paulson●Wier
# @file: hash算法.py
# @desc:

import hashlib

# MD5 加密
md5_1 = hashlib.md5()
md5_1.update(b"i'm using md5 in python")
# md5_1.update(b"283848")
print(md5_1.hexdigest())

#如果数据量很大，可以分块多次调用 update()，最后计算的结果是一样的
md5_2 = hashlib.md5()
md5_2.update(b"i'm using md5")
md5_2.update(b' in python')
print(md5_2.hexdigest())

# SHA1 加密
sha_1 = hashlib.sha1()
sha_1.update(b"i'm using sha1 in python")
print(sha_1.hexdigest())