#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'
import os,sys,time

def datetime():
 date= time.strftime("%Y%m%d%H%M%S", time.localtime())
 date1= date[-6:-2]
 hour=date[-6:-4]
 minite=date[-4:-2]

 print hour
 print minite
 return date1
 f=open('timelog.txt','w')
 f.write("hour"+hour,"minite"+minite)
 f.close()
 f.readline()

def adbDevice():
 os.system("adb devices")

def adbUninstall():
 os.system("adb uninstall com.wuba")

def adbInstall():
 os.system("adb install com.wuba")

def adbTest():

 os.system("adb pull /data/anr/traces.txt >d://pull"+datetime()+".txt")

def adbClear():
 os.system("adb shell pm clear com.wuba")

def adbServer():
 os.system("adb shell services list >d://pull"+datetime()+".txt")

def adbProcess():
 os.system("adb shell ps | findstr wuba >d://")

def adbMonkey():
 print time.time()
 filename="d://monekytest"+datetime()+".txt"
 filename2="d://monekytime.txt"
 os.system("adb shell monkey -v -v -v  -p com.wuba --ignore-timeouts --ignore-crashes  --ignore-security-exceptions --pct-syskeys 0 --throttle 200 300 >" +filename)
 print time.time()
 return  filename
 # if endtime - starttime < hour:
 #     adbMonkey()
 # else:
 #     print finished
# year = endtime -starttime
# years = 8
# bj = 10000
# rate = 0.05
# f = open("d://monekytime.txt", 'w+')
# while year < years:
#     adbMonkey()
#     print >> f, "endtime"(endtime),"starttime" (starttime)
#     year += 1




def readFile():
    with open(adbMonkey(), 'r') as f:
        line = f.readlines()
        return line


def searchFile():
    print adbMonkey().readlines()

if __name__ == '__main__':
    datetime()
    # adbMonkey()
    # readFile()
    # print time.time()
    # datetime()


