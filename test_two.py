import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest


class TestDemo():

    def setup_method(self):
        # options = Options()
        # options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('https://www.baidu.com')

    def test_wechat(self):
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(3)
        print('success')

    def test_shelve(self):
        # cookies = self.driver.get_cookies()       # 得到页面的cookies
        # print(cookies)
        # cookies = [{'domain': '.qq.com', 'expiry': 1604413299, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1604440493, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': 'jcn0lf'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851061603749'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851061603749'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635944957, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': True, 'value': 'a1659255'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '568090612'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True, 'value': '1428473492936148'}, {'domain': '.qq.com', 'expiry': 1604499639, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1909752025.1604408958'}, {'domain': 'work.weixin.qq.com', 'expiry': 1604440493, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'jcn0lf'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324945168673'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': True, 'value': '82pweMe9cnBtmkjeTeRTZ48OZX2-gOOgUAiY_3dAZbgKesqAst2rQfgzJEnBvUOz'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '3310277632'}, {'domain': '.work.weixin.qq.com', 'expiry': 1607005242, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': True, 'value': 'VZeatHgJVUTXt5ZFWk6-nHbuSJPOrMmL90V4ghMx2DzgLA4uF9GjZ4CAdEPdf3S5y9BbaBw-6tS9fXhIxLqv-sIwXvDUufcsJycYglLDQ8JyCy0cwb_smO394bc3_er-lhLalDpUHSRWi1AkWB6pe2bPYQiV6-k9dfiG32l-7i8c6cJq_x55iXa_brZDub0EduXJnumin-Na1ExAa2DTPp8ZcqrALFXUKikoCcVrA7AQTet9RXn881qZfiSLOpGpANnKbHObL52SOiIHBk5ljg'}, {'domain': '.qq.com', 'expiry': 1667485239, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1510583722.1604408958'}]
        # 当数据存储到shelve库中后，就可以删除上面的cookies了
        # python中存储数据的一个工具（内置模块），专门用来对数据进行持久化存储的一个库，也可以理解成一个小型的数据库
        # 可以通过key ，value来把数据保存到shelve中
        db = shelve.open('cookies')
        # db['cookie'] = cookies
        # db.close()    # 将数据存储到shelve库中后，就可以不用这两句代码了
        cookies = db['cookie']
        db.close()
        # 首先打开一个页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 然后重新打开一个页面，将cookie注入到这个页面中
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')  #第一种方式
        self.driver.refresh()   #第二种方式，也可以实现登录
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element_by_class_name('ww_fileImporter_fileContainer_uploadInputMask').send_keys(r'C:\Users\86159\Downloads\test\Car.xls')
        filename = self.driver.find_element_by_class_name('ww_fileImporter_fileContainer_fileNames').text
        assert 'Car.xls' == filename
        sleep(3)

if __name__ == '__main__':
    pytest.main(['-vs'])



















