#coding=utf-8
import os

def Stop_Monkey():
    # 停止monkey任务
    cmd = "adb shell ps | findstr monkey"
    result=os.popen(cmd)
    pid=result.readline().split(" ")[5]
    os.system("adb shell kill "+pid+"")
if __name__ == '__main__':
    Stop_Monkey()
