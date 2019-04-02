#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/1 17:55
# @author: Paulson●Wier
# @file: demo.py
# @desc:

import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%H:%S')) + '  星期：' + str(datetime.datetime.now().isoweekday())
print(a)