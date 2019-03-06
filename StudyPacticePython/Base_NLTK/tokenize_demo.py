#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/4 14:11
# @author: Paulson●Wier
# @file: tokenize_demo.py
# @desc:
import requests
from bs4 import BeautifulSoup

# 获取web页面
response = requests.get('http://php.net/')
html = response.text


# 使用 BeautifulSoup 清洗文字，得到干净的文本
soup = BeautifulSoup(html,'lxml')
text = soup.get_text(strip=True)
# print(text)


# 将文本转化为 Tokens
tokens = text.split()
print(tokens)


#统计词频
# text已经处理完毕了，现在使用Python NLTK统计token的频率分布。
# 通过调用NLTK中的FreqDist()方法实现
# import nltk
# freq = nltk.FreqDist(tokens)
# for key,value in freq.items():
#     print(str(key) + ':' + str(value))
#
# freq.plot(20, cumulative=False)


# 处理停用词(of a an ...)
# NLTK自带了许多种语言的停用词列表，如果你获取英文停用词:
import nltk
from nltk.corpus import stopwords

clear_tokens = list()
sr = stopwords.words('english')
for token in tokens:
    if token not in sr:
        clear_tokens.append(token)

#统计处理停用词后的词频
freq = nltk.FreqDist(clear_tokens)
for key,value in freq.items():
    print(str(key) + ':' + str(value))

#h绘制频率分布图
freq.plot(20, cumulative=False)