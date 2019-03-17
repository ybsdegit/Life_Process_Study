#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/25 20:57
# @author: Paulson●Wier
# @file: 类和实例.py
# @desc:

'''
类和实例
面向对象最重要的概念就是类（Class）和实例（Instance）
必须牢记类是抽象的模板，比如Student类，
而实例是根据类创建出来的一个个具体的“对象”，
每个对象都拥有相同的方法，但各自的数据可能不同

'''

class Student(object):

    def __init__(self, name, score):
        # 如果要让内部属性不被外部访问，
        # 可以把属性的名称前加上两个下划线__，
        # 在Python中，实例的变量名如果以__开头，
        # 就变成了一个私有变量（private），
        # 只有内部可以访问，外部不能访问，
        self.__name = name
        self.__score = score

    #注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

    '''
    class后面紧接着是类名，即Student，
    类名通常是大写开头的单词，
    紧接着是(object)，表示该类是从哪个类继承下来的，
    继承的概念我们后面再讲，
    通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
    
    '''

    def print_score(self):
        print('%s:% s' %(self.__name,self.__score))


    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


    def get_name(self):
        return self.__name


    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')











lisa = Student('Lisa', 99)
bart = Student('Bart', 59)

# print(lisa.__name,lisa.get_grade())
# print(bart.__name,bart.get_grade())


