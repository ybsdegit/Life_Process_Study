#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/13 9:52
# @author: Paulson●Wier
# @file: jiekou.py
# @desc:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return  "Hello world"

if __name__ == '__main__':
    app.run()