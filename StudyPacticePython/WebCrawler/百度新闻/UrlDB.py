#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/11 11:12
# @author: Paulson●Wier
# @file: UrlDB.py
# @desc:

# import leveldb

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

'''
UrlDB将被UrlPool使用，主要有三个方法被使用：

has(url) 查看是否已经存在某url
set_success(url) 存储url状态为成功
set_failure(url) 存储url状态为失败
'''