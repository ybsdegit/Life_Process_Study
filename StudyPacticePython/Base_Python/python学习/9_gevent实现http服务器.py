#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 20:14
# @Author  : Paulson
# @File    : 9_gevent实现http服务器.py
# @Software: PyCharm
# @define  : function

import re
import socket
import gevent  # 携程程
from gevent import monkey

monkey.patch_all()


def service_client(new_socket):
    """
    为这个客户端返回数据
    :return:
    """

    # 1. 接收浏览器发送过来的请求，即http请求
    # Get / HTTP/1.1
    file_name = ''
    request = new_socket.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()
    print("")
    print(">"*20)
    print(request_lines)

    # 2. 返回http格式的数据给浏览器
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*"*50, file_name)
        if file_name == '/':
            file_name = '/index.html'

    try:
        f = open("./html" + file_name, "rb")
    except Exception as e:
        print(len(str(e)))
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "-----file not found---"
        new_socket.send(response.encode('utf-8'))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        # 2.2 准备发送给浏览器的数据---body
        # 将response header 发送给浏览器
        new_socket.send(response.encode('utf-8'))
        # 讲 body 发送给浏览器
        new_socket.send(html_content)

    # new_socket.send(response.encode('utf-8'))
    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    #  1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close ，即服务器4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时，可以立即访问
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #  2. 绑定
    tcp_server_socket.bind(("", 7890))
    #  3. 监听套接字
    tcp_server_socket.listen(128)
    while True:
        #  4. 等待新客户端的连接
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 为这个客户端服务
        gevent.spawn(service_client, new_socket)
        # new_socket.close()  #多线程不需要，不复制资源
        # service_client(new_socket)
    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
