#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/25 20:45
# @author: Paulson●Wier
# @file: 面向对象.py
# @desc:

# std1 = { 'name': 'Michael', 'score': 98 }
# std2 = { 'name': 'Bob', 'score': 81 }
#
# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))

class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))


bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()
