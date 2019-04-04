#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/4 10:18
# @author: Paulson●Wier
# @file: phantomJs_demo1.py
# @desc:

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://cn.bing.com/")
titile = driver.title
print(titile)

keywords = 'SELENIUM 自动化测试'
driver.find_element_by_id("sb_form_q").send_keys(keywords)
# driver.save_screenshot("bing_1.png")  # 截图
driver.quit()  # 会自动删除临时文件夹
driver.close()   # 不会清除临时文件中的webdriver临时文件

