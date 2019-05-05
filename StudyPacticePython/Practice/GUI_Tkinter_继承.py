#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/5 16:24
# @author: Paulson●Wier
# @file: GUI_Tkinter_继承.py
# @desc:

# 导入库
import tkinter as tk


# 继承类
class Application(tk.Frame):

    # 构造函数
    def __init__(self, master=None):
        # 调用父类
        super().__init__(master)
        # 调整大小和位置
        self.pack()
        # 调用后面的内容
        self.create_widgets()

    # 创建窗口
    def create_widgets(self):
        # say_hello 按钮
        self.say_hello = tk.Button(self, text="click me to say\nHello World",command=self.say_hello)
        self.say_hello.pack(side="top")
        # 退出按钮
        self.quit = tk.Button(self, text="退出", fg="blue", command=root.destroy)
        self.quit.pack(side="bottom")

        # 构造功能函数
    def say_hello(self):
        print("hello_world")


# 实例化对象
root = tk.Tk()
# 设置标题
root.title("继承")
# 类的继承
app = Application(master=root)
# 程序循环
app.mainloop()