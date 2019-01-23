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
from appium import webdriver

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



