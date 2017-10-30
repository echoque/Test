__author__ = 'zhongyaqi'
import os,time


def adbMonkey():
    print time.time()
    monkeylog="d://MONKEY/monekytest.txt"
    cmd="adb shell monkey -v -v -v  -p com.wuba --ignore-timeouts --ignore-crashes  --ignore-security-exceptions " \
        "--pct-syskeys 0 --throttle 200 500 >" +monkeylog
    os.system(cmd)

def getFileSize():
    adbMonkey()
    fileSize = os.path.getsize("d://MONKEY/monekytest.txt")
    return fileSize


if __name__ == '__main__':
 adbMonkey()
 getFileSize()


