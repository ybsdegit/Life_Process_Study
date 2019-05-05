#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/5/5 15:10
# @author: Paulson●Wier
# @file: 发送邮件.py
# @desc:

import smtplib, time
from email.message import Message
from time import sleep
import email.utils
from StudyPacticePython.Practice.config import USER, PASSWORD, SMTPSERVER, FROM_ADDR, TO_ADDR

smtpserver = SMTPSERVER
username = USER
password = PASSWORD

time = email.utils.formatdate(time.time(), True)

def Sendmail(from_addr, to_addr, msg):
    message = Message()
    message['Subject'] = msg['subject']
    message['From'] = from_addr
    message['To'] = to_addr
    message.set_payload(msg['content'] + '\n' + time)
    m = message.as_string()

    sm = smtplib.SMTP_SSL(smtpserver, port=465, timeout=20)
    sm.ehlo()  # 初始化 SMTP 或 ESMTP 会话
    # sm.starttls()  # 启用 TLS 模式，默认 keyfile 和 certfile 为空如果给定使用这两个文件来创建安全套接字
    # sm.ehlo()
    sm.login(username, password)  # 使用用户和授权码来登录服务器
    sleep(2)
    sm.sendmail(from_addr, to_addr, m.encode('utf8'))
    sleep(2)
    sm.quit()
    return True


if __name__ == '__main__':
    from_addr = FROM_ADDR
    to_addr = TO_ADDR
    msg = {'subject':'this is a test project', 'content':'this is test content \n 测试内容'}
    Sendmail(from_addr, to_addr, msg)
    print('done')