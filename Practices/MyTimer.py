__author__ = 'zhongyaqi'
import time as t

class MyTimer():
    #��ʱ��ʼ
    def start(self):
        self.start=t.localtime()
        print("��ʱ��ʼ")

    #��ʱ����
    def stop(self):
        self.start=t.localtime()
        print("��ʱ����")

        
