#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 21:30
# @Author  : yb.w
# @File    : 包图网.py
import requests
from lxml import etree
class Spider():

    def get_request(self,url):
        response = requests.get(url)
        html = etree.HTML(response.content.decode())
        return html

    def xpath_data(self,html):
        src_list = html.xpath('//div[@class="video-play"]/video/@src')
        tit_list = html.xpath('//span[@class="video-title"]/text()')
        for src,tit in zip(src_list,tit_list):
            print(src,tit)
            content = requests.get('http:'+src).content
            file_name = "视频\\"+ tit + ".mp4"
            print('正在抓取视频： ' + file_name)

            with open(file_name,"wb") as f:
                f.write(content)




if __name__ == '__main__':
    spider = Spider()
    url = "https://ibaotu.com/shipin/"
    html = spider.get_request(url)
    # print(html)
    spider.xpath_data(html)