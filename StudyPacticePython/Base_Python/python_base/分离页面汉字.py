#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/21 14:25
# @author: Paulson●Wier
# @file: 分离页面汉字.py
# @desc:
import time

from selenium import webdriver
import re

driver = webdriver.Chrome()

def get_pageSourse(url):
    driver.get(url)
    time.sleep(5)
    content = driver.page_source
    print(content)
    return content

def get_Chinese(content):
    line = content.strip()
    p2 = re.compile(r'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    zh = " ".join(p2.split(line)).strip()
    zh = ",".join(zh.split())
    outStr = zh  # 经过相关处理后得到中文的文本
    print(outStr)
    return outStr


    # page_chinese = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", content)
    # print(page_chinese)


if __name__ == '__main__':
    url = "https://uat.95303.com/"
    content = get_pageSourse(url)
    get_Chinese(content)
    driver.quit()