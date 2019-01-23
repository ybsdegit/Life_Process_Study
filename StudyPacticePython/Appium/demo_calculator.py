#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 23:08
# @Author  : Paulson
# @File    : demo_calculator.py
# @Software: PyCharm
# @define  : function
import time

from appium import webdriver

desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "f350e2f7",
        "appPackage": "com.oneplus.calculator",
        "appActivity": ".Calculator",
        "noReset": True,
        "automationName": "Appium",
        "newCommandTimeout": "240",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id('com.oneplus.calculator:id/digit_7').click()
driver.find_element_by_id('com.oneplus.calculator:id/digit_6').click()
driver.find_element_by_id('com.oneplus.calculator:id/digit_5').click()
driver.find_element_by_id('com.oneplus.calculator:id/digit_4').click()
driver.find_element_by_id('com.oneplus.calculator:id/op_add').click()
driver.find_element_by_id('com.oneplus.calculator:id/digit_7').click()
driver.find_element_by_id('com.oneplus.calculator:id/digit_6').click()
driver.find_element_by_id('com.oneplus.calculator:id/digit_5').click()
driver.find_element_by_id('com.oneplus.calculator:id/eq').click()


time.sleep(10)

