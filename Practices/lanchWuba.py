#!/usr/bin/env python
# -*- coding: utf-8 -*

from appium import webdriver
from module.swipePage import swipe_to_up
from module.publish import test_publish
import time
import unittest
import sys
from module.install import test_install
from module.install import test_uninstall
import module

reload(sys)
sys.setdefaultencoding('utf-8')



class DesiredOptions(unittest.TestCase):
    # def setUpClass(cls):
    test_uninstall()
    test_install()
    def setUp(self):
        try:
            desired_capas={}
            desired_capas['deviceName']='123'
            desired_capas['platformName']='Android'
            desired_capas['platformVersion']='6.0.1'
            desired_capas['appPackage']='com.wuba'
            desired_capas['appActivity']='com.wuba.activity.launch.LaunchActivity'
            desired_capas['unicodeKeyboard']= True
            desired_capas['resetKeyboard']=True
            desired_capas['noReset']=True
            self.driver=webdriver.Remote( 'http://127.0.0.1:4723/wd/hub',desired_capas)

        except Exception as e:
            print 'setUp failed, %s' % (str(e))
            raise

    def test_demo(self):
        #登录前判断是否已经处于登录状态
        time.sleep(12)
        test_install()
        self.driver.find_element_by_android_uiautomator('text("我的")').click()
        # 已登录状态会有用户名或商家版（商家账号），判断是否有头像上方用户名或商家版(商家账号)，如果有则发布，如果没有则登录
        # if self.driver.find_elements_by_id('com.wuba:id/mycenter_switch_view'):
        if self.driver.find_elements_by_id('com.wuba:id/mycenter_head_name'):
            self.test_publish()
        else:
            self.test_login()
            self.test_publish()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
