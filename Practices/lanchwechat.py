# coding:utf-8
"""
Created on 15/10/8
@author: Guocg
测试点：

"""
#from WubaTestUtils.Andr_Config_Params import udid
from appium import webdriver
import time
import unittest


class DesiredOptions(unittest.TestCase):
    def test_setUp(self):

        desired_capas={}
        desired_capas['deviceName']='123'
        desired_capas['platformName']='Android'
        desired_capas['platformVersion']='5.1.1'
        desired_capas['appPackage']='com.tencent.mm'
        desired_capas['appActivity']='com.tencent.mm.ui.LauncherUI'
        desired_capas['unicodeKeyboard']= False
        #使用 Unicode 输入法。默认值false
        desired_capas['resetKeyboard']=False
        #在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值 false
        self.driver=webdriver.Remote( 'http://127.0.0.1:4723/wd/hub',desired_capas)


    def tearDown(self):
        self.driver.quit()

    def test_demo(self):
        # self.logger.step(1, '启动微信app')
        time.sleep(5)
        # self.logger.step(2,'启动微信APP->点击好友仲筱琦')
        self.driver.find_element_by_android_uiautomator('text("仲筱琦")').click()
        # self.logger.step(3,'启动微信APP->点击好友仲筱琦->点击表情')
        # b=self.driver.find_element_by_android_uiautomator('id("com.tencent.mm:id/a4a")')
        # b.click()
        # self.driver.find_element(MobileBy.ID, 'com.tencent.mm:id/a4a').click()
        # self.driver.find_element_by_id(self,'com.tencent.mm:id/a4a').click()
        # c=self.driver.find_element_by_android_uiautomator('content-desc("[微笑]")')
        # c.click()
        # self.logger.step(4,'启动微信APP->点击好友仲筱琦->点击表情->选择微笑并发送')
        # self.driver.find_element_by_accessibility_id("[微笑]").click()
        # self.driver.find_element_by_android_uiautomator('text("发送")').click()



# if __name__=="__main__":
#     unittest.main()