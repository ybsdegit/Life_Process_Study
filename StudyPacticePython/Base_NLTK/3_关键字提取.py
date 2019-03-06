
# encoding: gbk
#!/usr/bin/env python

# -*- coding: gbk -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/5 16:25
# @author: Paulson●Wier
# @file: 3_关键字提取.py
# @desc:

'''




'''

import jieba.analyse

# 基于 TF-IDF 算法进行关键词提取
'''
jieba 已经实现了基于 TF-IDF 算法的关键词抽取，
通过命令 import jieba.analyse 引入，函数参数解释如下：

sentence：   待提取的文本语料；
topK：       返回 TF/IDF 权重最大的关键词个数，默认值为 20；
withWeight： 是否需要返回关键词权重值，默认值为 False；
allowPOS：   仅包括指定词性的词，默认值为空，即不筛选。
'''

sentence  = "人工智能（Artificial Intelligence），英文缩写为AI。它是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学。人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器，该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大，可以设想，未来人工智能带来的科技产品，将会是人类智慧的“容器”。人工智能可以对人的意识、思维的信息过程的模拟。人工智能不是人的智能，但能像人那样思考、也可能超过人的智能。人工智能是一门极富挑战性的科学，从事这项工作的人必须懂得计算机知识，心理学和哲学。人工智能是包括十分广泛的科学，它由不同的领域组成，如机器学习，计算机视觉等等，总的说来，人工智能研究的一个主要目标是使机器能够胜任一些通常需要人类智能才能完成的复杂工作。但不同的时代、不同的人对这种“复杂工作”的理解是不同的。2017年12月，人工智能入选“2017年度中国媒体十大流行语”。"
content = '''
安心财产保险有限责任公司（以下简称安心互联网保险），全国首批互联网创新型保险公司，总部设在北京。

安心互联网保险坚持“简单的保险”理念，首创移动端一键完成的极简流程，为客户提供极致体验。安心互联网保险用互联网思维，实现从承保、查勘、定损到理赔的全流程改造，将条款通俗化、投保自助化、理赔简单化，确保客户看得明白、买得方便、赔得快捷。

作为全国首家全业务在“云”上的保险公司，安心互联网保险将保险和科技充分结合。通过移动互联、大数据、人工智能、云计算等技术，让用户从投保到理赔，手机端一键轻松解决；搭建反欺诈模型，实现风险识别与管控；自主甄别风险两核系统，升级服务体验；利用云端技术以及分布式存储，轻松应对海量并发业务。

目前，安心互联网保险已拥有丰富的产品线，涵盖车险、健康险、意外险、信用保证保险等。安心互联网车险，互联网车险领导者，以保费最高、增速最快、渠道最强三大优势，在互联网车险领域稳居第一；安心健康险，以“守护国民健康，打造国民保险”为己任，推出一系列高性价比的明星产品，给用户提供实惠、全面的保障。

安心互联网保险率先提出“全国理赔一张网”理念，一张保单保全国，35家服务中心遍布全国，让所有客户享受无地域差别的理赔服务。此外，完善的增值服务，以及多样化的理赔工具，确保客户买得安心、用得省心。
'''
keywords1 = " ".join(jieba.analyse.extract_tags(content , topK=20, withWeight=False, allowPOS=()))
keywords2 = (jieba.analyse.extract_tags(content, topK=10, withWeight=True, allowPOS=(['n', 'v'])))

print(keywords1)
print(keywords2)



# 基于 TextRank 算法进行关键词提取
keywords3 = " ".join(jieba.analyse.textrank(content,topK=20,withWeight=False,allowPOS=('ns', 'n', 'vn', 'v')))
keywords4 = (jieba.analyse.textrank(content,topK=20,withWeight=True,allowPOS=(['ns', 'n', 'vn', 'v'])))
print("\n",keywords3)
print(keywords4)



#基于 LDA 主题模型进行关键词提取


# 基于 pyhanlp 进行关键词提取
# 使用 HanLP 来完成关键字提取，内部采用 TextRankKeyword 实现

from  pyhanlp import *
keywords5 = HanLP.extractKeyword(content,20)
print("\npyhanlp获取关键字：",keywords5)