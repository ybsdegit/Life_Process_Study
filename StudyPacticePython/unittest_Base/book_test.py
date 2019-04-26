#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/19 16:09
# @author: Paulson●Wier
# @file: book_test.py
# @desc:
from StudyPacticePython.unittest_Base import book_main
import unittest


class book_test(unittest.TestCase):
    global instance
    instance = book_main(name="Harry Potter", page=350)

    def test_init(self):
        self.assertEqual(instance.name, "Harry Potter")
        self.assertEqual(instance.page, 350)
        self.assertTrue(isinstance(instance, dict))

    def test_key_add(self):
        instance.key1 = 'value1'
        self.assertTrue('key1' in instance)
        self.assertEqual(instance.key1, 'value1')

    def test_attr_add(self):
        instance["key2"] = "value2"
        self.assertTrue('key2' in instance)
        self.assertEqual(instance.key2, 'value2')

    def test_key_error(self):
        with self.assertRaises(KeyError):
            instance['empty']

    def test_attr_error(self):
        with self.assertRaises(AttributeError):
            instance.empty


def main():
    unittest.main()


if __name__ == '__main__':
    main()
