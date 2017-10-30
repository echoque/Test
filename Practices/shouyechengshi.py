# coding:utf-8
__author__ = 'zhongyaqi'

from multiprocessing import Pool
import os, time, random,json
import requests
def threadrequests_1():
    for i in range(0,1):
        url='http://apptest.58.com/api/log/api/info/citynew/1'
        r=requests.get(url)
        ob=r.json()

        if ob == None:
           print  u"获取城市 失败，返回数据为空"
        elif ob['infocode'] != '000000' :
           print u"获取城市 失败，解析数据失败"+"indfocode"+str(ob['infocode'])
        elif len(ob['result'][1])!=421:
            print u'第一个获取进程'+u'城市个数'+str(len(ob['result'][1]))
        else:
            print u"本次城市成功"+str(len(ob['result'][1]))+u"个城市"
        time.time()
        print time.time()

def threadrequests_2():
    for i in range(0,1):
        url='http://apptest.58.com/api/log/api/cache/update/city_cache/city_element?qq-pf-to=pcqq.discussion'
        r=requests.get(url)
        print u'第二个清除进程',i+1,r.status_code
        time.time()
        print time.time()


if __name__=='__main__':
    p = Pool()
    p.apply_async(threadrequests_1)
    p.apply_async(threadrequests_2)
    p.close()
    p.join()

    p = Pool()
    for i in range(50):
        p.apply_async(threadrequests_1())
        time.sleep(random.randint(1,5))

    for i in range(20):
        p.apply_async(threadrequests_2())
        time.sleep(random.randint(1,5))


    p.close()
    p.join()

