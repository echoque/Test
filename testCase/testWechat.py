#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'

from appium import webdriver
import time
from module.loginPage import loginPage
from module.IMPage import IMPage
from module.searchPage import searchPage
from module.swipePage import swipePage
from testUtils.Driver import DesiredOptions
#from module.screenshot import screenshotPage


class test_im (loginPage,IMPage,searchPage,swipePage):
        #首先判断登录状态(首次启动APP初始化状态；已登录过账号输入状态)
        #登录状态的话，搜索联系人，若在第一屏直接发消息，若不在第一屏则滑动屏幕；未登录则登录

        #首次启动APP，需要处理权限问题，有三个弹框需要处理

    def test_wechat(self):
        time.sleep(3)

        #保留登录账号状态，此时有账号上方有头像元素
        if self.driver.find_elements_by_id("com.tencent.mm:id/bfp"):
            self.driver.find_element_by_android_uiautomator('text("更多")').click()
            self.driver.find_element_by_android_uiautomator('text("切换帐号")').click()
            self.driver.find_element_by_android_uiautomator('text("使用其他方式登录")').click()
            loginPage.login(self)
        else:
              if self.driver.find_elements_by_android_uiautomator('text("登录")'):
                 time.sleep(3)
                 self.driver.find_element_by_android_uiautomator('text("登录")').click()
                 # self.driver.find_element_by_android_uiautomator('text("使用其他方式登录")').click()
                 self.driver.find_element_by_id('com.tencent.mm:id/bga').click()
                 loginPage.login(self)
              else:
                time.sleep(6)
                searchPage.search(self)
                #swipePage.swipe_to_up(self)
                #if self.driver.find_element_by_android_uiautomator('text("仲筱琦")'):
                IMPage.sendMessage(self)




