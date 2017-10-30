#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'

from appium import webdriver
import time
import unittest
import testUtils
import module
from module import loginPage
from testUtils.Driver import DesiredOptions
from testUtils.Configuration import NAME,message
# from module.screenshot import screenshotPage

class IMPage(DesiredOptions):
    #IM文字
    def sendMessage(self):
        for name in NAME:
         print name
         self.driver.find_element_by_android_uiautomator(name).click()
         self.driver.find_element_by_id('com.tencent.mm:id/a4n').send_keys(message)
         self.driver.find_element_by_android_uiautomator('text("发送")').click()
         #screenshotPage()
         self.driver.find_element_by_id('android:id/text1').click()

     #相册
    def sendPicture(self):
        self.driver.find_element_by_android_uiautomator('text("相册")').click()
        self.driver.find_element_by_id('com.tencent.mm:id/b8j').click()
        self.driver.find_element_by_android_uiautomator('text("发送(1/9)")').click()
     #拍摄
    def sendTakepicture(self):
      self.driver.find_element_by_android_uiautomator('text("拍摄")').click()
     #视频聊天
    def sendVideo(self):
        self.driver.find_element_by_id('com.tencent.mm:id/a4s').click()
        self.driver.find_element_by_android_uiautomator('text("视频聊天")').click()
        self.driver.find_element_by_android_uiautomator('text("视频聊天")').click()
        self.driver.find_element_by_android_uiautomator('text("允许")').click()
        self.driver.find_element_by_android_uiautomator('text("允许")').click()
    #位置
    #self.driver.find_element_by_android_uiautomator('text("位置")').click()

