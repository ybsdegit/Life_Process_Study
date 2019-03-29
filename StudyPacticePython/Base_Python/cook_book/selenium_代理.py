#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/27 14:51
# @author: Paulson●Wier
# @file: selenium_代理.py
# @desc:

# # 然后执行此代码
# # 查看本机ip，查看代理是否起作用
import time

from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://117.21.144.165:5412")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://35.220.135.30:7890
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser = webdriver.Remote()

# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")
print(browser.page_source)
time.sleep(10)
# 退出，清除浏览器缓存
# browser.quit()
