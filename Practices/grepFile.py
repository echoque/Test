#!/usr/bin/env python
# -*- coding: utf-8 -*


def grep_error(filename,typefile,start,end):
    """过滤出错误日志并保存"""
    start_list=[]
    end_list=[]
    with open(filename, 'r') as f:
        line = f.readlines()
        print len(line)
        for index in  range(1,len(line)):
            if line[index].startswith(start):
               start_list.append(index)
            if line[index].startswith(end):
               end_list.append(index)

        for index in range(len(start_list)) :
            result = []
            string = ''
            with open(filename, 'r') as f:
                for i in f.readlines()[start_list[index]:end_list[index]+1]:
                    result.append(i)
                finally_str = string.join(result)
            with open(typefile, 'ab+') as f:
                f.write(finally_str)

def Main(info):
    with open(info, 'r') as f:
            result=f.read()
            if ('08-07 14:45:00.000 ' and '08-07 15:16:59.561') in result:
                grep_error(info,'0807alarm3.txt','08-07 14:45:00.000 ','08-07 15:16:59.561')


if __name__ == '__main__':
    Main('20170807alarm3.txt')
