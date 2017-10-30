#!/usr/bin/python
# coding:utf-8

import time,os
import threading
class basePage():

    def grep_error(self,file,sstr):
         try:
            lines=open(file,'r').readlines()
            flen=len(lines)-1
            for i in range(flen):
                if sstr in lines[i]:
                    print "anr or crash"

            open(file,'w').writelines(lines)
         except Exception,e:
             print e




    def datetime(self):
        date= time.strftime("%Y%m%d%H%M%S", time.localtime())
        return date


    def adbMonkey(self):
        print "start adb monkey"
        monkeylog="d://monkey/monekytest"+self.datetime()+".txt"
        cmd="adb shell monkey -v -v -v  -p com.wuba --ignore-timeouts --ignore-crashes  --ignore-security-exceptions " \
            "--pct-syskeys 0 --throttle 200 10000000 >" +monkeylog
        os.system(cmd)
        #self.fun_timer()
    #每分钟写入一次文件,并统计一次文件行数，根据行数与4n+1q
    def fun_timer(self):
        print('Hello Timer!')
        self.write_time()
        self.count_lines()
        global timer
        timer = threading.Timer(60,self.fun_timer)
        timer.start()

    def write_time(self):
     with open('d://monkey/timelog.txt','a') as f:
        date= time.strftime("%Y%m%d%H%M%S", time.localtime())
        starttime=date[8:10]+":"+date[10:12]
        print "start write time"
        #f.truncate()
        f.write(starttime+"\n")

    #统计行数，经计算realines加上2是实际的行数
    def count_lines(self):
        filename = "d://monkey/timelog.txt"
        myfile = open(filename)
        lines = len(myfile.readlines())
        #print "There are %d lines in %s" % (lines, filename)
        print "start count lines"
        print lines
        return  lines

    def grepPid(self):
        log="d://Monkey/monkeyPid.txt"
        cmd="adb shell ps | findstr monkey>"+log
        os.system(cmd)
        #shell   7772  185  277516 22244 ffffffff 4010a58c S com.Android.commands.monkey kill
        fo = open(log, "r+")
        fo.seek(10,16)
        pid=fo.read(5)
        fo.close()
        return pid


    def stopMonkey(self):
         self.grepPid()
         os.system("adb shell kill "+self.grepPid()+"")
         print "stop adb monkey"
         # global timer
         # timer.cancel()

if __name__ == '__main__':

    m=basePage()
    file='D://mimonkey0905.txt'
    sstr="// CRASH:"
    m.grep_error(file,sstr)
    m.adbMonkey()
    #m.test_monkey()
    #m.fun_timer()
    #m.adbMonkey()
    #m.stopMonkey()



