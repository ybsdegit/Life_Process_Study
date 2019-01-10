#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 22:20
# @Author  : yb.w
# @File    : base_PyQuery.py

'''
如果你对 Web 有所涉及，
如果你比较喜欢用 CSS 选择器，
如果你对 jQuery 有所了解，
那么这里有一个更适合你的解析库—— PyQuery。
'''

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
# doc =pq(html)
# print(doc('li'))

'''
1. URL初始化

初始化的参数不仅可以以字符串的形式传递，
还可以传入网页的 URL，在这里只需要指定参数为 url 即可：
'''

# doc = pq(url='http://cuiqingcai.com')
# print(doc('title'))

'''
2. 文件初始化

当然除了传递一个 URL，
还可以传递本地的文件名，
参数指定为 filename 即可
'''

# doc = pq(filename='test.html')
# print(doc('li'))

'''
3. 基本CSS选择器
'''

# doc = pq(filename='test.html')
# print(doc('#container .list li'))
# print(type(doc('#container')))

'''
4. 查找节点
'''

#子节点
#查找子节点需要用到find()方法，
#传入的参数是CSS选择器
doc = pq(filename='test.html')
# items = doc('.list')
# print(items)
# print(type(items))
#
# lis = items.find('li')
# print(type(lis))
# print(lis)


#其实 find() 的查找范围是节点的所有子孙节点，
#而如果我们只想查找子节点，那可以用 children() 方法：
# lis = items.children()
# print(type(lis))
# print(lis)

# 如果要筛选所有子节点中符合条件的节点，
# 比如我们想筛选出子节点中 class 为 active 的节点，
# 可以向 children() 方法传入 CSS 选择器 .active：
# lis = items.children('.item-1')
# print(lis)


#父节点
#我们可以用 parent() 方法来获取某个节点的父节点

# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)


# 如果我们想获取某个祖先节点怎么办呢？可以用 parents() 方法：
# items = doc('.list')
# # print(parents)
# parents = items.parents('.wrap')
# print(parents)


# 兄弟节点
# 在上面我们说明了子节点和父节点的用法，
# 还有一种节点那就是兄弟节点，
# 如果要获取兄弟节点可以使用 siblings() 方法。
li = doc('.list .item-0.active')
print(li.siblings('.item-0'))
