#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 22:23
# @Author  : Paulson
# @File    : 字符转义.py
# @Software: PyCharm
# @define  : function


'''
如何将字母转换为ASCII码？
Python中提供函数ord()将字母转换成ASCII码，
提供函数chr()将相对应的ASCII码转化为字母，
'''
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"""
def ma_solution(text):
    o =''
    for each in text:
        if ord(each) >= ord('a') and ord(each) <= ord('z'):
            o += chr((ord(each)+2 - ord('a'))%26 + ord('a'))
        else:
            o += each
    print(o)


'''
maketrans() 方法用于创建字符映射的转换表，
对于接受两个参数的最简单的调用方式，
第一个参数是字符串，表示需要转换的字符，
第二个参数也是字符串表示转换的目标。
两个字符串的长度必须相同，为一一对应的关系。
'''
import string
def std_solution(text):
    table = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[2:]+string.ascii_lowercase[:2]
    )
    print(text.translate(table))

if __name__ == '__main__':
    std_solution(text)
