#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/20 20:18
# @author: Paulson●Wier
# @file: 生成器.py
# @desc:


# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(max):
    n, a, b = 0, 0 ,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

# f = fib(6)
# for n in fib(6):
#     print(n)

'''
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
'''

g = fib(6)
while True:
    try:
        x = next(g)
        print('g :',x)
    except StopIteration as e:
        print('Generator return values: ', e.value)
        break


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


#杨辉三角
'''
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1
'''

def triangle(num):
    L = [1]
    for i in range(1,num+1):   #用来输出多行
        print(L)               #首先输出第一行
        L = [L[j] + L[j+1] for j in range(len(L)-1)]   #使用列表生成式来生成下一行列表
        L.insert(0,1)          #杨辉三角第一个元素为1
        L.append(1)            #末尾追加1


def main():
    num = eval(input("please input a number: "))
    triangle(num)

main()






