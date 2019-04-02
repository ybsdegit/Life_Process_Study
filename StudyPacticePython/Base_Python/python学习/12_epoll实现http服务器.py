#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 21:44
# @Author  : Paulson
# @File    : 12_epoll实现http服务器.py
# @Software: PyCharm
# @define  : function
'''
linux 系统可用
'''
import re
import socket
# import multiprocessing  # 多进程
import select


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

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    client_socket_list = list()

    fd_event_dict = dict()
    while True:
        fd_event_list =epl.poll()  # 默认会堵塞，直到OS 监测到数据到来，通过事件通知方式，告诉这个程序

        # [(fd, event)]  (套接字对应的文件描述符， 这个描述符到底是什么事件  比如recv接收)
        for fd, event in fd_event_list:
            # 4. 等待新客户端的连接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经连接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    epl.unregister(fd)
                    del fd_event_dict[fd]





        # try:
        #     new_socket, client_addr = tcp_server_socket.accept()
        # except Exception as ret:
        #     pass
        # else:
        #     new_socket.setblocking(False)
        #     client_socket_list.append(new_socket)

        # for client_socket in client_socket_list:
        #         recv_data = client_socket.recv(1024)
        #         if recv_data:
        #             service_client(client_socket, recv_data)
        #         else:
        #             client_socket.close()
        #             client_socket_list.remove(client_socket)

        # 5. 为这个客户端服务
    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()