#!/usr/bin/env python
# -*- coding: utf-8 -*
import time

def datetime():
        date= time.strftime("%Y%m%d%H%M%S", time.localtime())[0:12]
        return date

def grep_error(file,anr,crash):
        monkeyreport="D://monkey/monkeyReport.txt"
        #list=[]
        with open(monkeyreport,"w") as ff:
         try:
            list=[]
            lines=open(file,'r').readlines()
            lens=len(lines)-1
            for i in range(lens):
                if anr in lines[i]:
                    print "anr happened"
                    list.append("anr happened")
                    grep_log(file,typefile,start,end)
                elif crash in lines[i]:
                    print "crash happened"
                    list.append("crash happened")
            ff.write(datetime()+"monkey结果"+"\n")
            if list!= (None or []):
                ff.write(str(list))
            else:
              print "Success"
              ff.write("Success,no problem")

         except Exception,e:
             print e

def grep_log(file,typefile,start,end):
    print "grep log"
    monkeyreport="D://monkey/monkeyReport.txt"
    start_list=[]
    end_list=[]
    with open(file, 'r') as f:
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
            with open(file, 'r') as f:
                for i in f.readlines()[start_list[index]:end_list[index]+1]:
                    result.append(i)
                finally_str = string.join(result)
                print finally_str
                with open(monkeyreport,"w") as ff:
                  ff.write(finally_str)
                  print ff
            with open(typefile, 'ab+') as f:
                f.write(finally_str)

if __name__ == '__main__':
    file="D://Monkey/monekytest1.txt"
    # file="D://mimonkey0905.txt"
    crash="// NOT RESPONDING: com.wuba"
    anr="// CRASH: com.wuba"
    start="// NOT RESPONDING: com.wuba"
    end="//"
    typefile="anr" or "crash"
    grep_error(file,crash,anr)
    #grep_log(file,typefile,start,end)