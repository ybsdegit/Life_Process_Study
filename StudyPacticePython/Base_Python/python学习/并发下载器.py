#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 23:12
# @Author  : Paulson
# @File    : 并发下载器.py
# @Software: PyCharm
# @define  : function
import random
import urllib.request

import gevent


def download(name,url):
    req = urllib.request.urlopen(url)
    img_content = req.read()
    with open(name,'wb') as f:
        f.write(img_content)



def main():

    url1 = 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/03/16/1864921_20190316203533_small.jpg'
    url2 = 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/03/06/6177519_20190306233354_small.jpg'

    gevent.joinall({
        gevent.spawn(download, '1.jpg',url1),
        gevent.spawn(download,'2.jpg',url2)
    })

if __name__ == '__main__':
    main()