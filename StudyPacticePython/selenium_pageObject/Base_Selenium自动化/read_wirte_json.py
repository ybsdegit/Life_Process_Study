#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/19 10:22
# @author: Paulson●Wier
# @file: read_wirte_json.py
# @desc:

import json
#这是我们提供的 JSON 格式示例数据
json_data={
 "results": [
 {
 "location": {
 "id": "WX4FBXXFKE4F",
 "name": "北京",
 "country": "CN",
 "path": "北京,北京",
 "timezone": "Asia/Shanghai",
 "timezone_offset": "+08:00"
 }
 }
 ]
}


# dumps()方法将 dict 转化成 str 格式
b = json.dumps(json_data)
print(b, type(b))

# loads()方法将 str 转化成 dict 格式
c = json.loads(b)
print(c, type(c))


# 把json保存为字符串
# with open(r'./file/text.txt', 'w') as f:
#     json.dump(json_data, f)


# 读取字符串，转换为json
with open(r'./file/text.txt', 'r') as f:
    # print(f.read())  # 不能同时使用 f.read() 和json.load()
    # 报错： json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    # 这种错误和 Windows 操作系统下的当前文件已经被其他程序占用很类似，f.read()调用后，json.load(f)方法就会什么都获取不到
    print(json.load(f))
