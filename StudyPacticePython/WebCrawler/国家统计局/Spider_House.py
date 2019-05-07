#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/6 16:57
# @author: Paulson●Wier
# @file: Spider_House.py
# @desc:
import pandas

import lxml.html

import requests

resp = requests.get('http://www.stats.gov.cn/tjsj/zxfb/201904/t20190416_1659682.html')
resp.encoding = resp.apparent_encoding
doc = lxml.html.fromstring(resp.text)

tables = doc.xpath('//table[@class="MsoNormalTable"]')
html = lxml.html.tostring(tables[0], encoding='utf-8').decode('utf-8')
print(html)

df = pandas.read_html(html)[0]
print(df)