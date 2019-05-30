#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/5/30 17:40
# @author: Paulson●Wier
# @file: async_study.py
# @desc:
import asyncio
import time


async def say_delay(msg, delay):
    await asyncio.sleep(delay)
    print(msg)


async def main():
    print(f"begin at {time.strftime('%H-%M-%S')}")
    await say_delay('你好', 1)
    await say_delay('学习协程', 2)
    print(f"end at {time.strftime('%H-%M-%S')}")


async def main1():
    task1 = asyncio.create_task(say_delay('你好', 1))
    task2 = asyncio.create_task(say_delay('学习协程', 2))
    print(f"begin at {time.strftime('%H-%M-%S')}")
    await task1
    await task2
    print(f"end at {time.strftime('%H-%M-%S')}")



# asyncio.run(main())
# 从起止时间可以看出，两个协程是顺序执行的，总共耗时1+2=3秒。

asyncio.run(main1())
# 从运行结果的起止时间可以看出，两个协程是并发执行的了，总耗时等于最大耗时2秒。
# asyncio.create_task() 是一个很有用的函数，在爬虫中它可以帮助我们实现大量并发去下载网页。在Python 3.6中与它对应的是 ensure_future()。