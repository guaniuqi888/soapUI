from selenium.webdriver.common.by import By
from common.Driver import Driver
import time

class HomePage(object):
    #封装页面元素属性（定位方式）

    #搜索输入框
    search_input = (By.ID,'com.ss.android.article.news:id/bo_')

    #搜索子输入框
    search_input_sub = (By.ID,'com.ss.android.article.news:id/vr')

    #搜索按钮
    search_btn = (By.ID,'com.ss.android.article.news:id/vq')

    def __init__(self,driver):
        #用来接收xxTest的driver实例

        self.driver = driver


    def clickSerach(self):
        self.driver.find_element(*self.search_input).click()
        time.sleep(2)
        print('点击完成')
        time.sleep(2)

        # 点击搜索按钮操作

    def clickSearchBtn(self):
        time.sleep(2)

        self.driver.find_element(*self.search_btn).click()

        print('点击完成')

        time.sleep(2)


        # 搜索按钮的输入操作

    def InputSearch(self, test_data):
        self.clickSerach()

        time.sleep(2)

        self.driver.find_element(*self.search_input_sub).send_keys(test_data)

        print('点击完成')

        time.sleep(2)

        self.clickSearchBtn()









# if __name__ == '__main__':
#     d=Driver()
#     driver = d.startUp()
#     h = HomePage(driver)
#     h.InputSearch('1')
