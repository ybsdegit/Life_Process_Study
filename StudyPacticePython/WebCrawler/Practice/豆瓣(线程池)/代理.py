#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 23:14
# @Author  : Paulson
# @File    : 代理.py
# @Software: PyCharm
# @define  : function
import requests
from lxml import etree


def get_xici_proxy(page_no):
    url = "https://www.xicidaili.com/nn/{}".format(page_no)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    r = requests.get(url,headers=headers)
    content = r.content.decode('utf-8')
    root = etree.HTML(content)
    tr_nodes = root.xpath('.//table[@id="ip_list"]/tr')[1:]

    result = []

    for tr_node in tr_nodes:
        td_nodes = tr_node.xpath('./td')
        ip = td_nodes[1].text   #ip
        port = td_nodes[2].text #端口号
        proxy_type = td_nodes[4].text #高匿
        proto = td_nodes[5].text  #http类型
        proxy = "{}:{}:{}".format(proto.lower(),ip,port)
        uptime = td_nodes[8].text  #验证时间
        # print(proxy)
        if proxy_type == "高匿" and proto.lower() == "https":
            with open('代理IP.txt','a+',encoding='utf-8') as f :
                f.write(proxy)
                f.write('\n')
            result.append(proxy)
            print(result)
    return result



if __name__ == '__main__':
    url = "https://www.xicidaili.com/"
    result = get_xici_proxy(2)
    print(result)
