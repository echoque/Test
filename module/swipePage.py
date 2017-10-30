#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'
import time
from testUtils.Driver import DesiredOptions


class swipePage(DesiredOptions):
 #向上滑动屏幕
 def swipe_to_up(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width / 2, height * 7 / 8, width / 2, height*3 / 8, 1000)

     #向下滑动屏幕
def swipe_to_down(self):
        width=self.driver.get_window_size()["width"]
        height=self.driver.get_window_size()['height']
        self.driver.wipe(width / 2, height * 1 / 8, width / 2, height*7 / 8, 1000)

    #向左滑动屏幕
def swipe_to_up(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width *7/ 8, height * 1 / 2, width *1/ 8, height*1 / 2, 1000)

    #向右滑动屏幕
def swipe_to_down(self):
        width=self.driver.get_window_size()["width"]
        height=self.driver.get_window_size()['height']
        self.driver.wipe(width *1/ 8, height * 1 / 2, width *7/ 8, height*1 / 2, 1000)

