#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 21:53
# @Author  : Paulson
# @File    : 豆瓣_1.py
# @Software: PyCharm
# @define  : function
import requests
from lxml import etree
from lxml.etree import Element

class Proxy(object):
    _instance = None
    def __new__(cls, proxyfile):
        if not isinstance(cls._instance,cls):
            cls._instance = super(Proxy,cls).__new__(cls)
            with open(proxyfile) as f:
                content = f.read()
                lines = content.split("\n")
                cls._instance._proxies = lines[:-1]
                cls._instance._curr = 0
        return cls._instance

    def get_proxy(self):
        idx = self._curr % len(self._proxies)
        proxy = self._proxies[idx]
        self._curr += 1
        return proxy

def get_books_by_page(tag,page_no):
    start = page_no * 20
    url = "https://book.douban.com/tag/{}?start={}&type=T".format(tag,page_no)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    inst = Proxy("可用代理IP.txt")
    proxy = inst.get_proxy()
    try:
        r = requests.get(url,headers=headers,proxies={"https": proxy},timeout=10)
        content = r.content.decode('utf-8')
        root = etree.HTML(content)
        items = root.xpath('.//li[@class="subject-item"]')
        print(r.status_code,len(items))
        print(proxy)

        books=[]
        for item in items:
            title_node = item.xpath('.//div[@class="info"]/h2/a')
            name = item.xpath('.//div[@class="info"]/h2/a/@title')
            url = item.xpath('.//div[@class="info"]/h2/a/@href')
            books.append({"name":name,"url":url})
        return books
    except Exception as e:
        msg = str(e)
        print(msg)
        return []

if __name__ == '__main__':
    tags = ["SQL","数据分析","计算机"]
    for tag in tags:
        page_no = 0
        while True:
            books = get_books_by_page(tag,page_no)
            print(books)
            if len(books) < 20:
                print(len(books))
                # break
            page_no+=1
