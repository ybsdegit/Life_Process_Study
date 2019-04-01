#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/21 11:00
# @author: Paulson●Wier
# @file: 1_8字典的运算.py
# @desc:
'''
问题
怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？

解决方案
考虑下面的股票名和价格映射字
'''
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
# 如果你在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是
# 值。比如：
min(prices)
max(prices)

# 许你会尝试着使用字典的 values() 方法来解决这个问题：
min(prices.values())
max(prices.values())

# 通常这个结果同样也不是你想要的。你可能还想要知道对应的键的信息
# 你可以在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息。比如：
min(prices,key=lambda k:prices[k])
max(prices,key=lambda k:prices[k])

# 但是，如果还想要得到最小值，你又得执行一次查找操作。比如：
min_value = prices[min(prices,key=lambda k:prices[k])]
print(min_value)

#  zip() 函数方案通过将字典”反转”为 (值，键) 元组序列来解决了上述问题。当比较两个元组的时候，值会先进行比较，然后才是键。
# 这样的话你就能通过一条简单的语句就能很轻松的实现在字典上的求最值和排序操作了。


# 注意的是在计算操作中使用到了 (值，键) 对。当多个实体拥有相同的值的时候，键会决定返回结果。
# 比如，在执行 min() 和 max() 操作的时候，如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回：
prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(),prices.keys()))
max(zip(prices.values(),prices.keys()))




