#coding:utf-8
__author__ = 'zhongyaqi'
from multiprocessing import Pool
import requests,time,os,random


def threadrequests_1():
    for i in range(0,1):
        url='http://apptest.58.com/api/log/api/info/citynew/1'
        r=requests.get(url)
        ob=r.json()
        # ob='d:\\获取城市列表.txt'
        if ob == None:
            print u"获取城市 失败，返回数据为空"
        elif ob["infocode"]!='000000':
            print u"获取城市 失败，解析数据失败"
        elif len(ob["result"][1])!=421:
            print u"获取城市个数"+str(len(ob['result'][1]))

def threadrequests_2():
    for i in range(0,1):
        url='http://apptest.58.com/api/log/api/cache/update/city_cache/city_element?qq-pf-to=pcqq.discussion'
        r=requests.get(url)
        print u'第二个清除进程',i+1,r.status_code
        #time.time()
        #print time.time()




if __name__=="__main__":
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