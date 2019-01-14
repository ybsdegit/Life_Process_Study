#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 20:31
# @Author  : Paulson
# @File    : hero_clother.py
# @Software: PyCharm
import json

import requests
import re

def get_url(js_url,start_url):
    r = requests.get(js_url).text
    id_str = re.search('"keys":(.*),"data":',r).group(1)
    # print(id_str)  #拿到第一个小括号里面的值
    id_dict =json.loads(id_str)
    for i,j in id_dict.items():
        # print(i,j)
        id = i
        name = j
        for k in range(15):
            #拼接得到所有英雄的url
            result_url = start_url + id + '%03d'%k + '.jpg'
            # print(result_url)
            #如果皮肤的url有效
            if requests.get(result_url).status_code == 200:
                with open('img/%s%d.jpg'%(name,k),'wb') as f:
                    result_content = requests.get(result_url)   #获取图片的字节
                    f.write(result_content.content)
                    print('===正在写入英雄皮肤===')

if __name__ == '__main__':
    #图片url
    # url = 'https://ossweb-img.qq.com/images/lol/web201310/skin/big 266    000    .jpg'
    #                                                                英雄id  皮肤id  图片后缀
    # https://ossweb-img.qq.com/images/lol/web201310/skin/big266000.ipg
    # https://ossweb-img.qq.com/images/lol/web201310/skin/big266000.jpg
    # 英雄id url
    js_url = 'https://lol.qq.com/biz/hero/champion.js'
    start_url = 'https://ossweb-img.qq.com/images/lol/web201310/skin/big'

    get_url(js_url,start_url)
