from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest


class TestDemo():

    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('https://www.baidu.com')

    def test_wechat(self):
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(3)
        print('success')


if __name__ == '__main__':
    pytest.main(['-vs'])
