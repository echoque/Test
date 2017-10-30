#coding=utf-8
import os,math,time
max_data=str(int(math.pow(100,4)))

def datetime():
        date= time.strftime("%Y%m%d%H%M%S", time.localtime())[0:12]
        return date

def Start_Monkey():
    print "start monkey"
    monkeylog="d://monkey/monekylog"+datetime()+".txt"
    cmd = "adb shell monkey -v -v -v  -p com.wuba --ignore-timeouts --ignore-crashes  --ignore-security-exceptions " \
              "--pct-syskeys 0 --throttle 200  "+max_data+" >" + monkeylog
    print cmd
    print monkeylog
    os.system(cmd)

if __name__ == '__main__':
    datetime()

