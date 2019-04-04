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


def test():
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        # com.tencent.mm:id/r4
        driver.find_elements_by_id('com.tencent.mm:id/r4')[2].click()  # 发现
        time.sleep(3)
        driver.find_elements_by_id('android:id/title')[0].click()  # 打开朋友圈
        time.sleep(3)
        for i in range(100):  # 循环滑动100次，点赞。
                try:
                        TouchAction(driver).press(x=530, y=350).move_to(x=530, y=300).release().perform()
                        time.sleep(3)
                        for i in range(3):
                                driver.find_elements_by_id('com.tencent.mm:id/ee2')[i].click()  # 朋友圈评论按钮
                                time.sleep(1)
                                driver.find_elements_by_id('com.tencent.mm:id/ee2')[i].click()  # 朋友圈评论按钮
                        # driver.find_elements_by_id('com.tencent.mm:id/ejf')[1].click()  # 朋友圈点赞
                                time.sleep(2)
                except Exception as e:
                        msg = str(e)
                        print(msg)
        driver.quit()


if __name__ == '__main__':
    test()
