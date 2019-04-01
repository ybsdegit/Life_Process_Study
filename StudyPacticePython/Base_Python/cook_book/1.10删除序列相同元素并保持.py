#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/22 11:37
# @author: Paulson●Wier
# @file: 1.10删除序列相同元素并保持.py
# @desc:

# 1.10 删除序列相同元素并保持
'''
问题
怎样在一个序列上面保持元素顺序的同时消除重复的值？

解决方案
如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题。比
'''


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


b = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(b))


# 这个方法仅仅在序列中元素为 hashable 的时候才管用。
# 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话，你需要将上述代码稍微改变一下，就像这样：
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: (d['x'], d['y'])))
list(dedupe(a, key=lambda d: d['x']))

# 如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合。比如：
set(b)
