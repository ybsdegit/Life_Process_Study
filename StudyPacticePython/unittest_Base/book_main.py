#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/19 16:02
# @author: Paulson●Wier
# @file: book_main.py
# @desc:


class book(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

        def __getattr__(self, key):
            """
            _getattr__其实是 python 中的一个内置函数，可以用来实现返回未知属性
            :param self:
            :param key:
            :return:
            """
            try:
                return self[key]
            except KeyError:
                raise AttributeError(r"Dict object has no attribute '%s' " % key)

        def __setattr__(self, key, value):
            """
            _setattr__(self, key, value)也是一个内置函数，
            当类的实例属性尝试赋值时，就会调用这个方法
            使用这种方法向字典中添加的元素和值（除了一开始字典中的元素和值）
            都会被添加到一个叫做__dict__的属性中，并且这个属性原有并不为空，从末尾位置开始添加
            :param self:
            :param key:
            :param value:
            :return:
            """
            self[key] = value

        # 按照页数
        def get_page(self):
            if self.page <= 60:
                return "短篇"
            elif self.page <= 150:
                return "中篇"
            elif self.page > 150:
                return "长篇"
