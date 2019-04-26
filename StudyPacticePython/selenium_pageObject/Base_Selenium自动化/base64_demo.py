#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/19 11:35
# @author: Paulson●Wier
# @file: base64_demo.py
# @desc:

import base64

# 定义字符串
string = b'qweq'

# encode 表示解码， decode表示解码
encoded = base64.b64encode(string)
decoded = base64.b64decode(string)

print(encoded)
print(decoded)