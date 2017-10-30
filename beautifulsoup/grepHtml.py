#!/usr/bin/env python
#-*- coding=utf-8 -*

from bs4 import BeautifulSoup

html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""
soup=BeautifulSoup(html_doc, "html.parser")
soup1=BeautifulSoup(open("C:\Users\zhongyaqi\Desktop\TEST.html"), "html.parser")
# print (soup1.title)
# print (soup1.getText)
print (soup1.prettify())


# print (soup.head)
# print (soup.title.name)
#print (soup.p)
#print (soup.find_all('a'))
# print (soup.find(id="link1"))
#
# for link in soup.find_all("a"):
#     print link.get("href")
#
# print soup.getText()
# for tag in soup.find_all(True):
#     print tag.name