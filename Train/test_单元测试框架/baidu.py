# coding=utf-8
'''
Created on 2016-7-22
@author: Jennifer
Project:登录百度测试用例
'''
from selenium import webdriver
import unittest, time


class BaiduTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("我是模块用例启动前准备")

    @classmethod
    def tearDownClass(cls) -> None:
        print("我是模块用例启动后准备")



    def setUp(self):
        print('我是用例级别前置条件')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"


    def tearDown(self):
        print('我是用例级别后置条件')
        self.driver.quit()

    def test_baidu01(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title, u"python_百度搜索")
        print("我是用例")

    # def tearDown(self):
    #     print('我是用例级别后置条件')
    #     self.driver.quit()


if __name__ == "__main__":
    # suite = unittest.TestSuite(BaiduTest)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
