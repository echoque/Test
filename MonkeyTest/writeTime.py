__author__ = 'zhongyaqi'
#qc test code
import time
import threading


def write_time():
     with open('d://timelog.txt','a') as f:
        date= time.strftime("%Y%m%d%H%M%S", time.localtime())
        starttime=date[8:10]+":"+date[10:12]
        starttime
        print starttime
        f.write(starttime+"\n")



def fun_timer():
    print('Hello Timer!')
    write_time()
    global timer
    timer = threading.Timer(60, fun_timer)
    timer.start()


if __name__ == '__main__':
    fun_timer()
