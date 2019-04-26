#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/4/16 16:45
# @author: Paulson●Wier
# @file: read_write_csv.py
# @desc:

import csv


def read_csv():
    with open('city.csv', 'r', encoding='utf-8') as f:
        # s = f.read()
        s = csv.reader(f)
        for i in s:
            print(i)


def save_csv():
    header = ["name", "gender", "score"]
    file_1 = ["zhang_san", "male", "100"]
    file_2 = ["Li_si", "male", "80"]
    # 如果不加,newline=””会多一行空行
    with open(r'.\file\city_2.csv', 'w', encoding='utf-8', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(file_1)
        writer.writerow(file_2)

save_csv()