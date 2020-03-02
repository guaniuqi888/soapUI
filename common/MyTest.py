from common.Driver import Driver
import unittest
import time


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('初始化方法')
        driver = Driver()
        cls.driver = driver.startUp()




    def setUp(self):
        print('每个test执行一次')










    def tearDown(self):
        print('每次关闭一次')



    @classmethod
    def tearDownClass(cls):
        print('初始化方法')
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()

