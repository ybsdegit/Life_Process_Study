#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 20:16
# @Author  : Paulson
# @File    : save_Mongo.py
# @Software: PyCharm
# @define  : function

import pymongo
# 第一个参数为地址 host，第二个参数为端口 port，端口如果不传默认是 27017。
from pymongo import MongoClient

#1. 连接MongoDB
client = pymongo.MongoClient(host='localhost',port=27017)

# client1 = MongoClient('mongodb://localhost:27017/')

#2. 指定数据库
db = client.test

# db = client['test]

#4. 指定集合
collection = db.students

# collection = db['students']


# 5. 插入数据

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# 调用 collection 的 insert() 方法即可插入数据，
# insert()方法已经不推荐使用了。推荐使用insert_one() 和 insert_many()方法插入单条和多条记录
# insert_many() 方法返回的类型是 InsertManyResult，


# 调用inserted_ids 属性可以获取插入数据的 _id 列表，运行结果：
# result = collection.insert_one([student])
# result = collection.insert_many([student1,student2])
# print(result)
# print(result.inserted_ids)  #插入数据的列表


# 6. 查询
# 直接根据 ObjectId 来查询，这里需要使用 bson 库里面的 ObjectId。
# from bson.objectid import ObjectId
# result = collection.find_one({'_id':ObjectId('5c3dd3023d5eea397823eb61')})
# print(result)


# 对于多条数据的查询，我们可以使用 find() 方法，例如在这里查找年龄为 20 的数据，
# results = collection.find({'age':20})
# print(results)
# for result in results:
#     print(result)


# 如果要查询年龄大于 20 的数据，
# results = collection.find({'age':{'$gt':20}})
# print(results)
# for result in results:
#     print(result)

'''
$lt	    小于	          {'age': {'$lt': 20}}
$gt	    大于	          {'age': {'$gt': 20}}
$lte	小于等于	      {'age': {'$lte': 20}}
$gte	大于等于	      {'age': {'$gte': 20}}
$ne	    不等于	      {'age': {'$ne': 20}}
$in	    在范围内	      {'age': {'$in': [20, 23]}}
$nin	不在范围内	  {'age': {'$nin': [20, 23]}}
'''


# 另外还可以进行正则匹配查询，例如查询名字以 M 开头的学生数据，
# results = collection.find({'name':{'$regex':'^M.*'}})
# print(results)
# for result in results:
#     print(result)

'''
符号	    含义	          示例	                             示例含义
$regex	匹配正则	    {'name': {'$regex': '^M.*'}}	    name 以 M开头
$exists	属性是否存在	{'name': {'$exists': True}}	        name 属性存在
$type	类型判断	    {'age': {'$type': 'int'}}	        age 的类型为 int
$mod	数字模操作	{'age': {'$mod': [5, 0]}}	        年龄模 5 余 0
$text	文本查询	    {'$text': {'$search': 'Mike'}}	    text 类型的属性中包含 Mike 字符串
$where	高级条件查询	{'$where': 'obj.fans_count == obj.follows_count'}	自身粉丝数等于关注数

'''


# 7. 计数
# 要统计查询结果有多少条数据，可以调用 count() 方法，如统计所有数据条数：
#查询结果有多少条数据
# count = collection.find().count() #不推荐此方法
# print(count)

#查询符合某个条件的的数据
# count = collection.find({'age':20}).count()
# print(count)



#8.排序
# 可以调用 sort() 方法，传入排序的字段及升降序标志即可
# pymongo.ASCENDING 指定升序，如果要降序排列可以传入 pymongo.DESCENDING。
# results = collection.find().sort('name',pymongo.ASCENDING)
# print([result['name'] for result in results])



# 9. 偏移
# 在某些情况下我们可能想只取某几个元素，在这里可以利用skip() 方法偏移几个位置，
# 比如偏移 2，就忽略前 2 个元素，得到第三个及以后的元素。

# results = collection.find().sort('name',pymongo.DESCENDING).skip(2)
# print([result['name'] for result in results])


# 另外还可以用 limit() 方法指定要取的结果个数
# results = collection.find().sort('name',pymongo.DESCENDING).skip(2).limit(2)
# print([result['name'] for result in results])

# 值得注意的是，在数据库数量非常庞大的时候，如千万、亿级别，
# 最好不要使用大的偏移量来查询数据，很可能会导致内存溢出，可以使用类似如下操作来进行查询

# from bson.objectid import ObjectId
# collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})



# 10. 更新
# 对于数据更新可以使用 update() 方法，指定更新的条件和更新后的数据即可，例如：
# condition = {'name':'Mike'}
# student = collection.find_one(condition)
# student['age'] = 25
# result = collection.updata(condition,student)
# print(result)


# 另外 update() 方法其实也是官方不推荐使用的方法，在这里也分了 update_one() 方法和 update_many() 方法，用法更加严格，
# 第二个参数需要使用 $ 类型操作符作为字典的键名，我们用示例感受一下。

# condition = {'name': 'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 26
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.matched_count, result.modified_count)

# condition = {'age': {'$gt': 20}}
# result = collection.update_one(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)

# condition = {'age': {'$gt': 20}}
# result = collection.update_many(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)

# 11. 删除

# result = collection.remove({'name':'Mike'})
# print(result)



# 另外依然存在两个新的推荐方法，delete_one() 和 delete_many() 方法，示例如下：
# result = collection.delete_one({'name':'Jordan'})
# print(result)
# print(result.deleted_count)
# result = collection.delete_many({'age': {'$lt': 25}})
# print(result.deleted_count)


# 12. 更多
# 另外 PyMongo 还提供了一些组合方法，如find_one_and_delete()、find_one_and_replace()、find_one_and_update()，就是查找后删除、替换、更新操作，用法与上述方法基本一致。
# 另外还可以对索引进行操作，如 create_index()、create_indexes()、drop_index() 等。