#!/usr/bin/env python
# -*- coding: utf-8 -*
from appium import webdriver
import time
def publish(self):
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator('text("发布")').click()
        #发布二手车
        self.driver.find_element_by_android_uiautomator('text("汽车/自行车")').click()
        self.driver.find_element_by_accessibility_id("拼车/顺风车").click()
        self.driver.find_element_by_accessibility_id("我是车主").click()

        #输入起点和终点
        self.driver.find_element_by_id('Startstation').send_keys(u'北京')
        self.driver.find_element_by_id('EndStation').send_keys(u'濮阳')

       #屏幕滑动
        self.swipe_to_up()

        self.driver.find_element_by_id("shengyuzuowei").send_keys('4')
        self.driver.find_element_by_id('Content').send_keys('fsfsdfsdfsdfdsfdsf')
        self.driver.find_element_by_id('goblianxiren').send_keys('gaoxing')
        self.driver.find_element_by_id('Phone').clear()
        self.driver.find_element_by_id('Phone').send_keys('18900920039')
        self.driver.find_element_by_accessibility_id('开通店铺并发布信息').click()