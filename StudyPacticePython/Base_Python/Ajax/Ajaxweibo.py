#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 21:10
# @Author  : Paulson
# @File    : Ajaxweibo.py
# @Software: PyCharm
# @define  : function

# https://m.weibo.cn/u/2145291155
# url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155'
# url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155&page=2'

# url  参数     type value containerid page
from urllib.parse import urlencode
import requests
from  pyquery import PyQuery as pq
from pymongo import MongoClient


url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155&page=2'
base_url = 'https://m.weibo.cn/api/container/getIndex?'
# attitudes_count 点赞数
# comments_count  评论数
# reposts_count   转发数

client = MongoClient()
db = client['weibo']
collection = db['weibo']
max_page = 14

headers = {
    'referer': 'https://m.weibo.cn/u/2145291155',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page':page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        print(items)
        for item in items:
            item = item.get('mblog')
            print(item)
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['text'] = pq(item.get('text')).text()
            weibo['comments'] = item.get('comments_count')
            weibo['reports'] = item.get('reposts_count')
            yield weibo


def save_json(result):
    with open('ma.json','a',encoding='utf-8')as f:
        f.write(str(result)+'\n')

def sava_to_monge(result):
    if collection.insert(result):
        print('Save to Mongo')

if __name__ == '__main__':
    for page in range(1,15):
        json = get_page(page)
        results = parse_page(json)
        print(results)
        for result in results:
            print(result)
            save_json(result)
            sava_to_monge(result)
