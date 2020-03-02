#导入包
from appium import webdriver
import os,time
class Driver(object):

    def startUp(self):
        print('启动中')
#设置启动参数
        desired_caps = {
            "deviceName": "127.0.0.1:21503",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": True,
            "unicodeKeyboard": True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        return self.driver

    print('已经启动,等待...')
    time.sleep(10)

if __name__=='__main__':
    d = Driver()
    d.startUp()
