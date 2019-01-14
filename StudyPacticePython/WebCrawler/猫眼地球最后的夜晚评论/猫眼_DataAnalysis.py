#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/6 18:52
# @Author  : yb.w
# @File    : 数据可视
# import csv
#
# from pyecharts import Style
# from  pyecharts import Geo
import csv

import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from os import path
import matplotlib.font_manager as fm
import jieba
from wordcloud import WordCloud,ImageColorGenerator


cityName = []
gender = []
nickName = []
userLevel = []
score = []
startTime =[]
content = []


def read_csv1():
    #读取文件内容
    # with open('maoyan_last_year.csv','r',encoding='utf-8',newline='') as f:
    #     #读文件
    #     reader = csv.reader(f)
    #
    #     i = 0
    #     for row in reader:
    #
    df = pd.read_csv('maoyan_last_year.csv',encoding='utf-8')
    df['城市'] = df['所在城市']
    df.to_csv('猫眼.csv', index=False)
    return df

def read_csv2():
    content = []
    with open('maoyan_last_year.csv','r',encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i != 0:
                cityName.append(row[0])
                gender.append(row[1])
                nickName.append(row[2])
                userLevel.append(row[3])
                score.append(row[4])
                startTime.append(row[5])
                content += row[6]
            i = i + 1


        #comment = [cityName,gender,nickName,userLevel,score,startTime,content]

        print('一共有：' + str(i-1) + '个')
        return content



def pie_sex_chart1(df):
    # 绘制饼图并保存

    count = df['评论者性别'].value_counts()
    print(count)

    plt.pie(count,labels=count.keys(),labeldistance=1.4,autopct='%2.1f%%')
    plt.axis('equal') #使饼图为正圆形
    plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1))
    plt.savefig('pie_chart.jpg')
    plt.show()

#评论者性别分布可视化
def pie_sex_chart2():
    from pyecharts import Pie
    list_num = []
    list_num.append(gender.count("('',)"))
    list_num.append(gender.count("(1,)"))
    list_num.append(gender.count("(2,)"))
    attr = ['其他','男','女']
    pie = Pie('性别饼图')
    pie.add('',attr,list_num,is_label_show=True)
    pie.render('sex_pie.html')

#评论者所在城市分布可视化
def city_distribution(cityName):
    city_list = list(set(cityName))
    city_dict = {city_list[i]: 0 for i in range(len(city_list))}
    for i in range(len(city_list)):
        city_dict[city_list[i]] = cityName.count(city_list[i])
    # 根据数量(字典的键值)排序
    sort_dict = sorted(city_dict.items(), key=lambda d: d[1], reverse=True)
    city_name = []
    city_num = []
    for i in range(len(sort_dict)):
        city_name.append(sort_dict[i][0])
        city_num.append(sort_dict[i][1])

    import random
    from pyecharts import Bar
    bar = Bar("评论者城市分布")
    bar.add("", city_name, city_num, is_label_show=True, is_datazoom_show=True)
    bar.render("city_bar.html")


#词云
def word_cloud(content):
    # 设置分词
    # comment_after_split = jieba.cut(str(comments), cut_all=False)  # 非全模式分词，cut_all=false
    # words = " ".join(comment_after_split)  # 以空格进行拼接
    # # print(words)

    words = ''.join(jieba.cut(str(content),cut_all=False))

    text = ''
    for line in df['评论内容']:
        text += line
    #使用jieba模块将字符串分割为单词列表
    cut_text = ''.join(jieba.cut(text))
    print(cut_text)
    # 导入背景图
    bg_image = plt.imread('bg1.jpg')

    # 设置词云参数，参数分别表示：画布宽高、背景颜色、背景图形状、字体、屏蔽词、最大词的字体大小
    wc = WordCloud(
                   background_color="white",  # 设置背景为白色，默认为黑色
                   width=890,  # 设置图片的宽度
                   height=600,  # 设置图片的高度
                   mask=bg_image,
                   # margin=10,  # 设置图片的边缘
                   max_font_size=150,  # 显示的最大的字体大小
                   random_state=50,  # 为每个单词返回一个PIL颜色
                   font_path="‪C:\Windows\Fonts\YaHei.Consolas.1.12.ttf",
                   )
    wc.generate_from_text(cut_text)



    # 将分词后数据传入云图
    wc.generate_from_text(words)
    plt.imshow(wc)
    plt.axis('off')  # 不显示坐标轴
    plt.show()
    # 保存结果到本地
    wc.to_file('词云图.jpg')


if __name__ == '__main__':
    df = read_csv1()
    content = read_csv2()
    pie_sex_chart2()
    city_distribution(cityName)
    word_cloud(content)