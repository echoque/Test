#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
import time
import subprocess

# flies = os.listdir(r"D:\集成分支包\7.12.0\58client_v7.12.0_58585858_20170706_15.23_release.apk");
# for ff in flies:
#    print "adb install -r " + ff
#    text = os.popen("adb install -r app/" + ff)
#    time.sleep(2)
#    print text.read();


# p1 = subprocess.Popen('adb shell cd sdcard&&cd Android&&cd data&&ls |grep com', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print p1.stdout.read()

def test_install():
   p3 = subprocess.Popen('adb install C:\\Users\\zhongyaqi\\Desktop\\test.apk', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   time.sleep(20)
   print p3.stdout.read()

def test_uninstall():
   p2 = subprocess.Popen('adb uninstall com.wuba', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   print p2.stdout.read()

def adb():
    p1=subprocess.Popen("dir", shell=True)
    p1.wait()