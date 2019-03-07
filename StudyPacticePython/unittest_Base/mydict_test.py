#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/6 17:25
# @author: Paulson●Wier
# @file: mydict_test.py
# @desc:

import unittest
from StudyPacticePython.unittest_Base.mydict import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        #setUp 方法在每调用一个测试方法的前后被执行
        print('begin setup ...,')


    def tearDown(self):
        #tearDown 方法在每调用一个测试方法之后被执行
        print('tearDonw ...')

    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))


    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

if __name__ == '__main__':
    unittest.main()