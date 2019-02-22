#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/22 11:50
# @author: Paulson●Wier
# @file: map_reduce.py
# @desc:

'''
map/reduce

map()函数接收两个参数，
一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


'''

def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。



# 对一个序列求和，就可以用reduce实现：
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def add(x,y):
    return x + y


def fn(x,y):
    return x*10 +y


s = reduce(add,[1,3,5,7,9])
# print(s)

t = reduce(fn,[1,3,5,7,9])
# print(t)


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x,y : x*10 +y, map(char2num,s))

# print(str2int("75356345345"))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：[‘adam’, ‘LISA’, ‘barT’]，输出：[‘Adam’, ‘Lisa’, ‘Bart’]：”

def normalize(name):
    name = name.lower()
    return name[0].upper() + str(name[1:])


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
# print(L2)


# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
    def mul(x,y):
        return x*y
    return reduce(mul,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：

def str_int(s):
    d = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
    return d[s]

def add_1(x,y):
    # 生成百位数
    return  x*10 + y



def str2float(s):
    s = s.split('.')
    s1 = s[0]  #整数部分
    s2 = s[1]  #小数部分

    d1 = reduce(add_1,map(str2int,s1))
    d2 = reduce(add_1,map(str2int,s2))

    d = d1+d2*0.001
    return d


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')