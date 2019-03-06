#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/4 15:41
# @author: Paulson●Wier
# @file: tokenize_demo1.py
# @desc:

'''
使用 NLTK Tokenize 文本
'''

from nltk.tokenize import sent_tokenize


# 使用句子tokenizer将文本tokenize成句子:(sent_tokenize)
mytext = 'Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude. ' \
         'Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude.'
print(sent_tokenize(mytext))

#输出结果：
'''
['Hello Adam, how are you?', 'I hope everything is going well.', 'Today is a good day, see you dude.']

'''


# 将文本tokenize成单词: (word_tokenize)
from nltk.tokenize import word_tokenize
mytext1 = 'Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude. '
print(word_tokenize(mytext1))
'''
输出结果：
['Hello', 'Adam', ',', 'how', 'are', 'you', '?', 'I', 'hope', 'everything', 'is', 'going', 'well', '.', 'Today', 'is', 'a', 'good', 'day', ',', 'see', 'you', 'dude', '.']
'''

# Tokenize时可以指定语言:
print(word_tokenize(mytext1,"french"))


