#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/5 16:14
# @author: Paulson●Wier
# @file: GUI_Tkinter_Button.py
# @desc:

import tkinter as tk

#实例化对象
root=tk.Tk()
#设置标题
root.title('Button Tkinter ——按钮')

def hello_world():
    print('Hello world')

# 创建按钮并居中
button = tk.Button(root, text='this is a button', fg='blue', command=hello_world)
button.pack()

root.mainloop()