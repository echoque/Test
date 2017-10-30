#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'

from appium import webdriver
import time
import unittest


class DesiredOptions(unittest.TestCase):
        #首先判断登录状态(首次启动APP初始化状态；已登录过账号输入状态)
        #登录状态的话，搜索联系人，若在第一屏直接发消息，若不在第一屏则滑动屏幕；未登录则登录

        #首次启动APP，需要处理权限问题，有三个弹框需要处理
    def setUp(self):
        try:
            desired_capas={}
            desired_capas['deviceName']='123'
            desired_capas['platformName']='Android'
            desired_capas['platformVersion']='6.0.1'
            desired_capas['appPackage']='com.tencent.mm'
            desired_capas['appActivity']='com.tencent.mm.ui.LauncherUI'
            desired_capas['unicodeKeyboard']= True
            desired_capas['resetKeyboard']=True
            desired_capas['noReset']=True
            self.driver=webdriver.Remote( 'http://127.0.0.1:4723/wd/hub',desired_capas)

        except Exception as e:
            print 'setUp failed, %s' % (str(e))
            raise

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
