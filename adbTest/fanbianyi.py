#!/usr/bin/env python
#-*- coding=utf-8 -*
import os
def fanbiyi():
# 再进入apktool      cd  /apktool
# 输入以下命令：apktool.bat d -f  test.apk
 apk="D://apktool/58client_v7.13.5_1015_20170906_10.52_release.apk"
 os.system(" cd d："|" cd /apktool" | "apktool.bat d -f "+apk )

def check_permission():
 apkPath=""
 permission="D://ADB/permission.txt"
 os.system("aapt dump badging "+apkPath > permission.txt)

def sign_name():
    os.system("cd C:\Users\用户名\.android")
    os.system("keytool -list -v -keystore debug.keystore")

def battery():
    os.system("adb shell logcat -v time")


if __name__ == '__main__':
    file="D://Monkey/monekytest1.txt"
