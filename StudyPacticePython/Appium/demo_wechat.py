#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/1/21 15:30
# @author: Paulson●Wier
# @file: demo_wechat.py
# @desc:

# coding=utf-8
# coding=utf-8
# f350e2f7
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "f350e2f7",
        "appPackage": "com.tencent.mm",
        "appActivity": "com.tencent.mm.ui.LauncherUI",
        "noReset": True,
        "automationName": "Appium",
        "newCommandTimeout": "240",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_elements_by_id('com.tencent.mm:id/qr')[2].click()   #发现
time.sleep(5)
driver.find_elements_by_id('android:id/title')[0].click()       #打开朋友圈
time.sleep(3)
for i in range(10):
        TouchAction(driver).press(x=835, y=1679).move_to(x=637, y=387).release().perform()
        time.sleep(5)
driver.quit()

