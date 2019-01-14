#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 21:18
# @Author  : yb.w
# @File    : douyu.py
import json

import requests


def get_json(url):
    response = requests.get(url)
    if response.status_code ==200:
        json_data = json.loads(response.text)
        return json_data
    return None

def parse_json(json_data):
    print(json_data)
    for i in json_data['data']['rl']:
        image_name = "图片\\"+ i['nn'] +".jpg"
        image_src = i['rs1']
        content = requests.get(image_src).content
        # print("正在抓取第 "+i+"张图片: "+i['nn'])
        print(content)
        with open(image_name,'wb') as f:
            f.write(content)





if __name__ == '__main__':
    url = 'https://www.douyu.com/gapi/rkc/directory/2_201/0'
    json_data = get_json(url)
    # print(json_data)
    parse_json(json_data)