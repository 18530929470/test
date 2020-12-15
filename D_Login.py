#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2020-12-12 18:35
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : D_Login.py
# @Software : PyCharm




from selenium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_ddx(url,value_A,value_B,value_C):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    # 添加Cookie
    # 将 fiddler 中抓到的 cookie 放到对应值中
    driver.add_cookie({'name': 'UM_distinctid', 'value': value_A})
    driver.add_cookie({'name': 'CNZZDATA1275846928', 'value':value_B})
    driver.add_cookie({'name': 'PHPSESSID', 'value':value_C})

    # 刷新页面
    time.sleep(5)
    driver.refresh()

    #点击个人中心
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@class="login-register"]/span')))
    driver.find_element_by_xpath('//*[@class="login-register"]/span').click()
    time.sleep(2)

    #点击淘宝授权
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[contains(text(),"淘宝授权")]')))
    driver.find_element_by_xpath('//*[contains(text(),"淘宝授权")]').click()
    time.sleep(3)


    #点击更新授权
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[contains(text(),"更新授权")]')))
    driver.find_element_by_xpath('//*[contains(text(),"更新授权")]').click()
    time.sleep(2)

    # 切换windows窗口
    driver.switch_to.frame(0)

    #输入用户名
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, 'fm-login-id')))
    driver.find_element_by_id('fm-login-id').send_keys("2016wdzj")

    #输入密码
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, 'fm-login-password')))
    driver.find_element_by_id('fm-login-password').send_keys("jnkj@2020")
    time.sleep(2)

    # 点击登录
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.TAG_NAME, 'button')))
    driver.find_element_by_tag_name('button').click()


    time.sleep(5)
    # driver.quit()

if __name__ == '__main__':
    test_url = 'https://www.dingdanxia.com/index/home.html'
    value_A = '1764d135e9124d-0a044b0b1de8c-333376b-1fa400-1764d135e92c84'
    value_B = '25107328-1607606891'
    value_C = 'ouv3p42rjged37esrss68qjfvl'
    login_ddx(test_url,value_A,value_B,value_C)

