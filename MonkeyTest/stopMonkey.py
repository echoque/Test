__author__ = 'zhongyaqi'
import  os
import threading



def grepPid():

    log="d://Monkey/monkeyPid.txt"
    cmd="adb shell ps | findstr monkey>"+log
    os.system(cmd)
    #shell   7772  185  277516 22244 ffffffff 4010a58c S com.Android.commands.monkey kill
    fo = open(log, "r+")
    fo.seek(10,16)
    pid=fo.read(5)
    fo.close()
    print pid
    #return pid

def stopMonkey():
     grepPid()
     os.system("adb shell kill "+grepPid()+"")

     timer.cancel()


def fun_timer():
    print('Hello Timer!')
    global timer
    timer = threading.Timer(3, fun_timer)
    timer.start()
    timer.cancel()

if __name__ == '__main__':
 stopMonkey()
