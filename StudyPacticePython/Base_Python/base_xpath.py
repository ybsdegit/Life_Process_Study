#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 21:27
# @Author  : yb.w
# @File    : base.py

from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
text1 = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.parse('./test.html',etree.HTMLParser())


# result = html.xpath('//*')
# result = html.xpath('//li')
# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# result = html.xpath('//li[@class="item-0"]//text()')
# result = html.xpath('//li[@class="item-0"]/a/@href')
# result = html.xpath('//li[contains(@class,"li")]/a/text()')

html1 = etree.HTML(text1)
# result = html1.xpath('//li[contains(@class, "li-first")]/a/text()')
# result = html.xpath('//li[2]/a/text()')
# result = html.xpath('//li[last()]/a/text()')
# result = html.xpath('//li[position()<3]/a/text()')
# result = html.xpath('//li[last()-2]/a/text()')

result = html.xpath('//li[1]/ancestor::*') #获取所有的祖先节点
print(result)

result = html.xpath('//li[1]/ancestor::div')
print(result)


result = html.xpath('//li[1]/attribute::*') #获取所有的属性值
print(result)

result = html.xpath('//li[1]/descendant::*')  #获取所有的子孙节点
print(result)

result = html.xpath('//li[1]/child::*')  #获取所有的儿子节点
print(result)

result = html.xpath('//li[1]/following::*[2]')  #获取当前节点之后的所有节点
print(result)

result = html.xpath('//li[1]/following-sibling::*')  #可以获取当前节点之后的所有同级节点
print(result)
