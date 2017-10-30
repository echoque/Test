#!/usr/bin/env python
#-*- coding=utf-8 -*

import requests,re
from bs4 import BeautifulSoup
#url="http://news.sina.com.cn/china/"
url='http://cmnt.sina.cn/index?product=comos&index=fymzqpq2357734&tj_ch=sports&is_clear=0'
res=requests.get(url)
res.encoding="utf-8"
html_sample=res.text
print html_sample

soup=BeautifulSoup(html_sample,"html.parser")
alink=soup.select("a")
title=soup.select('#title')
# for link in alink:
#     print(link['href'])
print(soup.select('.j_con_txt con_txt'))
print re.findall(r'<span class="j_con_txt con_txt">(\w+\d+)*?</span>', html_sample, re.S)
# print(alink)
# print(title)
# print(soup.title)
#print(header.name)
# print(soup.text)
#print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
 #s = re.findall(r'hash=(\w+)*', line, re.M)
# print re.findall('charset=(\w+\d+)*?', html_sample, re.M)
# title = re.search('<title>(.*?)</title>', html_sample, re.S).group(1)
#print 'title = ', title + '\n'

# 正则表达式
# reg=re.findall(r' <h2 class="hd_tit_l"> <a class="hd_tit_a" href=".*?" </a></h2>',html_sample, re.M)
# reg1=re.findall(r'<img src=".*?" class="img_width finpic" .*? ',html_sample, re.M)
# reg2=re.search(r'<h2 class="m_f_con_t cm_tit">".*?"</h2>',html_sample, re.M)
# reg3=re.findall(r'石泰峰:在新时代指导理论指引下奋勇前进',html_sample,re.M)
# print reg2


