#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020-09-29 21:40
# @Author   :wangqinghua
# @File     : test.py
# @Software : PyCharm


# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
class Demo(unittest.TestCase):

    def setUp(self):
        print("测试开始")

    def test_01(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.ximalaya.com/yinyue/9963059/")
        driver.find_element_by_css_selector(".xui-header-search-input").send_keys("神秘嘉宾")
        driver.find_element_by_css_selector(".xuicon.xuicon-web_ic_search").click()

    def tearDown(self):
        sleep(10)
        print("测试结束")


if __name__ == '__main__':
    unittest.main()







