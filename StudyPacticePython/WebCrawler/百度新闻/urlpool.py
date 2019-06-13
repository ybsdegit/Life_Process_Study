#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/11 11:25
# @author: Paulson●Wier
# @file: urlpool.py
# @desc:
import pickle
import time
import urllib.parse as urlparse


class UrlDB:
    """
    use LevelDB to store URLs what have been down(succeed or failed)
    """
    status_failure = b'0'
    status_success = b'1'

    def __init__(self, db_name):
        self.name = db_name + '.urldb'
        self.db = leveldb.LevelDB(self.name)

    def load_from_db(self, status):
        urls = []
        for url, _status in self.db.RangeIter():
            if status == _status:
                urls.append(url)
        return urls

    def set_success(self, url):
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            self.db.Put(url, self.status_success)
            s = True
        except:
            s = False
        return s

    def set_failure(self, url):
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            self.db.Put(url, self.status_failure)
            s = True
        except:
            s = False
        return s

    def has(self, url):
        if isinstance(url, str):
            url = url.encode('utf8')
        try:
            attr = self.db.Get(url)
            return attr
        except:
            pass
        return False


class UrlPool:
    """URL Pool fro crawler to manage URLS"""

    def __init__(self, pool_name):
        self.name = pool_name
        self.db = UrlDB(pool_name)

        self.pool = {}  # host: set([urls]), 记录待下载URL
        self.pending = {}  # url: pended_time, 记录已被pend但还未被更新状态（正在下载）的URL
        self.failure = {}  # url：times, 记录失败的URL的次数
        self.failure_threshold = 3
        self.pending_threshold = 60  # pending 的最大时间，过期要重新下载
        self.in_mem_count = 0
        self.max_hosts = ['', 0]  # [host: url_count] 目前pool中url最多的host及其url数量
        self.hub_pool = {}  # {url: last_query_time}
        self.hub_refresh_span = 0
        self.load_cache()

    def load_cache(self):
        """
        load_cache() 在 init()中调用，创建pool的时候，尝试去加载上次退出时缓存的URL pool；
        :return:
        """
        path = self.name + '.pkl'
        try:
            with open(path, 'rb') as f:
                self.pool = pickle.load(f)
            cc = [len(v) for k, v in self.pool]
            print('save pool loaded! urls: ', sum(cc))
        except:
            pass

    def set_hubs(self, urls, hub_refresh_span):
        self.hub_refresh_span = hub_refresh_span
        self.hub_pool = {}
        for url in urls:
            self.hub_pool[url] = 0

    def set_status(self, url, status_code):
        if url in self.pending:
            self.pending.pop(url)

        if status_code == 200:
            self.db.set_success(url)
            return
        if status_code == 404:
            self.db.set_failure(url)
            return
        if url in self.failure:
            self.failure[url] += 1
            if self.failure[url] > self.failure_threshold:
                self.db.set_failure(url)
                self.failure.pop(url)
            else:
                self.add(url)
        else:
            self.failure[url] = 1

    def push_to_pool(self, url):
        host = urlparse.urlparse(url).netloc
        if not host or '.' not in host:
            print('try to push_to_pool with bad url:', url, ', len of ur:', len(url))
            return False
        if host in self.pool:
            if url in self.pool[host]:
                return True
            self.pool[host].add(url)
            if len(self.pool[host]) > self.max_hosts[1]:
                self.max_hosts[1] = len(self.pool[host])
                self.max_hosts[0] = host
        else:
            # self.pool[host] = set([url])
            self.pool[host] = {url}
        self.in_mem_count += 1
        return True

    def add(self, url, always):
        if always:
            return self.push_to_pool(url)
        pended_time = self.pending.get(url, 0)
        if time.time() - pended_time < self.pending_threshold:
            print('being downloading:', url)
            return
        if self.db.has(url):
            return
        if pended_time:
            self.pending.pop(url)
        return self.push_to_pool(url)

    def addmany(self, urls, always=False):
        if isinstance(urls, str):
            print('urls is a str !!!!', urls)
            self.add(urls, always)
        else:
            for url in urls:
                self.add(url, always)

    def pop(self, count, hubpercent=50):
        print('\n\tmax of host:', self.max_hosts)

        # 取出的url有两种类型：hub=1, 普通=2
        url_attr_url = 0
        url_attr_hub = 1
        # 1. 首先取出hub，保证获取hub里面的最新url.
        hubs = {}
        hub_count = count * hubpercent // 100
        for hub in self.hub_pool:
            span = time.time() - self.hub_pool[hub]
            if span < self.hub_refresh_span:
                continue
            hubs[hub] = url_attr_hub  # 1 means hub-url
            self.hub_pool[hub] = time.time()
            if len(hubs) >= hub_count:
                break

        # 2. 再取出普通url
        # 如果某个host有太多url，则每次可以取出3（delta）个它的url
        if self.max_hosts[1] * 10 > self.in_mem_count:
            delta = 3
            print('\tset delta:', delta, ', max of host:', self.max_hosts)
        else:
            delta = 1
        left_count = count - len(hubs)
        urls = {}
        for host in self.pool:
            if not self.pool[host]:
                # empty_host.append(host)
                continue
            if self.max_hosts[0] == host:
                while delta > 0:
                    url = self.pool[host].pop()
                    self.max_hosts[1] -= 1
                    if not self.pool[host]:
                        break
                    delta -= 1
            else:
                url = self.pool[host].pop()
            urls[url] = url_attr_url
            self.pending[url] = time.time()
            if len(urls) >= left_count:
                break
        self.in_mem_count -= len(urls)
        print('To pop:%s, hubs: %s, urls: %s, hosts:%s' % (count, len(hubs), len(urls), len(self.pool)))
        urls.update(hubs)
        return urls

    def size(self, ):
        return self.in_mem_count

    def empty(self, ):
        return self.in_mem_count == 0

    def __del__(self):
        path = self.name + '.pkl'
        try:
            with open(path, 'wb') as f:
                pickle.dump(self.pool, f)
            print('self.pool saved!')
        except:
            pass