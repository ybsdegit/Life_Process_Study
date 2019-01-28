#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/1/23 18:06
# @author: Paulson●Wier
# @file: fanti.py
# @desc:
import requests
from lxml import etree

headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
def get_text(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        html = etree.HTML(response.content.decode())

        content  = html.xpath("//*[@id='container']/div/div/div[2]/table/tbody/tr/td/p/text()")
        return content
    else:
        return None


def sava_text(content):

    with open('繁难字.txt','w',encoding='utf-8') as f:
        for text in content:
            f.write(text)
            print(text)
            f.write('\n')




if __name__ == '__main__':
    url = 'http://www.zhaozi.cn/tool/shengpi.html'
    content = get_text(url)
    print(content)
    print(type(content))
    sava_text(content)
