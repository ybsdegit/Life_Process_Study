#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/5 17:56
# @author: Paulson●Wier
# @file: 4_文本可视化.py
# @desc:

'''
文本可视化类型，除了包含常规的图表类，如柱状图、饼图、折线图等的表现形式，在文本领域用的比较多的可视化类型有：
（1）基于文本内容的可视化。
基于文本内容的可视化研究包括基于词频的可视化和基于词汇分布的可视化，常用的有词云、分布图和 Document Cards 等。
（2）基于文本关系的可视化。
基于文本关系的可视化研究文本内外关系，帮助人们理解文本内容和发现规律。常用的可视化形式有树状图、节点连接的网络图、力导向图、叠式图和 Word Tree 等。
（3）基于多层面信息的可视化
基于多层面信息的可视化主要研究如何结合信息的多个方面帮助用户从更深层次理解文本数据，发现其内在规律。其中，包含时间信息和地理坐标的文本可视化近年来受到越来越多的关注。常用的有地理热力图、ThemeRiver、SparkClouds、TextFlow 和基于矩阵视图的情感分析可视化等。
'''
import jieba


import chardet

import jieba.analyse
import matplotlib.pyplot as plt
content = '''
安心财产保险有限责任公司（以下简称安心互联网保险），全国首批互联网创新型保险公司，总部设在北京。

安心互联网保险坚持“简单的保险”理念，首创移动端一键完成的极简流程，为客户提供极致体验。安心互联网保险用互联网思维，实现从承保、查勘、定损到理赔的全流程改造，将条款通俗化、投保自助化、理赔简单化，确保客户看得明白、买得方便、赔得快捷。

作为全国首家全业务在“云”上的保险公司，安心互联网保险将保险和科技充分结合。通过移动互联、大数据、人工智能、云计算等技术，让用户从投保到理赔，手机端一键轻松解决；搭建反欺诈模型，实现风险识别与管控；自主甄别风险两核系统，升级服务体验；利用云端技术以及分布式存储，轻松应对海量并发业务。

目前，安心互联网保险已拥有丰富的产品线，涵盖车险、健康险、意外险、信用保证保险等。安心互联网车险，互联网车险领导者，以保费最高、增速最快、渠道最强三大优势，在互联网车险领域稳居第一；安心健康险，以“守护国民健康，打造国民保险”为己任，推出一系列高性价比的明星产品，给用户提供实惠、全面的保障。

安心互联网保险率先提出“全国理赔一张网”理念，一张保单保全国，35家服务中心遍布全国，让所有客户享受无地域差别的理赔服务。此外，完善的增值服务，以及多样化的理赔工具，确保客户买得安心、用得省心。
'''
# keywords1 = " ".join(jieba.analyse.extract_tags(content , topK=20, withWeight=False, allowPOS=()))
keywords1 = ' '.join(jieba.cut(content))
print(type(keywords1))
print(keywords1)

# 1.词云图
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator


abel_mask = imread('anxin3.png')  #这里设置了一张中国地图

wc = WordCloud(background_color='black',  # 设置背景颜色
                     mask = abel_mask,  # 设置背景图片
                     max_words = 300,  # 设置最大现实的字数
                     font_path = "msyh.ttc",  # 设置字体格式
                     # width=2048,
                     # height=1024,
                     # scale=4.0,
                     max_font_size= 100,  # 字体最大值
                     random_state=42).generate(keywords1)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)
# 以下代码显示图片
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
# plt.imshow(wc)
plt.axis("off")
plt.show()
# wordcloud2.to_file(dir+'wordcloud_2.jpg') #保存结果
