#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/14 16:04
# @author: Paulson●Wier
# @file: 进程之间的通信（一个进程写、一个进程读）.py
# @desc:
import random
import time
from multiprocessing import Queue, Process


# 要写入的数据
list1 = ['java', 'python', 'JS']

def write(queue):
    """
    向队列中添加数据
    :param queue:
    :return:
    """
    for value in list1:
        print('正在向队列中添加数据-->{}'.format(value))
        queue.put(value)
        time.sleep(random.random())  # 0-1


def read(queue):
    while True:
        # 判断队列是否为空
        if not queue.empty():
            value = queue.get(True)
            print('从队列中取到的数据为-->{}'.format(value))
            time.sleep(random.random())  # 0-1
        else:
            break


if __name__ == '__main__':
    # 父进程创建出队列，通过参数的形式传递给子进程
    queue = Queue()

    # 创建两个进程 一个写数据 一个读数据
    write_data = Process(target=write, args=(queue,))
    read_data = Process(target=read, args=(queue,))

    # 启动进程 写入数据
    write_data.start()
    # 使用join 等待写数据结束
    write_data.join()

    # 启动进程 读取数据
    print('*'*20)
    read_data.start()
    read_data.join()

    print('所有的数据都写入并读取完成***')