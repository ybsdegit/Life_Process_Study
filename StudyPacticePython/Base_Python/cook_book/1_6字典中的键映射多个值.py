#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/20 15:06
# @author: Paulson●Wier
# @file: 1_6字典中的键映射多个值.py
# @desc:
'''
问题
怎样实现一个键对应多个值的字典（也叫 multidict）？

解决方案
一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你
就需要将这多个值放到另外的容器中，比如列表或者集合里面。比如，你可以像下面这
样构造这样的字典

选择使用列表还是集合取决于你的实际需求。如果你想保持元素的插入顺序就应
该使用列表，如果想去掉重复元素就使用集合（并且不关心元素的顺序问题）。
你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要
关注添加元素操作了。比如：

'''
pairs = {
'a' : 1,
'b' : 4
}
# from collections import defaultdict
# d = defaultdict(list)
#
# for key, value in pairs:
#     d[key].append(value)
#
# print(d)