#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/28 15:16
# @author: Paulson●Wier
# @file: 实例属性和类属性.py
# @desc:

'''
由于python是动态语言，根据类创建的实例可以任意绑定属性
给实例绑定属性的方法是通过实例变量，或者通过self变量
'''


'''
class Student(object):
    def __init__(self,name):
        self.name=name


s = Student('Bob')
s.score = 90


'''

# 如果Student类本身需要绑定一个属性，可以直接在class中定义属性，这种属性是类属性，归Student

# class Student(object):
    # name = "Sdudent"

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count +=1
        #在类的函数中也不能直接引用count类属性，需要Student.count


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


'''
小结
实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
'''


