#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/21 15:55
# @author: Paulson●Wier
# @file: 一组元素.py
# @desc:

import random
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
a = driver.find_element_by_id('kw')
a.send_keys(u"测试部落")
driver.implicitly_wait(10)
a.submit()
s = driver.find_elements_by_css_selector("h3.t>a")#定位好哦
x = s.__len__()
print("x:",x)
print(s)
#获取href属性，打印出url地址
for i in s:
    print(i.get_attribute('href'))
#设置随机值
t = random.randint(0,x)
print(t)
