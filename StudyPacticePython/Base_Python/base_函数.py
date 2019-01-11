#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/1/10 14:34
# @author: Paulson●Wier
# @file: 函数.py
# @desc:

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s


'''
可变参数
在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

定义可变参数和定义一个list或tuple参数相比，
仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple，
因此，函数代码完全不变。
但是，调用该函数时，可以传入任意个参数，包括0个参数：
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def main(x):
    # power(x,n)
    pass


'''
关键字参数

可变参数允许你传入0个或任意个参数，
这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。请看示例：
'''
# 关键字参数有什么用？它可以扩展函数的功能。

def person(name,age,**kw):
    #函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
    print('name:',name,'age:',age,'other:',kw)



if __name__ == '__main__':
    # s = power(5,3)
    # s = calc([1,2,3])
    # s1 = calc((1,2,3))
    # s2 = calc(1,2)
    # s3 = calc()
    # nums = [1,2,3]
    # s4 = calc(*nums)  #pyhton 允许在list或tuple前面加一个*号，把list或tuple元素变成可变参数传进去：
    # print(s4)

    s = person('Yuanbao',30)
    s1 = person('Paulson',23,city='Beijing')