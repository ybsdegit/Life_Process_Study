#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/28 17:18
# @author: Paulson●Wier
# @file: 6_1_读写csv.py
# @desc:

# import csv
# with open('1.csv') as f:
#     f_csv = csv.DictReader(f)
#     for row in f_csv:
#         print(row['Symbol'])

from collections import OrderedDict


# def output_result(result, log=None):
#     if log is not None:
#         log.debug('Cot: %r', result)
#
#
# def add(x, y):
#     return x + y
#
#
# if __name__ == '__main__':
#     import logging
#     from multiprocessing import Pool
#     from functools import partial
#
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test')
#
#     p = Pool()
#     p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
#     p.close()
#     p.join()


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)