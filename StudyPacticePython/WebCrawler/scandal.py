#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 20:20
# @Author  : yb.w
# @File    : 12_29_scandal.py  糗事百科 正则表达式

import requests
import re


def getScandalText(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    ret = requests.get(url=url,headers = headers).text
    # .* 能够匹配任何内容无数多次，除了\n（换行符）
    # re.S 表示 . 能匹配到换行符
    result = re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>',ret,re.S)
    return result
'''
如果你想保存数据，不能报错列表，只能以字符串或者字符类型来保存
将代码存放至Git仓库
'''
def writerScandal(result):
    # w:write
    with open('糗事百科.txt','a',encoding='utf-8') as f:
        for i  in result:
            i = re.sub('<br/>|\n','',i)
            f.write(i+'\n')

if __name__ == '__main__':
    for i in range(4):
        url = "https://www.qiushibaike.com/hot/page/%s/"%str(i)
        result = getScandalText(url)
        print(result)
        writerScandal(result)