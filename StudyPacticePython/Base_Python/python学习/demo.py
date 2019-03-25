#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 22:35
# @Author  : Paulson
# @File    : demo.py
# @Software: PyCharm
# @define  : function
import random

import requests
from lxml import etree
import re

def get_html():
    with open('demo.html','r',encoding='utf-8') as f:
        html = f.read()

    result_html = etree.HTML(html)

    urllist = result_html.xpath('//*[@id="tab4FilesTable"]/tbody/tr/td[6]/div/a/@href')
    for url in urllist:
        print(url)
        filename = str(url)[-10:-5]
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename+'.hdf','wb') as f:
                f.write(response.content)
        else:
            print('url响应出错')



if __name__ == '__main__':
    get_html()