#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/11 17:09
# @author: Paulson●Wier
# @file: baidu_news_crawer.py
# @desc:

import urllib.parse as urlparse
import lzma
import farmhash
'''
farmhash是Google开源的一个hash算法。64位的hash空间有2的64次方那么大，大到随意把url映射为一个64位无符号整数，也不会出现hash碰撞。
'''
import traceback

from ezpymysql import Connection
from urlpool import UrlPool
import functions as fn
import config

class NewsCrawlerSync:
    def __init__(self, name):
        self.db = Connection(
            config.db_host,
            config.db_db,
            config.db_user,
            config.db_password
        )
        self.logger = fn.init_file_logger(name + '.log')
        self.urlpool = UrlPool(name)
        self.hub_hosts = None
        self.load_hubs()

    def load_hubs(self):
        sql = 'select url from crawler_hub'
        data = self.db.query(sql)
        self.hub_hosts = set()
        hubs = []
        for d in data:
            host = urlparse.urlparse(d['url']).netloc
            self.hub_hosts.add(host)
            hubs.append(d['url'])
        self.urlpool.set_hubs(hubs, 300)

    def save_to_db(self, url, html):
        urlhash = farmhash.hash64(url)
        sql = 'select url from crawler_html where urlhash=%s'
        d = self.db.get(sql, urlhash)
        if d:
            if d['url'] != url:
                msg = 'farmhash collision: %s <=> %s' % (url, d['url'])
                self.logger.error(msg)
            return True
        if isinstance(html, str):
            html = html.encode('utf8')
        html_lzma = lzma.compress(html)
        sql = ('insert into crawler_html(urlhash, url, html_lzma) '
               'values(%s, %s, %s)')
        good = False
        try:
            self.db.execute(sql, urlhash, url, html_lzma)
            good = True
        except Exception as e:
            if e.args[0] == 1062:
                # Duplicate entry
                good = True
                pass
            else:
                traceback.print_exc()
                raise e
        return good

    def filter_good(self, urls):
        goodlinks = []
        for url in urls:
            host = urlparse.urlparse(url).netloc
            if host in self.hub_hosts:
                goodlinks.append(url)
        return goodlinks

    def process(self, url, ishub):
        status, html, redirected_url = fn.downloader(url)
        self.urlpool.set_status(url, status)
        if redirected_url != url:
            self.urlpool.set_status(redirected_url, status)
        # 提取hub网页中的链接, 新闻网页中也有“相关新闻”的链接，按需提取
        if status != 200:
            return
        if ishub:
            newlinks = fn.extract_links_re(redirected_url, html)
            goodlinks = self.filter_good(newlinks)
            print("%s/%s, goodlinks/newlinks" % (len(goodlinks), len(newlinks)))
            self.urlpool.addmany(goodlinks)
        else:
            self.save_to_db(redirected_url, html)

    def run(self, ):
        while True:
            urls = self.urlpool.pop(5)
            for url, ishub in urls.items():
                self.process(url, ishub)

if __name__ == '__main__':
    crawler = NewsCrawlerSync('yuanrenxyue')
    crawler.run()