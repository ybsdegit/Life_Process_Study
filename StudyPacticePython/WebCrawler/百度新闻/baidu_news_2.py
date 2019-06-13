#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/10 18:00
# @author: Paulson●Wier
# @file: baidu_news_1.py
# @desc:
import time
import traceback
import cchardet
import requests
from urllib.parse import urlparse, urlunparse
import re
# import tldextract
'''
tldextract准确地从URL的域名和子域名分离通用顶级域名或国家顶级域名。
tld = tldextract.extract('http://news.baidu.com/')
> subdomain='news', domain='baidu', suffix='com'
'''

# g_bin_postfix = set(['exe', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx','pdf','jpg', 'png', 'bmp', 'jpeg', 'gif','zip', 'rar', 'tar', 'bz2', '7z', 'gz','flv', 'mp4', 'avi', 'wmv', 'mkv','apk',])
g_bin_postfix = ['exe', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx','pdf','jpg', 'png', 'bmp', 'jpeg', 'gif','zip', 'rar', 'tar', 'bz2', '7z', 'gz','flv', 'mp4', 'avi', 'wmv', 'mkv','apk']

g_news_postfix = [
    '.html?', '.htm?', '.shtml?',
    '.shtm?',
]


def clean_url(url):
    # 1. 是否为合法的http url
    if not url.startswith('http'):
        return ''
    # 2. 去掉静态化url后面的参数
    for np in g_news_postfix:
        p = url.find(np)
        if p > -1:
            p = url.find('?')
            url = url[:p]
            return url
    # 3. 不下载二进制类内容的链接
    up = urlparse(url)
    path = up.path
    if not path:
        path = '/'
    postfix = path.split('.')[-1].lower()
    if postfix in g_bin_postfix:
        return ''

    # 4. 去掉标识流量来源的参数
    # badquery = ['spm', 'utm_source', 'utm_source', 'utm_medium', 'utm_campaign']
    good_queries = []
    for query in up.query.split('&'):
        qv = query.split('=')
        if qv[0].startswith('spm') or qv[0].startswith('utm_'):
            continue
        if len(qv) == 1:
            continue
        good_queries.append(query)
    query = '&'.join(good_queries)
    url = urlunparse((
        up.scheme,
        up.netloc,
        path,
        up.params,
        query,
        ''  #  crawler do not care fragment
    ))
    return url


