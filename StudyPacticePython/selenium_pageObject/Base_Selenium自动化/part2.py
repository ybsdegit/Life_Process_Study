#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/15 16:43
# @author: Paulson●Wier
# @file: part2.py
# @desc:
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def sava_csv(item):
    with open('image/jrtt.csv', 'a+', encoding='utf-8') as f:
        writer = csv.writer(f)
        try:
            writer.writerow(item)
        except:
            print('写入error')

def webdriver_wait(XPath):
    try:
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, XPath)))
    finally:
        driver.find_element_by_xpath(XPath).click()

def main():
    pass

def getinfo():
     id_ = driver.find_element_by_xpath('//*/div[@class="article-sub"]/span[1]')
     time_ = driver.find_element_by_xpath('//*/div[@class="article-sub"]/span[2]')
     title_ = driver.find_element_by_xpath('//*/h1[@class="article-title"]')
     text_ = driver.find_element_by_xpath('//*/div[@class="article-content"]')
     item = [id_.text,time_.text,title_.text,text_.text]
     return item


def top_search(value):
    url = "https://www.toutiao.com/search/?keyword={}".format(value)
    driver.get(url)

    now_handle = driver.window_handles

    # 刷新出足够的条数，保证加载到底
    # 这里循环次数尽量大
    # 经过测试，大概 1600 左右可以到低
    for i in range(2000):
        # 相当于一直按着 DOWN 键，下拉页面
        ActionChains(driver).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
        print(f'下拉已完成{i}次')

    # 再次留下时间加载，因为无法确定最后刷新到了哪一个，所以不用显式等待
    time.sleep(1)
    url_ = driver.find_elements_by_css_selector('.link.title')

    url_list = []
    for i in url_:
        url_list.append(i.get_attribute('href'))

    for i in url_list:
        try:
            driver.get(i)
            time.sleep(0.5)
            # print(getinfo())
            sava_csv(getinfo())
            driver.get(url)
            print(i+'写入成功')
        except:
            print('error')


    # xpath = '//*[@id="J_section_2"]/div/div/div[1]/div/div[1]/a/span'
    # webdriver_wait(xpath)
    time.sleep(2)  # 页面加载，防止被禁IP

    all_handles = driver.window_handles

    for handle in all_handles:
        if handle != now_handle:
            driver.switch_to.window(handle)

if __name__ == '__main__':
    url = 'http://top.baidu.com/'
    driver = webdriver.PhantomJS()
    # driver = webdriver.Chrome()
    driver.get(url)

    hw_dict = []
    top_elements = driver.find_elements_by_xpath('//ul[@id="hot-list"]/li/a[1]')
    for top_element in top_elements:
        value = top_element.get_attribute('title')
        hw_dict.append(value)

    # top_search(hw_dict[5])
    for x in hw_dict:
        print(x)
        top_search(x)
    driver.quit()
