__author__ = 'zhongyaqi'
import re
m=re.search("[A-Z]","sdfabbbbaA,Bbcd")
print m
name="Hello,My name is kuangl,nice to meet you..."
k=re.search(r'k(uan)gl',name)
if k:
        print k.group(0),k.group(1)
else:
        print"Sorry,not search!"