#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/20 17:44
# @author: Paulson●Wier
# @file: 1_7字典排序.py
# @desc:

'''
问题
你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

解决方案
为了能控制一个字典中元素的顺序，你可以使用collections模块中的
OrderedDict 类。在迭代操作的时候它会保持元素被插入时的顺序，示例如下：
'''

# OrderedDict使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key,d[key])

import json
print(json.dumps(d))

'''
讨论
OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的
元素插入进来的时候，它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会
改变键的顺序。
需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维
护着另外一个链表。所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的
时候（比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去），那么你就得仔
细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。

'''