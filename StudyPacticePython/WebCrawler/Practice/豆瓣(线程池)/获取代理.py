#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 23:14
# @Author  : Paulson
# @File    : 获取代理.py
# @Software: PyCharm
# @define  : function
import random

import requests
from lxml import etree


def get_xici_proxy(page_no):
    '''
    获取代理IP信息
    :param page_no:
    :return:
    '''
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
            result.append(proxy)
            test_proxy(proxy)
            # print(result)
    return result


def test_proxy(proxy):
    # https_url = 'https://book.douban.com'
    https_url = "https://www.baidu.com/"
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    user_agent = random.choice(user_agent_list)
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'User-Agent':user_agent
    }
    try:
        proxies = {"https": proxy}
        r = requests.get(https_url, headers=headers, verify=False,proxies=proxies,timeout=3)
        content = r.content.decode('utf-8')
        # root = etree.HTML(content)
        # items = root.xpath('.//li[@class="subject-item"]')
        # print(r.status_code, len(items))

        # if r.status_code == 200 and len(items) ==20:
        if r.status_code == 200:
            with open('可用代理IP.txt','a+',encoding='utf-8') as f :
                f.write(proxy)
                f.write('\n')
                print(proxy)
            return True
        return False
    except Exception as e:
        msg = str(e)
        print(msg)
        return False




if __name__ == '__main__':
    url = "https://www.xicidaili.com/"
    for page_no in range(0,10):
        result = get_xici_proxy(page_no)
    # print(result)