#coding=utf-8
# __author__ = 'zhongyaqi'

'''
Create on 2015-1-7
python 2.7 for window
@auther: tangdongchu
'''
import os
import sys
import time
import re
import datetime

class monkeyTest():

    def __init__(self):
        """ init """

    #monkey命令，packageName包名，interval间隔时间单位ms ，frequency执行次数
    def monkeyApp(self,packageName,interval,frequency):
        try:
            os.popen("adb shell monkey -p %s --throttle %s --ignore-crashes --ignore-timeouts --ignore-security-exceptions --ignore-native-crashes --monitor-native-crashes -v -v -v %s >e:\monkeylog\monkeyScreenLog.log" % (packageName, interval, frequency),'r')
        except Exception,e:
            print e

    #获取当前电量
    def getCurrentBattery(self):
        try:
            for Battery in os.popen('adb shell dumpsys battery','r').readlines():
                reList = re.sub('Battery:','',Battery)
                reList = reList.replace('\n','')
                result = re.search('level', reList)
                if result != None :
                    List = reList.split()
                    level=List.pop()#删除第i个元素，并返回这个元素。若调用pop()则删除最后一个元素
                    #print "battery level " + level + "%"
                    return level
                    break
        except Exception,e:
            print e

    #获取当前时间，用于计算应用运行时间
    def getCurrentTime(self):
        try:
            currentTime = datetime.datetime.now()
            return currentTime
        except Exception,e:
            print e

def main():
    print """"""


if __name__=="__main__":

    packageName = 'com.wuba'
    myApp = monkeyTest()
    level = int(myApp.getCurrentBattery())
    runtime = myApp.getCurrentTime()
    myApp.monkeyApp(packageName,500,2500) #0.5秒点一次，运行2500次
    #判断是否执行完成，执行完成后统计耗电量
    for i in range(1, 1000000):
        monkeylog = open('E:\monkeylog\monkeyScreenLog.log')
        try:
            temp = monkeylog.read( )
        finally:
            monkeylog.close( )
        if temp.count('Monkey finished')>0:
            level = int(myApp.getCurrentBattery())-level
            runtime = myApp.getCurrentTime()-runtime
            break
        else:
            time.sleep(2)
    print "run time " + str(runtime)
    print "use battery" + str(level) + "%"