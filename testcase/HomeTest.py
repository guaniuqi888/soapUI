from common.MyTest import MyTest
import time
import unittest

from common.Public import Operation
from po.HomePage import HomePage


class HomeTest(MyTest):



    def test_click(self):
        h = HomePage(self.driver)
        h.clickSerach()
        time.sleep(5)
        self.assertEqual(1,1)
        # 发微头条
        # self.driver.find_element_by_id('com.ss.android.article.news:id/bov').click()
        # time.sleep(5)
        # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"发微头条\")").click()
        # time.sleep(5)
        # self.driver.find_element_by_id('com.ss.android.article.news:id/blh').send_keys("这是我的第一个微头条")
        # time.sleep(5)
        # self.driver.find_element_by_id('com.ss.android.article.news:id/a8n').click()
        # time.sleep(5)

    # def test_input(self):
    #     h = HomePage(self.driver)
    #     h.InputSearch('2')
    #     time.sleep(5)
    #     self.assertEqual(1, 1)

    # def test_swipe(self):
    #     p = Operation(self.driver)
    #
    #     p.swipeDown()






if __name__ == '__main__':
    unittest.main()
