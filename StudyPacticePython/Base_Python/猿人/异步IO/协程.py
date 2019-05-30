#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/5/30 18:06
# @author: Paulson●Wier
# @file: 协程.py
# @desc:
import asyncio
import time


async def now_time():
    return time.time()


async def main():
    now1 = now_time()
    print('now1 is ', type(now1))

    now2 = await now1
    print(f'now is {now2}')

    now3 = await now_time()
    print(f'now is {now3}')


asyncio.run(main())
