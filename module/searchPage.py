#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'

from testUtils.Driver import DesiredOptions
from testUtils.Configuration import searchObject
import time

class searchPage(DesiredOptions):
 def search(self):
     #self.driver.find_element_by_android_uiautomator('text("通讯录")').click()
     self.driver.find_element_by_accessibility_id("搜索").click()
     #self.driver.find_element_by_android_uiautomator('text("搜索")').send_keys(u"仲筱琦")
     self.driver.find_element_by_android_uiautomator('text("搜索")').send_keys(searchObject)
     #self.driver.find_element_by_android_uiautomator('text("仲筱琦")').click()
     #self.driver.find_element_by_xpath("//android.widget.TextView[@text='仲筱琦']").click()
     time.sleep(6)
     self.driver.find_element_by_accessibility_id("com.tencent.mm:id/jc").click()


