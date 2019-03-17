#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/2/28 10:27
# @author: Paulson●Wier
# @file: 继承和多态.py
# @desc:

class Animal(object):
    def run(self):
        print('\nAnimal is running...')



class Dog(Animal):

    def run(self):
        print('\nDog is running...')
        L = []
        for i in range(10):
            L.append(i)
        print(L)
        print(L[::-1])


class Cat(Animal):

    def run(self):
        print('\nCat is running,too...')

def run_twice(animal):
    animal.run()
    animal.run()

class Timer(object):
    def run(self):
        print('Start...')

'''
小结
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
'''
# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Timer())

