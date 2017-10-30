#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import re,json,requests,time


class getInfo():

 #解析URL
    def test_Parse():
      payload={"yoyo":"hello", "python":'8888888'}
     #转换成json格式
      data_json=json.dumps(payload)
      r=requests.post("https://app.58.com/api/list/banjia?v=1&tabkey=map&circleLon=116.511036&action=getMapInfo%2CgetFilterInfo&curVer=7.12.2&appId=1&localName=bj&circleLat=39.993337&format=json&os=android&maptype=2&qq-pf-to=pcqq.c2c",data=data_json)
      print(r.text)

      # url="https://app.58.com/api/list/banjia?v=1&tabkey=map&circleLon=116.511036&action=getMapInfo%2CgetFilterInfo&curVer=7.12.2&appId=1&localName=bj&circleLat=39.993337&format=json&os=android&maptype=2&qq-pf-to=pcqq.c2c"
      # urllib.request.urlretrieve(r.text,r"d://oppoz")

    if __name__ == '__main__':
      test_Parse()
      # grepField('baidu.txt')