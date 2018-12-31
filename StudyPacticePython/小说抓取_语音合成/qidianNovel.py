#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 20:21
# @Author  : yb.w
# @File    : 12.30.py   全站小说抓取-人工智能语音合成-搭建一个网站
#
'''
 VIP小说 身份篡改（？）
 垃圾数据 -数据清洗
'''

#   1.面向对象 -- 》 集成封装
import requests
from lxml import etree
import os

class Spider(object):
    def start_request(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        response = requests.get("https://www.qidian.com/all",headers=headers)
        print()
        html = etree.HTML(response.content.decode())
        Bigtit_list = html.xpath("//div[@class='book-mid-info']/h4/a/text()")
        Bigsrc_list = html.xpath("//div[@class='book-mid-info']/h4/a/@href")

        for Bigsrc,Bigtit in zip(Bigsrc_list,Bigtit_list):
            if os.path.exists(Bigtit) == False:
                os.mkdir(Bigtit)
            self.xpath_data(Bigsrc,Bigtit)

    def xpath_data(self,Bigsrc,Bigtit):
        response = requests.get("http:"+Bigsrc)
        html = etree.HTML(response.content.decode())
        Listtit_list = html.xpath("//ul[@class='cf']/li/a/text()")
        Listsrc_list = html.xpath("//ul[@class='cf']/li/a/@href")
        for Listsrc, Listtit in zip(Listsrc_list, Listtit_list):
            self.finally_file(Listtit,Listsrc,Bigtit)

    def finally_file(self,tit,url,Bigtit):
        response = requests.get("http:"+url)
        html = etree.HTML(response.content.decode())
        content = "\n".join(html.xpath("//div[@class='read-content j_readContent']/p/text()"))
        file_name = Bigtit + "\\" + tit + ".txt"
        print("正在抓取文章："+file_name)
        with open(file_name,'a',encoding='utf=8') as f:
            f.write(content)


if __name__ == '__main__':
    spider = Spider()
    spider.start_request()