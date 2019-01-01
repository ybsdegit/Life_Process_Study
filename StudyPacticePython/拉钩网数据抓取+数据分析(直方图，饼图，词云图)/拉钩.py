#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/1 0:29
# @Author  : yb.w
# @File    : 拉钩.py


import requests
import math
import pandas as pd
import time

def get_json(url,num):

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 8.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Cookie":"_ga=GA1.2.638044571.1520341071; user_trace_token=20180306205751-fa94dc20-213d-11e8-b12a-5254005c3644; LGUID=20180306205751-fa94e400-213d-11e8-b12a-5254005c3644; _gid=GA1.2.1115326601.1546259516; JSESSIONID=ABAAABAABEEAAJA1A9E8BD18BB416B213DBA414723C2E86; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546259534,1546273934,1546273940,1546326319; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546326319; LGSID=20190101150518-98e89d2e-0d93-11e9-b765-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DRvFvawzoR0eq43i7836lyqOqa_tf8leLr7IC1Q7dDuw3Xj46gE8ezerz-p9Z7TW8%26wd%3D%26eqid%3Dfb37f67400071a9c000000035c2b1122; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; LGRID=20190101150518-98e89fdf-0d93-11e9-b765-525400f775ce; SEARCH_ID=0bc733db9e7e4609915dde3b136e9169",
        "Host":"www.lagou.com",
        "Origin":"https://www.lagou.com",
        "Referer":"https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With':'XMLHttpRequest'
    }

    data = {
        'first':'true',
        'pn': num,
        'kd': '自动化测试工程师',
    }

    res = requests.post(url,headers=headers,data=data)
    res.raise_for_status()
    res.encoding = 'utf-8'

    page = res.json()
    return page

def get_page_num(count):
    #计算要抓取的页数
    #每页15个岗位，向上取整
    res = math.ceil(count/15)
    #拉钩网最多显示30页结果

    if res > 30:
        return 30
    else:
        return res

def get_page_info(jobs_list):
    #获取网页信息
    page_info_list = []
    for i in jobs_list:
        job_info = []
        job_info.append(i['companyShortName'])
        job_info.append(i['companySize'])
        job_info.append(i['positionName'])
        job_info.append(i['salary'])
        job_info.append(i['workYear'])
        job_info.append(i['education'])
        job_info.append(i['district'])
        job_info.append(i['positionAdvantage'])
        page_info_list.append(job_info)
    return page_info_list


def main(page_num):
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    #先设定页数为1，获取总得职位数
    page_1 = get_json(url,1)
    total_count = page_1['content']['positionResult']['totalCount']

    num = get_page_num(total_count)

    total_info = []
    time.sleep(20)
    print('职位总数{}，页数{}'.format(total_count,num))

    for n in range(1,page_num+1):
        page = get_json(url,n)

        print("开始抓取第{}页数据".format(n))

        job_list = page['content']['positionResult']['result']

        page_info = get_page_info(job_list)

        total_info += page_info

        time.sleep(30)  #每次抓取完成后，暂停一会，防止被服务器拉黑

        print("第{}页数据抓取完毕".format(n))

    #将总数据转化为 data frame 再输出

    df = pd.DataFrame(data = total_info,columns=['公司全名','公司规模','职位名称','薪资水平','工作经验','学历要求','区域','职位福利'])
    df.to_csv('lagou_job.csv',index = False)
    print('已保存为CSV文件')



if __name__ == '__main__':
    # 从外部获取页数
    page_num = int(input("请输入页数"))
    if page_num < 30:
        page_num = page_num
    else:
        page_num = 30

    main(page_num)




# #遍历数据
#     for i in result:
#         # 公司名称
#         companyShortName = i['companyShortName']
#         # 职位
#         positionName = i['positionName']
#         #学历要求
#         education = i['education']
#         #
#         firstType = i['firstType']
#         #
#         industryField = i['industryField']
#         #薪资
#         salary = i['salary']
#         #开发类型
#         secondType = i['secondType']
#         #工作年限
#         workYear = i['workYear']
#         #地区
#         businessZones = i['businessZones']
#         #福利
#         companyLabelList = i['companyLabelList']
#
#     # 保存数据
#         with open(region+word+'.csv','a') as f:
#             f.write('{},{},{},{},{},{},{},{},{},{}\n'.format(companyShortName,positionName,education,salary,workYear,firstType,industryField,secondType,businessZones,companyLabelList))





