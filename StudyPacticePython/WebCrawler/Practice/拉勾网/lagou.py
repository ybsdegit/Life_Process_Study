#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 22:54
# @Author  : Paulson
# @File    : lagou.py
# @Software: PyCharm
# @define  : function
import requests


class crawler():
    '''

    '''
    def __init__(self,url):
        self.url = url


    def get_html(self,url):
        response = requests.get(url)
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    url = ""
    crawler = crawler()
    crawler.get_html()
