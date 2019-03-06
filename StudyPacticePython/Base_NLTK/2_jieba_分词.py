#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/4 18:17
# @author: Paulson●Wier
# @file: jieba_分词.py
# @desc:

# 使用jieba分词

import jieba

jieba.load_userdict('userdict.txt')  #加载外部 用户词典

# 结巴分词——全模式
# 全模式分词：把句子中所有的可能是词语的都扫描出来，速度非常快，但不能解决歧义。

sent1 = '''安心互联网保险坚持“简单的保险”理念，首创移动端一键完成的极简流程，为客户提供极致体验。安心互联网保险用互联网思维，实现从承保、查勘、定损到理赔的全流程改造，将条款通俗化、投保自助化、理赔简单化，确保客户看得明白、买得方便、赔得快捷。'''
sent = "在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度搜索探索解空间树。"

content = "现如今，机器学习和深度学习带动人工智能飞速的发展，并在图片处理、语音识别领域取得巨大成功。"

# wordlist = jieba.cut(sent,cut_all=True)
# print("|".join(wordlist))

# 结巴分词——精确切分
# 精确分词：精确模式试图将句子最精确地切开，精确分词也是默认分词。
wordlist = jieba.cut(sent1)
# print("/".join(wordlist))
print("|".join(wordlist))

# wordlist = jieba.cut(content,cut_all=False)
# print("|".join(wordlist))


# 结巴分词——搜素引擎模式
# 搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
wordlist = jieba.cut_for_search(sent)
# print("|".join(wordlist))


# 用 lcut 生成 list
'''
jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 Generator，
可以使用 for 循环来获得分词后得到的每一个词语（Unicode）。
jieba.lcut 对 cut 的结果做了封装，l 代表 list，即返回的结果是一个 list 集合。
同样的，用 jieba.lcut_for_search 也直接返回 list 集合。
'''
segs = jieba.lcut(sent1)
print(segs)

# 获取词性
import jieba.posseg as psg
print([(x.word,x.flag) for x in psg.lcut(sent1)])

