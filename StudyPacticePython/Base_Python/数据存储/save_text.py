#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 11:29
# @Author  : yb.w
# @File    : save_text.py
import requests
from pyquery import PyQuery as pq
url = 'https://www.zhihu.com/explore'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = items.find('h2').text()