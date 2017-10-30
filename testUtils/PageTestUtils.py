#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'zhongyaqi'

import time

#睡眠
def sleep(seconds):
    time.sleep(seconds)

 #向上滑动屏幕
def swipe_to_up(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width / 2, height * 7 / 8, width / 2, height*1 / 8, 1000)

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

def assert_ok(self, loc, timeout=45, isOnly=False, context_index=None):
        bykey = loc[0]
        byvalue = loc[1]

        if context_index is None:
            self.driver.switch_to.context("NATIVE_APP")
        else:
            # if not context in self.driver.contexts:
            # raise AssertionError('无效的context:'+context)
            context = self.driver.contexts[context_index]
            self.driver.switch_to.context(context)
        if isOnly:
            end_time = time.time() + timeout
            while (True):
                if len(self.driver.find_elements(bykey, byvalue)) == 1:
                    break
                if (time.time() > end_time):
                    raise AssertionError('查找元素超时 => ' + str(bykey) + ':' + byvalue + ',timeout:' + str(timeout))
        else:
            self.driver.implicitly_wait(timeout)
            try:
                self.driver.find_element(bykey, byvalue)
            except:
                raise AssertionError('查找元素存在超时(imp) => ' + str(bykey) + ':' + byvalue + ',timeout:' + str(timeout))
            finally:
                self.driver.implicitly_wait(0.5)
                self.sleep(1)
        if not context_index is None:
            self.driver.switch_to.context("NATIVE_APP")
        return 1

def assert_no(self, loc, timeout=45, context_index=None):
        bykey = loc[0]
        byvalue = loc[1]

        if context_index is None:
            self.driver.switch_to.context("NATIVE_APP")
        else:
            context = self.driver.contexts[context_index]
            self.driver.switch_to.context(context)

        end_time = time.time() + timeout
        while (True):
            if not len(self.driver.find_elements(bykey, byvalue)):
                break
            if (time.time() > end_time):
                raise AssertionError('查找元素不存在超时 => ' + bykey + ':' + byvalue + ',timeout:' + str(timeout))
        if not context_index is None:
            self.driver.switch_to.context("NATIVE_APP")

