__author__ = 'zhongyaqi'
import time as t

class MyTimer():
    #计时开始
    def start(self):
        self.start=t.localtime()
        print("计时开始")

    #计时结束
    def stop(self):
        self.start=t.localtime()
        print("计时结束")

        
