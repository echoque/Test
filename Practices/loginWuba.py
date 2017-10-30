#!/usr/bin/env python
# -*- coding: utf-8 -*

from appium import webdriver
import time
time.sleep(12)



def test_login(self):
        self.driver.find_element_by_android_uiautomator('text("我的")').click()
        # 登录状态会有用户名或商家版（商家账号），判断是否有头像上方用户名或商家版(商家账号)，如果有则发布，如果没有则登录
        # if self.driver.find_elements_by_id('com.wuba:id/mycenter_switch_view'):
        if self.driver.find_elements_by_id('com.wuba:id/mycenter_head_name'):
            self.test_publish()
        else:
            self.test_login()
            self.test_publish()
        a=self.driver.find_elements_by_id('com.wuba:id/home_tab_title')[4]
        a.click()
        time.sleep(3)
        self.driver.find_element_by_id('com.wuba:id/mycenter_head_image').click()
        self.driver.find_element_by_id('com.wuba:id/login_username').send_keys('58qq80')
        self.driver.find_element_by_id('com.wuba:id/login_password').send_keys('123321')
        self.driver.find_element_by_android_uiautomator('text("登录")').click()
