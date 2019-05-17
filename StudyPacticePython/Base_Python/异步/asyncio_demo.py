#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/16 10:02
# @author: Paulson●Wier
# @file: asyncio_demo.py
# @desc:
import asyncio

async def foo():
    print('this is a async! ')
    return '返回值'

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        print('开始运行协程')
        core = foo()
        print('进入事件循环')

        # run_until_complete的参数是一个futrue对象。当传入一个协程，其内部会自动封装成task，其中task是Future的子类
        # run_until_complete可以获取协程的返回值，如果没有给定返回值，则像函数一样，默认返回None。
        result = loop.run_until_complete(core)  # 默认循环 启动，协程返回这个方法将停止循环
        print(f"run_until_complete 可以获取协程的{result}，默认输出None")
    finally:
        print('关闭事件循环')
        loop.close()