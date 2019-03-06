#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/5 20:46
# @author: Paulson●Wier
# @file: 5_词袋模型.py
# @desc:

# 词袋模型（Bag of Words Model）

# （1）词袋模型
import jieba

#定义停用词
punctuation = ["，","。", "：", "；", "？"]
#定义语料
content = ["机器学习带动人工智能飞速的发展。",
            "深度学习带动人工智能飞速的发展。",
            "机器学习和深度学习带动人工智能飞速的发展。"
              ]
seqs_1 = [jieba.lcut(con) for con in content]
print(seqs_1)

#去标点
tokenized = []
for sentence in seqs_1:
    words = []
    for word in sentence:
        if word not in punctuation:
            words.append(word)
    tokenized.append(words)
print(tokenized)


# 把所有的分词结果放到一个袋子（List）里面，也就是取并集，再去重，获取对应的特征词。

# 求并集
bag_of_words = [x for item in seqs_1 for x in item if x not in punctuation]
# 去重
bag_of_words = list(set(bag_of_words))
print("\n",bag_of_words)


# 词袋化

bag_of_word2vec = []
for sentence in tokenized:
    tokens = [1 if token in sentence else 0 for token in bag_of_words]
    bag_of_word2vec.append(tokens)
print(bag_of_word2vec)


# (2)Gensim 构建词袋模型

from gensim import corpora
import gensim
# tokenized 是去标点之后的
dictionary = corpora.Dictionary(tokenized)
# 保存词典
dictionary.save('deerwester.dict')
print(dictionary)
print(dictionary.token2id)


# 根据得到的结果，我们同样可以得到词袋模型的特征向量
# doc2bow()，作用是计算每个不同单词的出现次数，将单词转换为其整数单词 id 并将结果作为稀疏向量返回。
corpus = [dictionary.doc2bow(sentence) for sentence in seqs_1 ]
print(corpus)


# 词向量 （Word Embedding）
