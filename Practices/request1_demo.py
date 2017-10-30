# coding:utf-8
# __author__ = 'zhongyaqi'

import sys,requests


def request():
    t=requests.get('https://www.baidu.com',allow_redirects=False)
    print t.status_code
    # print t.json()
    index= t.content
    print index
    # write(index)


# def write(index):
#     with open('C:\\Users\\zhongyaqi\\Desktop\\testSX10.txt',"ab") as a:
#       a.write(index)
#     print "写入成功"





if __name__=="__main__":
        request()
        # write()
