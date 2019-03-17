#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/22 16:36
# @author: Paulson●Wier
# @file: filter.py
# @desc:

'''
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

'''

#在一个list中，删掉偶数，保留奇数
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,0]))
print(L)


# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(m):
    return m and m.strip()

M = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(M)




'''
用filter求素数
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
'''

# 先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n):
    return lambda x : x % n > 0

#定义一个生成器
def primes():
    yield 2
    it = _odd_iter()  #初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
        # 生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列

# 打印1-10000以内的素数
for n in primes():
    if n < 10000:
        print(n)
        with open('素数.txt', 'a', encoding='utf-8') as f:
            f.write(str(n))
            f.write(',')
    else:
        break