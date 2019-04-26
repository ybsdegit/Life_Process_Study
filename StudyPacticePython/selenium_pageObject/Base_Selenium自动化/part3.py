#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/19 14:38
# @author: Paulson●Wier
# @file: part3.py
# @desc: 猫眼原因


# for i in range(0,10):
#     x = i*10
#     print(x)
#
import csv
import time

from selenium import webdriver

L = [i * 10 for i in range(0, 10)]
print(L)

url_list = []
for i in L:
    url = "https://maoyan.com/board/4?offset={}".format(i)
    url_list.append(url)
    print("获取地址：{}".format(url))

# 打开浏览器
driver = webdriver.Chrome()

# 打开csv文件
csv_file = open("./file/top100.csv", 'w+', newline="", encoding='utf-8')
writer = csv.writer(csv_file)
header = ["title", "actor", "score", "url_now"]
writer.writerow(header)

# 循环调用url
print(url_list)
for url_now in url_list:
    driver.get(url_now)
    time.sleep(0.5)
    print('正在链接为{}的页面'.format(url_now))
    for j in range(1, 10):
        # 获取演员
        xpath2 = '//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[1]/p[2]' % j
        actor = driver.find_element_by_xpath(xpath2).text
        # 获取分数
        xpath3 = '//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[2]/p' % j
        score = driver.find_element_by_xpath(xpath3).text
        # 获取标题
        xpath1 = '//*[@id="app"]/div/div/div[1]/dl/dd[%d]/div/div/div[1]/p[1]/a' % j
        title = driver.find_element_by_xpath(xpath1).get_attribute('title')
        # 获取电影介绍
        driver.find_element_by_xpath(xpath1).click()
        xpath4 = '//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span'
        introduce = driver.find_element_by_xpath(xpath4).text

        # print('电影标题：%s' % title)
        # print("演员：%s" % actor)
        # print("分数：%s" % score)
        # print(introduce+"\n")
        #

        # 拼接
        text = []
        text.append(title)
        text.append(actor)
        text.append(score)
        text.append(url_now)

        # 写入CSV
        writer.writerow(text)
        print("---正在获取第{}条---".format(j))
        # 返回首页
        driver.get(url_now)
driver.close()
