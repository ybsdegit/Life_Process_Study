#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/19 11:25
# @author: Paulson●Wier
# @file: 1_安装demo.py
# @desc:

import asyncio
import os

from pyppeteer import launch


async def main():
    browser = await launch(headless = False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.run(main())
# asyncio.get_event_loop().run_until_complete(main())

