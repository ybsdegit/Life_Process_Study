#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/4 11:06
# @author: Paulson●Wier
# @file: part1.py
# @desc:


from selenium import webdriver
# driver = webdriver.PhantomJS()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# 隐性等待设置一次对整个程序运行过程全部起作用，只要设置一次即可
driver.implicitly_wait(30)   # 设置隐式等待，最长等30s
driver.get("https://www.csdn.net/")
driver.maximize_window()

# 修改标题
JS1 = "document.title='test_test';"
driver.execute_script(JS1)
driver.save_screenshot("image/save.png")

# 弹窗显示现在的标题
# JS2=r"alert($(document).attr('title'));"
# driver.execute_script(JS2)

# 使用显示等待
try:
    """
    WebDriverWait()可选择的参数有四个，但一般情况下，我们只会用到其中三个，
    第一个参数设置的是打开的浏览器，
    第二个参数设置超时时间，
    第三个参数设置的是检查频率
    """
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, u'首页'))).click()
finally:
    print(driver.find_element_by_link_text(u'首页').get_attribute('href'))

driver.quit()
