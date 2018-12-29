#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/30 0:52
# @Author  : yb.w
# @File    : MaoYan.py

import requests
from lxml import etree

index =1 #全局变量
def get_response(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers)

    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        return None

#保存数据
def parser_page_content(html):
    html = etree.HTML(html)

    '''
    谓语：[]
    '''
    name = html.xpath("//p[@class='name']//text()")
    star = html.xpath("//p[@class='star']//text()")
    releasetime = html.xpath("//p[@class='releasetime']//text()")

    global index  #知名当前变量使用外部的全局变量
    with open("热映口碑影片.txt", 'a+', encoding='utf-8') as f:
        for item in range(8):
            f.write("\n排名第%s"%index+"电影:\t"+name[item].strip()+"\n\t\t"+star[item].strip()+"\n\t"+releasetime[item]+"\n")
            index+=1

if __name__ == '__main__':
    with open("热映口碑影片.txt",'w',encoding='utf-8') as f:
        f.write("猫眼电影热映排行\n")
    url = "https://maoyan.com/board"
    html = get_response(url)
    parser_page_content(html)


