#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/5 16:05
# @author: Paulson●Wier
# @file: GUI_Tkinter.py
# @desc:

import tkinter as tk

# 实例化对象
root = tk.Tk()

# 设置标题
root.title('this is a GUI 界面')

# 创建Lable 标签
text = tk.Label(root, text='a simple tkinter GUI')

# 将文字居中
text.pack()

# 程序循环
root.mainloop()