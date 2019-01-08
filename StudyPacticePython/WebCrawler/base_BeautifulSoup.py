#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 22:19
# @Author  : yb.w
# @File    : base_BeautifulSoup.py

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
html1 = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""

from bs4 import BeautifulSoup

# soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())

# print(soup.title)
# print(type(soup.title))  #类型
# print(soup.title.string) #输出文本内容
# print(soup.head)
# print(soup.a)
# print(soup.a.string)
# print(soup.title.name)
# print(soup.p.attrs)
#
# print(soup.p['name'])
# print(soup.p['class'])
#
# print(soup.p.string)
#
# print(soup.head.title.string)

# soup1 = BeautifulSoup(html1,'lxml')
# print(soup1.p.children)

# for i,child in enumerate(soup1.p.children):     #得到所有的儿子节点
    # print(i,child)

# for i,child in enumerate(soup1.p.descendants):   #得到所有的子孙节点的话可以调用 descendants 属性
    # print(i,child)

# print(soup1.p.parent)

# print('Next Sibling',soup1.a.next_sibling)  #获取下一个节点的元素
# print('Prew Sibling',soup1.a.previous_sibling) #获取上一个节点的元素
# print(list(enumerate(soup1.a.next_siblings))) #返回下一个元素的生成器

html2 = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""

from bs4 import BeautifulSoup


# soup = BeautifulSoup(html2,'lxml')
# print("Next Sibling: ")
# print(type(soup.a.next_sibling))
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.string)
#
# print('Parent: ')
# print(type(soup.a.parents))
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])
# print(list(soup.a.parents)[1])


#方法选择器

#find_all()


html3='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html3,'lxml')

'''
这里我们调用了 find_all() 方法，
传入了一个 name 参数，参数值为 ul，
也就是说我们想要查询所有 ul 节点，
返回结果是列表类型，长度为 2，
每个元素依然都是 bs4.element.Tag 类型。

print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

'''

'''
attrs
除了根据节点名查询，
我们也可以传入一些属性来进行查询，
我们用一个实例感受一下：

里我们查询的时候传入的是 attrs 参数，
参数的类型是字典类型，
比如我们要查询 id 为 list-1 的节点，
那就可以传入attrs={'id': 'list-1'} 的查询条件，
得到的结果是列表形式，
包含的内容就是符合 id 为 list-1 的所有节点，
上面的例子中符合条件的元素个数是 1，
所以结果是长度为 1 的列表。
'''

# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'name':'elements'}))


'''
text
text 参数可以用来匹配节点的文本，
传入的形式可以是字符串，
可以是正则表达式对象，
我们用一个实例来感受一下：
'''
import re
html4='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
# soup4 = BeautifulSoup(html4,'lxml')
# print(soup4.find_all(text=re.compile('Hello')))


'''
find()
除了 find_all() 方法，还有 find() 方法，
只不过 find() 方法返回的是单个元素，
也就是第一个匹配的元素，
而 find_all() 返回的是所有匹配的元素组成的列表
'''

html5='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup5 = BeautifulSoup(html5,'lxml')
print(soup5.find(name='ul'))
print(soup5.find(class_='list'))

'''
find_parents() find_parent()
find_parents() 返回所有祖先节点，find_parent() 返回直接父节点。
find_next_siblings() find_next_sibling()
find_next_siblings() 返回后面所有兄弟节点，find_next_sibling() 返回后面第一个兄弟节点。
find_previous_siblings() find_previous_sibling()
find_previous_siblings() 返回前面所有兄弟节点，find_previous_sibling() 返回前面第一个兄弟节点。
find_all_next() find_next()
find_all_next() 返回节点后所有符合条件的节点, find_next() 返回第一个符合条件的节点。
find_all_previous() 和 find_previous()
find_all_previous() 返回节点后所有符合条件的节点, find_previous() 返回第一个符合条件的节点
'''

'''
推荐使用 LXML 解析库，必要时使用 html.parser。
节点选择筛选功能弱但是速度快。
建议使用 find()、find_all() 查询匹配单个结果或者多个结果。
如果对 CSS 选择器熟悉的话可以使用 select() 选择法。
'''