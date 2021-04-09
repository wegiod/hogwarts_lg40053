# -*- coding: utf-8 -*-
# @Time      :2021/4/9 10:58 上午
# @Author    :jxd
# @File      :test_wx.py
import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def teardown(self):
        self.driver.quit()

    def test_lxr(self):
        # 打开文件cookies
        db = shelve.open('cookies')
        # 把cookies赋值
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            # 为了避免expiry参数对于脚本的影响，可以删除该参数
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        self.driver.find_element(By.ID, 'username').send_keys("aaa")
        self.driver.find_element(By.NAME, 'acctid').send_keys("111111111")
        self.driver.find_element(By.CSS_SELECTOR, '.ww_telInput_mainNumber').send_keys("15011170052")
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_continue').click()