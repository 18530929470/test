#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020-09-29 23:41
# @Author   :wangqinghua
# @File     : 百度搜索.py
# @Software : PyCharm


from selenium import webdriver
import unittest
from time import sleep


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.dr.quit()

    def baidu_search(self, searchkeys):
        dr = self.dr
        dr.get(self.base_url)
        dr.find_element_by_id("kw").send_keys(searchkeys)
        dr.find_element_by_id("su").click()
        sleep(3)

    def test_selenium(self):
        self.baidu_search("明天过后")
        self.assertEqual(self.dr.title, "明天过后_百度搜索")
        sleep(5)

    def test_python(self):
        self.baidu_search("慢慢靠近")
        self.assertEqual(self.dr.title, "慢慢靠近_百度搜索")


if __name__ == "__main__":
    unittest.main()