#!/usr/bin/python
# -*- encoding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

def getNewsDetail(newsurl):
    result={}
    res=requests.get(newsurl)
    # print res.content
    res.encoding='utf-8'
    soup=BeautifulSoup(res.content,'html.parser')
    result['title']=soup.select('#artibodyTitle')[0].text
    result['body']=soup.select('#artibody')[0].text
    result['time']=soup.select('.time-source')[0].contents[0].strip()
    result['source']=soup.select('.time-source span a')[0].text
    print result

if __name__ == '__main__':
 newurl='http://news.sina.com.cn/o/2017-10-24/doc-ifymyyxw4478787.shtml'
 getNewsDetail(newurl)
