#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/19 10:39
# @author: Paulson●Wier
# @file: read_write_xml.py
# @desc:
"""
在解析 XML 的时候，我们主要会用到两个方法， Element 和 tostring，前者用于创建
一个 XML 文件，后者则用于将 XML 文件转换的可以被人类读取、理解的字符形式的代
码。
"""
from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import Element


dict = { "name":"zhang_san", "gender":"female", "phone_number":"01234567890","note":"none"}


# 写一个转换函数，将字典转换为xml
def convert(tag_name, dict):
    # 建立一个xml
    elem = Element(tag_name)

    # 双值循环取出字典中的key和value
    for key, value in dict.items():
        # print(key, ":", value)

        # 相当于为key建一个标签
        xml_elem = Element(key)
        # 将key的值赋给这个标签的值
        xml_elem.text = str(value)

        # 添加进xml文件
        elem.append(xml_elem)
    return elem


# 字典转换
dict_convert = convert('text', dict)
print("="*20)
print(dict_convert)

# 这是转换为标准可读的xml
print(tostring(dict_convert))
# 设置最外层的标签属性
dict_convert.set("id_number", "123456789")
# 再次输出
print(tostring(dict_convert))


# 解析xml
from xml.etree import ElementTree as et
xml_string = tostring(dict_convert)
# 从文件获取xml
# root = ElementTree.parse(r"D:/test.xml")

# 从文本获取xml
root = et.fromstring(xml_string)

# instance 1
print("*"*20)
# 列表形式输出内存地址
for i in list(root):
    print(i.tag, i.text)

# instance 2
print("*"*30)
test_person = root.getiterator("test")
for i in test_person:
    for j in i:
        print(j.tag, j.text)

# instance 3
print("*"*30)
find_node2=root.findall("name")
print(find_node2[0],find_node2[0].tag,find_node2[0].text)

# instance 4
print("*"*30)
find_node=root.find("name")
print(find_node,find_node.tag,find_node.text)