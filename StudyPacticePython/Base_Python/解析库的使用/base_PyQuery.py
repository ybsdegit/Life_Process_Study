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

# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''

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
# doc = pq(filename='test.html')
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
# li = doc('.list .item-0.active')
# print(li.siblings('.item-0'))


# Twisted-18.9.0.tar.bz2
'''
适用于3.7
pip install D:\Twisted-18.9.0-cp37-cp37m-win_amd64.whl 

pip install D:\Twisted-18.9.0-cp36-cp36m-win_amd64.whl 
scrapy startproject ScrapyStudy
'''

'''
5. 遍历
'''

# doc = pq(filename='test.html')


# li = doc('.item-0.active')
# #对于单个节点来说，我们可以直接打印，也可以直接转成字符串
# print(li)
# print(str(li))

#对于多个及诶单的结果，我们需要遍历来获取

# lis = doc('li').items()
# # for li in lis:
# #     print(li,type(li))


'''
6. 获取信息
'''

#获取属性
#提取某个节点之后，可以调用attr()方法来获取属性：

# doc = pq(filename='test.html')
# a = doc('.item-0.active a')
# print(a,type(a))
# print(a.attr('href'))
# print(a.attr.href)
#
# b = doc('a')
# print(a.attr.href)



# 所以当返回结果包含多个节点时，调用 attr() 方法只会得到第一个节点的属性。
# 如果想要获取所有的a节点的属性，可以用  遍历

# doc = pq(filename='test.html')
# a = doc('a')
# for item in a.items():
#     print(item.attr.href)


#获取文本
# 使用text()方法获取文本

# doc = pq(filename='test.html')
# a = doc('.item-0.active a')
# print(a.text())


# 如果我们想要获取这个节点内部的 HTML 文本，就可以用 html() 方法
# li = doc('.item-0.active')
# print(li)
# print(li.html())


#选中的结果是多个节点，text() 或 html() 会得到第一节点的内部文本或内部文档
# li = doc('li')
# print(li.text())
# print(li.html())

#如果要获取所有文本，使用遍历的方法

# for lis in li.items():
#     print(lis.text())


'''
7. 节点操作
'''

#addClass、removeClass

# doc = pq(filename='test.html')
# li = doc('.item-0.active')
# print(li)
#
# li.removeClass('active')
# print(li)
#
# li.addClass('active')
# print(li)


#attr、text、html
# 当然除了操作 class 这个属性，也有 attr() 方法来专门针对属性进行操作，
# 也可以用 text()、html() 方法来改变节点内部的内容。

# html = '''
# <ul class="list">
#      <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# </ul>
# '''

# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name','link')
# print(li)
#
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)
'''
所以说，attr() 方法如果只传入第一个参数属性名，则是获取这个属性值，如果传入第二个参数，可以用来修改属性值，
text() 和 html() 方法如果不传参数是获取节点内纯文本和 HTML 文本，如果传入参数则是进行赋值。
'''

#remove 移除
# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
#
# #移除p节点信息
#
# wrap.find('p').remove()
# print(wrap.text())



'''
8. 伪类选择器
'''

doc = pq(filename='test.html')
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)

'''
更多的 CSS 选择器的用法可以参考：http://www.w3school.com.cn/css/index.asp
9. 结语
到此为止 PyQuery 的常用用法就介绍完了，如果想查看更多的内容可以参考一下 PyQuery 的官方文档：http://pyquery.readthedocs.io，相信有了它，解析网页不再是难事。
'''