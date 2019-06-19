#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/14 15:32
# @author: Paulson●Wier
# @file: 进程之间通信 Queue.py
# @desc:


# 导入 multiprocessing模块中的Queue
from multiprocessing import Queue


# 初始化Queue对象， 参数表示Queue队列中消息的最大数量
q = Queue(3)

# 向队列中添加数据
q.put('消息1')
q.put('消息2')

# full() 判断队列是否是满的，满的True，不满False
print(q.full())

q.put('消息3')
print(q.full())


# 因为消息队列此时已经满了，执行下面的操作会抛出异常

try:
    # 等待 2 秒 抛出异常
    q.put('消息4', True, 2)
except Exception as e:
    print('消息队列已满，现有消息数量：{}'.format(q.qsize()))

try:
    # 等待两秒再2抛出异常
    q.put_nowait('消息4', True, 2)
except Exception as e:
    print("消息队列已满，现有消息数量：%s" % q.qsize())

# 读取数据 先判断队列是否为空，再进行读取
# empty()判断队列是否为空  空True 非空False
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())