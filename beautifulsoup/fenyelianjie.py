#!/usr/bin/python
# -*- encoding:utf-8 -*-
import requests,json
import commonmethod
from bs4 import BeautifulSoup

def req(url):
    res=requests.get(url)
    res.encoding='utf-8'
    resdic=res.text.lstrip('  newsloadercallback(').rsplit(');')
    result=json.loads(resdic[0])
    #reg=re.findall(r'url ',result, re.M)
    #print result['result']['data']
    newsdetail=[]
    for en in result['result']['data']:
        newsdetail.append(getNewsDetail(en['url']))
    return newsdetail

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

# def func(obj):
#     urllist=[]
#     if  isinstance(obj,dict):
#        for key in obj:
#            print key
#            print obj[key]
#            if key == 'url'and isinstance(obj[key],str):
#                urllist.append(obj[key])
#            else:
#                 func(obj[key])
#     elif isinstance(obj,list or tuple):
#         for a in obj:
#             func(a)
#     print urllist

if __name__ == '__main__':
    # obj = {
    #         'url': 'www.baidu.com'
    # }
    #
    # func(obj)
    url='http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&\
    level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=2&callback=newsloadercallback&_=1508908695130'
    req(url)








