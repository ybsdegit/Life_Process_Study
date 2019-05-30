#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/5/30 18:13
# @author: Paulson●Wier
# @file: 任务.py
# @desc:

import asyncio
import time


async def whattime(i):
    await asyncio.sleep(1)
    print(f'calling: {i}, now is {time.strftime("%X")}')


async def main():
    task = asyncio.create_task(whattime(0))
    await task
    for i in range(1, 5):
        s = asyncio.create_task(whattime(i))

    await  asyncio.sleep(1)

asyncio.run(main())