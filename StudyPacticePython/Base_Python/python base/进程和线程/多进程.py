#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/7 11:44
# @author: Paulson●Wier
# @file: 多进程.py
# @desc:

# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
import os
import random
import time
from multiprocessing import Pool, Queue, Process


# import os,time,random
#
# def long_time_task(name):
#     print('Run task %s(%s)...' %(name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f senconds. ' %(name,(end-start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Wating for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subproccesses done...')

# 写数据进程执行的代码
def writer(q):
    print('Process to write : %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' %value)
        q.put(value)
        time.sleep(random.random())


# 读数据进行执行的代码
def read(q):
    print('Process to read : %s' %os.getpid()  )
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=writer,args=(q,))
    pr = Process(target=read,args=(q,))

    # 启动子进程pw,进行写入
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
