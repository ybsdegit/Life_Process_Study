#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 13:20
# @Author  : Paulson
# @File    : requests_Base.py
# @Software: PyCharm
# @define  : function

# 请求库 requests
import json

import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://www.baidu.com/')
# print(type(response))
# print(response.status_code)
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key + '=' + value)

# response = requests.get('http://httpbin.org/get')
# print(response.json())
# # print(response.text)
# print(json.loads(response.text))

# response = requests.get('https://www.12306.cn')
# print(response.status_code)



# 代理设置
proxies = {
    # "http":"http://127.7.7.1:9743",
    # "https":"https://127.7.7.1:9743"
}

response = requests.get("https://taobao.com",proxies=proxies)
print(response.status_code)


# 异常捕获
