#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 15:27
# @Author  : yb.w
# @File    : maoyan_last_year.py

import json
import time

import pandas as pd
import requests

#获取数据
def get_data(url):
    headers = {
    'Cookie':'lxsdk_cuid=167f9b04329c8-043d664148d302-6313363-100200-167f9b0432ac3; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=121549239.1546082337646.1546102449426.1546604230576.9; uuid_n_v=v1; iuuid=B9B6FF10101B11E9893C4561AE8566B782CCB0DCAB494811A1C14617B9CD967F; webp=true; ci=1%2C%E5%8C%97%E4%BA%AC; _lxsdk=B9B6FF10101B11E9893C4561AE8566B782CCB0DCAB494811A1C14617B9CD967F; _lxsdk_s=16818c9a875-42f-7c9-e40%7C%7C61',
    'Host' : 'm.maoyan.com',
    'Referer': 'http://m.maoyan.com/movie/345036/comments?_v_=yes',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
    }

    html = requests.get(url=url,headers=headers)
    print(html.status_code)
    if html.status_code == 200:
        return  html.content
    else:
        return None

#处理接口返回数据
def parse_data(html):
    print(html)
    json_data = json.loads(html,encoding='utf-8')['cmts']
    print(json_data)
    comments = []
    for item in json_data:
        cityName = item['cityName']
        gender = item['gender'] if 'gender' in item else '',
        nickName = item['nickName']
        userLevel = item['userLevel']
        score = item['score']
        startTime = item['startTime']
        content = item['content']

        comment = [cityName,gender,nickName,userLevel,score,startTime,content]
        comments.append(comment)
    return comments


#处理链接及存储数据
def file_save(comments):
    print(comments)
    name = ['所在城市', '评论者性别', '评论者昵称', '猫眼等级', '评分', '评论日期', '评论内容']
    df = pd.DataFrame(data=comments, columns=name)
    df.to_csv('maoyan_last_year.csv', index=False)



def main():
    # 2018-12-31大陆上映
    startTime = '2019-01-01'
    offset = 0
    total_info = []
    all_total_info = []
    page_num = int(150 / 15)  #150条数据
    # day= [1,2,3,4,5,6]
    for n in range(6):
        startTime = '2019-01-0%d' % n
        print("开始爬取{}数据".format(startTime))
        for i in range(page_num):
            offset = i*15
          # url = 'http://m.maoyan.com/mmdb/comments/movie/1049245982.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset, startTime)
            url = 'http://m.maoyan.com/mmdb/comments/movie/345036.json?_v_=yes&offset={0}&startTime={1}%2021%3A09%3A31'.format(offset, startTime)
            print(url)
            html = get_data(url)
            comments = parse_data(html)
            total_info += comments
            # time.sleep(2)  # 每次抓取完成后，暂停一会，防止被服务器拉黑
            print("第{}页数据抓取完毕".format(i))
    all_total_info += total_info
    file_save(all_total_info)


if __name__ == '__main__':
    main()
    



