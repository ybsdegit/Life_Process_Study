#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 21:33
# @Author  : Paulson
# @File    : douban250.py
# @Software: PyCharm
# @define  : function

# coding：utf-8

import requests
from pyquery import PyQuery as pq
import json
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.douban
collection = db.douban250


def get_html(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def get_content(html):
    doc = pq(html)
    image_srl = doc('.pic a').find('img').attr('src')
    title = doc('.hd .title').text()
    for i in title:
        print(i)
        collection.insert_one(i)
    # print(title)
    # rating_num = doc('.rating_num').text()
    # print(rating_num)
    # comment = doc('.star span')
    # print(comment)
    # print(image_srl)
    return title





if __name__ == '__main__':
    for i in range(10):
        number = i * 25
        url = "https://movie.douban.com/top250?start={}&filter=".format(number)
        html = get_html(url)
    # url = "https://movie.douban.com/top250?start=25&filter="
    # html = get_html(url)
        title = get_content(html)
