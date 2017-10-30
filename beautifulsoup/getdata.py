#!/usr/bin/env python
#-*- coding=utf-8 -*
import urllib2
import urllib
import urllib3

url='http://python.jobbole.com/81336/'
request=urllib2.Request(url)
response=urllib2.urlopen(request)
#print response.read()

# value={"name":"zhongyaqi","password":"zhong"}
# data=urllib.urlencode(value)
# geturl=url+"?"+data
# request=urllib2.Request(geturl)
# response=urllib2.urlopen(request)
# print geturl

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
value={"name":"zhongyaqi","password":"zhong"}
data=urllib.urlencode(value)
headers={"user_agent":user_agent}
request=urllib2.Request(url,data,value)
response=urllib2.urlopen(request)
print response.read()
