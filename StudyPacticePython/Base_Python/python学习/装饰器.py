#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 22:36
# @Author  : Paulson
# @File    : 装饰器.py
# @Software: PyCharm
# @define  : function

# 私有属性添加getter和setter方法
# class Foo:
#
#     def func(self):
#         pass
#
#     # 定义property 属性
#     @property
#     def prop(self):
#         return 1
#
#
# foo_obj = Foo()
# foo_obj.func()  # 调用实例方法
# s = foo_obj.prop    # 调用property 属性
# print(s)


# 使用property升级getter和setter方法
# class Money(object):
#     """
#     私有属性添加getter和setter方法
#     """
#     def __init__(self):
#         self.__money = 0  # 私有变量
#
#     def get_money(self):
#         return self.__money
#
#     def set_money(self, value):
#         if isinstance(value, int):
#             self.__money = value
#         else:
#             print("error: 不是整形数字")
#
#     # 定义一个属性，当这个money设置值时调用setMoney,当获取值时调用getMoney
#     money = property(get_money, set_money)
#
#
# a = Money()
# a.money = 100  # 调用setMoney 方法
# print(a.money)  # 调用getMonet 方法


# 3. 使用property取代getter和setter方法
class Money(object):
    def __init__(self):
        self.__money = 0

    # 使用装饰器对money进行装饰，那么会自动添加一个叫money的属性，
    # 当调用获取money的值时，调用装饰的方法
    @property
    def money(self):
        return self.__money

    # 使用装饰器对money进行装饰，当对money设置值时，调用装饰的方法
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error")


a = Money()
a.money = 100
print(a.money)

