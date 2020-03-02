
#coding:utf-8

import os

from common.Driver import Driver

from common import readConfig

import time

import logging





# class Operation():

class Operation(object):



    '''1.2018年8月22日：封装滑动公共操作方法：上滑，下滑，左滑、右滑

       2.2018年8月23日：封装截图公共操作方法

    '''



    def __init__(self,driver):

        # print('--Base-__init')

        self.driver = driver



    #参数：t--滑动时间

    def swipeUp(self,t=500):

        l = self.driver.get_window_size()

        print('上滑页面')

        x1 = l['width'] * 0.5

        y1 = l['height'] * 0.65

        y2 = l['height'] * 0.25

        # print(x1, y1, y2)

        time.sleep(1)

        return  self.driver.swipe(x1, y1, x1, y2, t)



    def swipeDown(self,t=500):

        l = self.driver.get_window_size()

        print('下滑页面')

        x1 = l['width'] * 0.5

        y1 = l['height'] * 0.25

        y2 = l['height'] * 0.75

        # print(x1,y1,y2)

        time.sleep(1)

        return  self.driver.swipe(x1, y1, x1, y2, t)



    def swipeRight(self,t=500):

        l = self.driver.get_window_size()

        print('右滑页面')

        x1 = l['width'] * 0.05

        y1 = l['height'] * 0.5

        x2 = l['width'] * 0.75

        # print(x1, y1, x2)

        time.sleep(1)

        return  self.driver.swipe(x1, y1, x2, y1, t)



    def swipeLeft(self,t=500):

        l = self.driver.get_window_size()

        print('左滑页面')

        x1 = l['width'] * 0.75

        y1 = l['height'] * 0.5

        x2 = l['width'] * 0.05

        # print(x1, y1, x2)

        time.sleep(1)

        return  self.driver.swipe(x1, y1, x2, y1, t)







if __name__ == '__main__':
    d=Driver()
    driver = d.startUp()

    p = Operation(driver)

    p.swipeDown(100)
