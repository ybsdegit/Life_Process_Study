#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 22:34
# @Author  : yb.w
# @File    : findIp.py

from tkinter import *
import requests,re


def get_content():
    #获得输入框中的IP信息
    ip = ip_input.get()
    #模拟浏览器请求网络
    headers={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }

    #请求网络
    response = requests.get("https://www.ipip.net/ip/().html".format(ip),headers=headers).text
    # print(response)

    ipnow = re.search(r'当前IP.*?html">(.*?)</a>',response,re.S)
    wrap = re.search(r'地区中心经纬度.*?;">(.*?)</span>',response,re.S)
    address = re.search(r'地理位置.*?;">(.*?)<span',response,re.S)
    print(ipnow,wrap,address)

    if ipnow:
        ip_info=['ip地址'+ipnow.group(1)]
        if wrap:
            ip_info.insert(0,'地区中心经纬度:' + wrap.group(1))
        if address:
            ip_info.insert(0,'地理位置:' + address.group(1))

        display_info.delete(0,5)

        for item in ip_info:
            display_info.insert(0,item)
    else:
        display_info.delete(0,5)
        display_info.insert(0,'这是无效的IP地址。')

#创建一个窗口
root = Tk()
#标题
root.title("这是一个查询IP地址的小程序")
#设置 输入框 规定尺寸
ip_input = Entry(root,width = 40)
#创建一个回显列表
display_info = Listbox(root,width=60,height=10)
#创建查询按钮
result_button = Button(root,command=get_content,text="查 询")



def main():
    #显示桌面
    ip_input.pack()
    display_info.pack()
    result_button.pack()

    #运行
    root.mainloop()

if __name__ == '__main__':
    main()