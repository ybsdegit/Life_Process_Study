#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 22:10
# @Author  : Paulson
# @File    : save_json.py
# @Software: PyCharm
# @define  : json 文件存储

import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

'''
1. 读取json
'''
# 使用了 loads() 方法将字符串转为 Json 对象，由于最外层是中括号，所以最终的类型是列表类型。
# print(type(str))
# data = json.loads(str)
# # print(type(data))
# # print(data)
#
# print(data[0].get('name'))
# print(data[0]['name'])
#
# # print(data[0]['age'])
# print(data[0].get('age',25))


'''
Json 的数据需要用双引号来包围，不能使用单引号。

"name":"paulson"  right
'name':'wier'     faulse
'''

#从json文本文件内容读出，然后利用loads()方法转化

# with open('data.json','r') as f:
#     str = f.read()
#     data = json.loads(str)
#     print(data)


'''
2. 输出json(保存json文件)
利用 dumps() 方法我们可以将 Json 对象转为字符串，然后再调用文件的 write() 方法即可写入到文本
'''

# data = [{
#     'name':'Bob',
#     'age':'22',
#     'gender':'male'
# }]

# with open('data.json','w') as f:
#     f.write(json.dumps(data))


# 另外如果我们想保存 Json 的格式，可以再加一个参数 indent，代表缩进字符个数。
# with open('data.json','w')as f:
#     f.write(json.dumps(data,indent=2))

#写入中文

data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2,ensure_ascii=False))