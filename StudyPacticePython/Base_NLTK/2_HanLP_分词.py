#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/5 13:56
# @author: Paulson●Wier
# @file: HanLP_分词.py
# @desc:

from pyhanlp import *

sent = '''安心互联网保险坚持“简单的保险”理念，首创移动端一键完成的极简流程，为客户提供极致体验。安心互联网保险用互联网思维，实现从承保、查勘、定损到理赔的全流程改造，将条款通俗化、投保自助化、理赔简单化，确保客户看得明白、买得方便、赔得快捷。'''
content = "现如今，机器学习和深度学习带动人工智能飞速的发展，并在图片处理、语音识别领域取得巨大成功。"


# 使用自定义词典分词
CustomDictionary.add('安心互联网保险')
CustomDictionary.add('移动端')
CustomDictionary.add('极简')
print(HanLP.segment(sent))