#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 21:52
# @Author  : Paulson
# @File    : 1_安装demo.py
# @Software: PyCharm
# @define  : function

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.quit()