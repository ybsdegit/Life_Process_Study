#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 20:49
# @Author  : Paulson
# @File    : Mongo_demo.py
# @Software: PyCharm
# @define  : function

import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)




#2. 指定数据库
db = client.newtestdb

# db = client['test]

#4. 指定集合
collection = db.students

# collection = db['students']


# 5. 插入数据

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
collection.insert_one(student)

collection.insert_one({'name':'Bob'})
# collection.insert_one([student])
