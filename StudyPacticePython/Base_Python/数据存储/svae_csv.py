#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 22:45
# @Author  : Paulson
# @File    : svae_csv.py
# @Software: PyCharm
# @define  : function CSV文件存储

import csv

# 1. 写入

# 写入的文本默认是以逗号分隔的，调用一次 writerow() 方法即可写入一行数据，
# with open('data.csv','w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['1','Mike','11'])
#     writer.writerow(['2','Bob','22'])
#     writer.writerow(['2','Paulson','18'])


# 如果我们想修改列与列之间的分隔符可以传入 delimiter 参数
# with open('data.csv','w') as csvfile:
#     writer = csv.writer(csvfile,delimiter=' ')
#     writer.writerow(['id','name','age'])
#     writer.writerow(['1','Mike','11'])
#     writer.writerow(['2','Bob','22'])
#     writer.writerow(['2','Paulson','18'])


# # 另外我们也可以调用 writerows() 方法同时写入多行，此时参数就需要为二维列表，例如：
# with open('data.csv','w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow([['1','Mike','11'],['2','Bob','22'],['3','Paulson','18']])


'''
但是一般情况下爬虫爬取的都是结构化数据，
我们一般会用字典来表示，在 csv 库中也提供了字典的写入方式，实例如下：

在这里我们先定义了三个字段，用 fieldnames 表示，
然后传给 DictWriter 初始化一个字典写入对象，
然后可以先调用 writeheader() 方法先写入头信息，
然后再调用 writerow() 方法传入相应字典即可
'''
# with open('data1.csv','w') as csvfile:
#     fieldnames = ['id','name','age']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

# 追加写入
# with open('data1.csv','a')as csvfile:
#     fieldnames = ['id','name','age']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})
#
# 写入中文
# with open('data.csv', 'a', encoding='utf-8') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})
#


# 2.读取


# with open('data1.csv','r')as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

import pandas as pd

df = pd.read_csv('data1.csv')
print(df)