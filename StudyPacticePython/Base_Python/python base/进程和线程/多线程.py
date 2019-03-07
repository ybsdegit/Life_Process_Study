#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/7 14:17
# @author: Paulson●Wier
# @file: 多线程.py
# @desc:

import time ,threading

# 新线程执行的代码：
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n +=1
        print('Thread %s >>> %s '% (threading.current_thread().name,n))
        time.sleep(1)
    print('Thread %s ended...' %threading.current_thread().name)

print('Thread %s running1...' %threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' %threading.current_thread().name)


