#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/16 10:10
# @author: Paulson●Wier
# @file: 协程调用协程.py
# @desc:

import asyncio

async def main():
    print('主协程')
    print('等待result1 协程运行')
    res1 = await result1()
    print('等待result2 协程运行')
    res2 = await result2(res1)
    return (res1, res2)


async def result1():
    print("this is result1 async!")
    return 'result1'

async def result2(arg):
    print("this is result2 async!")
    return f"result2 accept a args,{arg}"

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main())
        print(f"获取返回值：{result}")
    finally:
        print('关闭时间循环')
        loop.close()