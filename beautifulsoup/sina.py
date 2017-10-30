#!/usr/bin/python
# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

#url="http://baidu.com"
# url='http://news.sina.com.cn/china/'
url='http://news.sina.com.cn/c/2017-10-22/doc-ifymzksi0974429.shtml'
res=requests.get(url)
res.encoding='utf-8'
htmlsample=res.text
print type(htmlsample)
soup=BeautifulSoup(htmlsample,"html.parser")
#print(soup.text)
#print(soup.select('.link'))
# alinks=soup.select('a')
# for link in alinks:
#     print(link)
#     print(link['href'])
# print(soup.select('.news-item '))

#取得详情页单条新闻的信息,包括标题、时间及来源(若存在两个相同的标签，使用contents可将此拆成一个list的两个元素)
# print(soup.select('#artibodyTitle')[0].text)
#print(soup.select('.time-source')[0].contents[0].strip())
# print(soup.select('.time-source span a')[0].text)
#print(soup.select('.time-source')[0].contents[1].text)

#获取详情页单条新闻的信息，包括正文、编辑
print(soup.select('#artibody')[0].text)
#for p in soup.select('#artibody p')[-1]:





#取得首页各条新闻的时间、标题及链接
# for news in soup.select('.news-item'):
#     # print news
#     # print news.select('h2')
#
#     if len(news.select('h2'))>0:
#        link= news.select('a') [0]['href']
#        target=news.select('h2')[0].text
#        time=news.select('.time')[0].text
#        print(time,target,link)






