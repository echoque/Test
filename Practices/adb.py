#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'
import os,sys

def adbTest():
 os.system("adb pull /data/anr/traces.txt >d://121.txt")


def adbClear():
 os.system("adb shell pm clear com.wuba")

def adbMonkey():
 os.system("adb shell monkey -v -p com.wuba --ignore-timeouts --ignore-crashes --throttle 100 10000")

def adbServer():
 os.system("adb shell services list")

def adbProcess():
 os.system("adb shell ps | findstr wuba >d://")

if __name__ == '__main__':
    adbTest()
    adbClear()
    adbMonkey()

