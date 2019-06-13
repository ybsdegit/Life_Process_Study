#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/10 18:00
# @author: Paulson●Wier
# @file: baidu_news_1.py
# @desc:
import time

import requests
import re
# import tldextract
'''
tldextract准确地从URL的域名和子域名分离通用顶级域名或国家顶级域名。
tld = tldextract.extract('http://news.baidu.com/')
> subdomain='news', domain='baidu', suffix='com'
'''


def save_to_db(url, html):
    # 保存网页到数据库，暂时用打印相关信息代替
    print(f'{url}: {len(html)}')


def cravl():
    # 1. download baidu news
    hub_url = 'http://news.baidu.com/'
    res = requests.get(hub_url)
    html = res.text

    # 2. extract news link
    links = re.findall(r'href="(.*?)"', html)
    # print(links)
    print('find links:', len(links))
    news_links = []
    # 2.1 filter non-news link
    for link in links:
        if not link.startswith('http'):
            continue
        # tld = tldextract.extract(link)
        # if tld.domain == 'baidu':
        #     continue
        if link.endswith('baidu.com/'):
            continue
        news_links.append(link)

    print('find news links:', len(news_links))
    # print(news_links)
    # 3. download news and save to database
    for link in news_links:
        html = requests.get(link).text
        save_to_db(link, html)
    print('works done!')


def main():
    while True:
        cravl()
        time.sleep(300)


if __name__ == '__main__':
    main()
