#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 23:51
# @Author  : yb.w
# @File    : 验证码.py
import random

from PIL import Image, ImageFont, ImageFilter
from PIL.ImageDraw import ImageDraw

#生成大写字母
def rnd_char():
    return chr(random.randint(65,90)) #快速导入模块 ALt +enter

#生成数字+字母
def get_rand(num,many):
    for i in range(many):
        s =""
        for j in range(num):
            n =random.randint(1,2)  #n =1 数字 n=2 字母
            if n == 1:
                num1 = random.randint(1,9)
                s += str(num1)
            else:
                n1 = random.randint(1,2) # 1大写 2小写
                n2 = random.randint(1,26)
                if n1 == 1:
                    num1 = chr(64+n2)
                    s += num1
                else:
                    num1 = chr(96+ n2)
                    s += num1
        return s

#生成随机颜色
def rad_color1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rad_color2():
    return  (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60*4
height = 60

image = Image.new("RGB",(width,height),(0,0,0))

#创建front字体
font = ImageFont.truetype("msyh.ttc",36)

#创建绘图对象
draw = ImageDraw(image)

#填充每个像素点
for i in range(width):
    for j in range(height):
        draw.point((i,j),rad_color2())

for i in range(4):
    draw.text((60*i+10,10),get_rand(1,4),font=font,fill=rad_color1())

#模糊滤镜
image = image.filter(ImageFilter.BLUR)
image.show()

image.save('yanzheng.jpg')
# with open('yanzhengma.jpg','wb') as f:
#     f.write(image.save())


