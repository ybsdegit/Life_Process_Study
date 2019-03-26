# # -*- coding: utf-8 -*-
# """
# Created on Tue Feb 26 17:36:17 2019
#
# @author: liuyuying
# """
#
# from lxml import etree
# from selenium import webdriver
# #use selenium create Brower
# html_driver = webdriver.Chrome()
# #get all urls from start url
# def get_all_urls(s_url):
# 	#get html
#     # print(s_url)
#     html_driver.get(s_url)
#     #save urls
# 	urls=[]
# 	re_urls=[]
# 	#get links from start html
# 	for link in html_driver.find_elements_by_tag_name("a"):
# 		h = link.get_attribute('href')
# 		if h!=None and h!='':
# 			urls.append(h)
# 	#remove duplicate url
# 	for url in urls:
# 		if url not in re_urls:
# 			re_urls.append(url)
# 	return re_urls
# 	html_driver.close()
# #get all pagesource from urls
# def get_all_page_source(re_urls):
#     with open("pagesource.txt","w+",encoding='utf-8') as f:
#         for url in re_urls:
#         	print(url)
#         	html_driver.get(url)
#         	f.write(html_driver.page_source+'\n')
# #get we want content from pagesource
# def get_words_from_page_source():
#     html = etree.parse('pagesource.txt',etree.HTMLParser())
#     words = html.xpath('//text()')
#     words=is_ustr(words).split()
#     words=' '.join(words)
#     return words
# #just get pure words
# def is_uchar(uchar):
#     #jugde a unicode is Chiness
#     if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
#         return True
# def is_ustr(in_str):
#     out_str = ''
#     for i in range(len(in_str)):
#         if is_uchar(in_str[i]):
#             out_str=out_str+in_str[i]
#         else:
#             out_str=out_str+' '
#     return out_str
# def remove_duplicate_words(words):
#     w = words.split()
#     new_words = []
#     for i in w:
#         if i not in new_words:
#             new_words.append(i)
#     words = ' \n'.join(new_words)
#     return words
#
# h = get_all_urls('https://www.baidu.com/')
# pgs = get_all_page_source(h)
# html_driver.close()
# words = get_words_from_page_source()
# res = remove_duplicate_words(words)
# print(res)
#

