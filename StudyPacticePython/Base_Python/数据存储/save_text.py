#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 11:29
# @Author  : yb.w
# @File    : save_text.py
import requests
from pyquery import PyQuery as pq
url = 'https://www.zhihu.com/explore'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    person_title = item.find('.bio').text()
    content = item.find('.content').text()
    # file = open('explore.txt','a',encoding='utf-8')
    # file.write('\n'.join([question,author,person_title,content]))
    # file.write('\n'+'='*50+'\n')
    # file.close()

    with open('explore.txt','w',encoding='utf-8') as f:
        f.write('\n'.join([question,author,person_title,content]))
        f.write('\n'+'='*50+'\n')


'''
r，以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb，以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+，打开一个文件用于读写。文件指针将会放在文件的开头。
rb+，以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w，打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb ，以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+， 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+，以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a，打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+，打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+，以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''