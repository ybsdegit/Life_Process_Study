#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/19 15:58
# @author: Paulson●Wier
# @file: 2_api_puppteer.py
# @desc:


import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    await page.screenshot(path='example.png')
    await page.pdf(path='example.pdf')
    dimensions = await page.evaluate('''() => {
           return {
               width: document.documentElement.clientWidth,
               height: document.documentElement.clientHeight,
               deviceScaleFactor: window.devicePixelRatio,
           }
       }''')
    print(dimensions)
    await browser.close()


asyncio.run(main())
