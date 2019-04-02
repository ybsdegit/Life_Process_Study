#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 21:00
# @Author  : Paulson
# @File    : 11_单进程_单线程_非堵塞_长链接.py
# @Software: PyCharm
# @define  : function


import re
import socket
# import multiprocessing  # 多进程


def service_client(new_socket, request):
    """
    为这个客户端返回数据
    :return:
    """
    file_name = ''
    # 1. 接收浏览器发送过来的请求，即http请求
    # Get / HTTP/1.1
    # request = new_socket.recv(1024).decode('utf-8')
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
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "-----file not found---"
        new_socket.send(response.encode('utf-8'))
    else:
        html_content = f.read()
        f.close()

        # 2.1 准备发送给浏览器的数据---header
        # 2.2 准备发送给浏览器的数据---body
        # 将response header 发送给浏览器
        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += '\r\n'
        response = response_header.encode('utf-8') + response_body

        # 讲 body 发送给浏览器
        new_socket.send(response)


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
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    client_socket_list = list()
    while True:
        #  4. 等待新客户端的连接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as ret:
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

        # 5. 为这个客户端服务
    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
