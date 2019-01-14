#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/1 20:48
# @Author  : yb.w
# @File    : 拉钩_DataAnalysis.py
# 参照：https://blog.csdn.net/danspace1/article/details/80197106#1-%E7%94%A8%E5%88%B0%E7%9A%84%E8%BD%AF%E4%BB%B6%E5%8C%85


import pandas as pd
import matplotlib.pyplot as plt
# import statsmodels.api as sm
from wordcloud import WordCloud
from scipy.misc import imread
import jieba
from pylab import mpl

#使matlotlib模块能显示中文
# mpl.rcParams['front.sans_serif'] = ['SimHei']  #指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False #解决保存五香是负号‘-’显示方块的问题

mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def data_drop():

    #读取数据
    df = pd.read_csv('lagou_job_cekai.csv',encoding='utf-8')

    #数据清洗（剔除实习岗位）
    df.drop(df[df['职位名称'].str.contains('实习')].index,inplace=True)
    # print(df.describe())

    #由于CSV文件内的数据时字符串形式，先用正则表达式将字符串转化为列表，再取区间的均值
    pattern = '\d+'
    df['工作年限'] = df['工作经验'].str.findall(pattern)

    avg_work_year = []
    for i in df['工作年限']:
        #如果工作经验为'不限' 或'应届毕业生'，那么匹配值为空，工作年限为0
        if len(i) == 0:
            avg_work_year.append(0)
        #如果匹配值为一个数值，那么返回该数值
        elif len(i) == 1:
            avg_work_year.append(int(''.join(i)))
        #如果匹配值是一个区间，那么取平均值
        else:
            num_list = [int(j) for j in i]
            avg_year = sum(num_list)/2
            avg_work_year.append(avg_year)

    df['经验'] = avg_work_year

    #将字符串转换为列表，再取区间的前25%，比较贴近现实(工资)
    df['salary'] = df['薪资水平'].str.findall(pattern)

    avg_salary = []
    for k in df['salary']:
        int_list = [int(n) for n in k]
        avg_wage = int_list[0] +(int(int_list[1]-int_list[0]))/4
        avg_salary.append(avg_wage)

    df['月工资'] = avg_salary

    #将清洗后的数据保存，以便检查
    df.to_csv('draft.csv',index=False)
    return df, df['月工资']

def salary_describ():
    # 描述统计
    print('测试开发工程师工资描述：\n{}'.format(df['月工资'].describe()))

def histagram_image():
    #绘制频率直方图并保存
    plt.hist(salary_moth,bins=12)
    plt.xlabel('工资（千元）')
    plt.ylabel('频数')
    plt.title('工资直方图')
    plt.savefig('histogram.jpg')
    plt.show()


def pie_chart():
    # 绘制饼图并保存
    count = df['区域'].value_counts()
    print(count)

    plt.pie(count,labels=count.keys(),labeldistance=1.4,autopct='%2.1f%%')
    plt.axis('equal') #使饼图为正圆形
    plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1))
    plt.savefig('pie_chart.jpg')
    plt.show()

def word_cloud():
    text = ''
    for line in df['职位福利']:
        text += line
    #使用jieba模块将字符串分割为单词列表
    cut_text = ''.join(jieba.cut(text))
    # color_mask = imread('D:\\Desktop\\bb\\study\\Life_Process_Study\\StudyPacticePython\\WebCrawler\\xin.jpg')
    mask = plt.imread('xin.jpg')

    cloud = WordCloud(
        # font_path='yahei.ttf',
        font_path="‪C:\Windows\Fonts\YaHei.Consolas.1.12.ttf",
        background_color='white',
        mask=mask,
        max_words=1000,
        max_font_size=100
    )
    text_test = open('ciyun.txt', 'r', encoding='utf-8').read()

    word_cloud = cloud.generate(cut_text)
    # word_cloud = cloud.generate(text_test)
    #保存词云图片
    word_cloud.to_file('word_cloud.jpg')
    plt.imshow(word_cloud)
    plt.axis('on')
    plt.show()


if __name__ == '__main__':
    df,salary_moth = data_drop()
    # salary_describ()
    # histagram_image()
    # pie_chart()
    word_cloud()
