#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'
import time
from testUtils.Driver import DesiredOptions
# from module.screenshot import screenshotPage
from selenium import webdriver
import time,unittest
from selenium.webdriver.support import expected_conditions as EC
from testUtils.Configuration import path

class loginPage(DesiredOptions):
 def login(self):
        # time.sleep(3)
        # #self.driver.find_element_by_android_uiautomator('text("登录")').click()
        # # self.driver.find_element_by_android_uiautomator('text("使用其他方式登录")').click()
        # #self.driver.find_element_by_id('com.tencent.mm:id/bga').click()
        try:
               login=self.driver.find_elements_by_id("com.tencent.mm:id/h1")
               login[0].send_keys("1019176312")
               login[1].send_keys("yaqi19920612zhong")
               self.driver.find_element_by_android_uiautomator('text("登录")').click()
                #　判断登录成功页面是否有账号："zhongxiaye1992"
               time.sleep(10)
               self.driver.find_element_by_android_uiautomator('text("我")').click()
               locator = ("id", "com.tencent.mm:id/bxz")
               result = EC.text_to_be_present_in_element(locator,u"微信号：zhongxiaye1992")(self.driver)
               self.driver.get_screenshot_as_png(path)
               self.assertFalse(result)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            # 图片名称可以加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
            raise
        time.sleep(8)
        print 'pass'
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        self.driver.get_screenshot_as_file('%s.jpg' % nowTime)

       # try:
       #      self.driver.find_element_by_id("input1").send_keys(u"上海-悠悠")
       #      self.driver.find_element_by_id("input2").send_keys("xxx")
       #      # 登录id是错的，定位会抛异常
       #      self.driver.find_element_by_id("signin").click()
       #      #　判断登录成功页面是否有账号："上海-悠悠"
       #      time.sleep(3)
       #      locator = ("id", "lnk_current_user")
       #      result = EC.text_to_be_present_in_element(locator,u"上海-悠悠")(self.driver)
       #      self.assertFalse(result)
       # except Exception as msg:
       #      print(u"异常原因%s"%msg)
       #      # 图片名称可以加个时间戳
       #      nowTime = time.strftime("%Y%m%d.%H.%M.%S")
       #      self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
       #      raise
