#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 23:35
# @Author  : yb.w
# @File    : 18_12_12_Sister.py
import os
import requests
from pyquery import PyQuery as pq
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

def get_requests(url):
    html = requests.get(url=url,headers=headers).content.decode("utf-8")
    doc = pq(html)
    items = doc('.span3').items()

    for each in items:
        # 向下查找 追加一个属性
        url_img = each.find("img").attr("src")
        name = each.find("img").attr("title")
        #再次请求网络 获取图像内容
        download_img = requests.get(url_img,headers=headers).content
        print('图片名字: %s 图片链接：%s'%(name,url_img))
        try:
            with open('./12_12_妹纸图/'+name+'.jpg','wb') as f:
                f.write(download_img)
        except OSError:
            continue


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(),'12_12_妹纸图')
    #判断路径是否存在
    if not os.path.exists(file_path):
        #不存在就创建这个文件夹
        os.makedirs(file_path)
    for item in range(1,15):
        url = "https://www.dbmeinv.com/?pager_offset=%s"%str(item)
        get_requests(url)


