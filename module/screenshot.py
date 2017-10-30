#!/usr/bin/env python
# -*- coding: utf-8 -*

import pyscreenshot as ImageGrab
from testUtils.Driver import DesiredOptions


# class screenshotPage(DesiredOptions):
#     def screenshot(self):
#         #fullscreen
#         im=ImageGrab.grab()
#         im.show()
#
#         # part of the screen
#         im=ImageGrab.grab(bbox=(10,10,510,510)) # X1,Y1,X2,Y2
#         im.show()



        #通过if进行断言判断
# 20 driver.get("https://baidu.com/")
# 21 #新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
# 22 pic_path = '.\\result\\image\\' + current_time1+'\\' + current_time +'.png'
# 23 print(pic_path)
# 24 time.sleep(5)
# 25 print(driver.title)
# 26 #截取当前url页面的图片，并将截取的图片保存在指定的路劲下面（pic_path），注：一下两种方法都可以
# 27 driver.save_screenshot(pic_path)
# 28 driver.save_screenshot('.\\result\\image\\' + current_time1+'\\' + current_time +'.png')