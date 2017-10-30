#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time,os,sys
import threading,getFileSize,writeTime
from MonkeyTest import stopMonkey1
from MonkeyTest import writeTime
from basePage import basePage

class monkeyPage(basePage):
    #执行monkey并写入本地时间
    def test_monkey(self):
        basePage.adbMonkey(self)

    def fun_timer(self):
        basePage.fun_timer(self)

     #每15分钟写入一次时间
     #判断当前时间和预期时间,n是预期时间（单位是小时）。将写入文件的行数和60n/15=4n对比
    # def compareTime(self,n):
    #      basePage.count_lines()
    #      while lines < 4n+1
    #        writeTime.fun_timer()
    #        adbMonkey()
    #     else:
    #       count_lines
if __name__ == '__main__':

    # cmd_commands = []
    # for c in cmd_commands:
    #   os.popen(i)
    m=monkeyPage()
    # m.test_monkey()
    # m.fun_timer()


    # filename = "d://monkey/timelog.txt"
    # myfile = open(filename)
    # lines = len(myfile.readlines())
    # print lines
    # if lines <6:
    #     print "countinue monkey"
    # else:
    #     m.stop_monkey()

    m.stopMonkey()




