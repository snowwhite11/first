import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


class Test_info():

    def setup_class(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'io.manong.developerdaily'
        desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
        # 解决中文输入问题
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[contains(@text,'下次再说')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'我的')]").click()
        self.driver.find_element_by_id('io.manong.developerdaily:id/login_btn').click()
        self.driver.find_element_by_id('io.manong.developerdaily:id/btn_email').click()



    def teardown_class(self):
        self.driver.quit()


    def wait_el(self,idel):
        return WebDriverWait(self.driver,5,0.5).until(lambda x: x.find_element_by_id(idel))

    def test001(self):
        # 正确用例
        self.wait_el('io.manong.developerdaily:id/edt_email').send_keys('yangjiaai0826@163.com')
        self.wait_el('io.manong.developerdaily:id/edt_password').send_keys(123456)
        self.wait_el('io.manong.developerdaily:id/btn_login').click()
        self.driver.get_screenshot_as_file('./picture/picture01.png')
        start = self.driver.find_element_by_xpath("//*[contains(@text,'我的收藏')]")
        end = self.driver.find_element_by_xpath("//*[contains(@text,'昨日收益')]")
        self.driver.scroll(start,end)
        self.driver.find_element_by_xpath("//*[contains(@text,'设置')]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@text,'退出当前')]").click()
        self.wait_el('io.manong.developerdaily:id/md_buttonDefaultPositive').click()
        self.driver.scroll(end,start)


    def test002(self):
        # 执行错误的用例---账号正确，密码为空
        self.wait_el('io.manong.developerdaily:id/login_btn').click()
        self.wait_el('io.manong.developerdaily:id/btn_email').click()
        self.wait_el('io.manong.developerdaily:id/edt_email').send_keys('yangjiaai0826@163.com')
        self.wait_el('io.manong.developerdaily:id/edt_password').send_keys()
        self.wait_el('io.manong.developerdaily:id/btn_login').click()
        self.driver.get_screenshot_as_file('./picture/picture02.png')


    def test003(self):
        # 执行错误的用例---账号正确，密码不正确，少输几位
        self.wait_el('io.manong.developerdaily:id/edt_email').clear()
        self.wait_el('io.manong.developerdaily:id/edt_email').send_keys('yangjiaai0826@163.com')
        self.wait_el('io.manong.developerdaily:id/edt_password').send_keys('11')
        self.wait_el('io.manong.developerdaily:id/btn_login').click()
        self.driver.get_screenshot_as_file('./picture/picture03.png')


    def test004(self):
        # 执行错误的用例---账号正确，密码不正确，多输几位
        self.wait_el('io.manong.developerdaily:id/edt_email').clear()
        self.wait_el('io.manong.developerdaily:id/edt_email').send_keys('yangjiaai0826@163.com')
        self.wait_el('io.manong.developerdaily:id/edt_password').send_keys('1234567')
        self.wait_el('io.manong.developerdaily:id/btn_login').click()
        self.driver.get_screenshot_as_file('./picture/picture04.png')


    def test005(self):
        # 执行错误的用例---账号为空，密码正确
        self.wait_el('io.manong.developerdaily:id/edt_email').clear()
        self.wait_el('io.manong.developerdaily:id/edt_email').send_keys('')
        self.wait_el('io.manong.developerdaily:id/edt_password').send_keys('123456')
        self.wait_el('io.manong.developerdaily:id/btn_login').click()
        self.driver.get_screenshot_as_file('./picture/picture05.png')


    def test06(self):
        # 执行错误的用例---账号错误，密码正确
        self.wait_el('io.manong.developerdaily:id/edt_email').clear()
        self.wait_el('io.manong.developerdaily:id/edt_email').send_keys('yangjiaai@163.com')
        self.wait_el('io.manong.developerdaily:id/edt_password').send_keys('123456')
        self.wait_el('io.manong.developerdaily:id/btn_login').click()
        self.driver.get_screenshot_as_file('./picture/picture06.png')


    def test07(self):
        # 执行错误的用例---账号格式错误，密码正确
        self.wait_el('io.manong.developerdaily:id/edt_email').clear()
        self.wait_el('io.manong.developerdaily:id/edt_email').send_keys('yangjiaai0826@')
        self.wait_el('io.manong.developerdaily:id/edt_password').send_keys('123456')
        self.wait_el('io.manong.developerdaily:id/btn_login').click()
        self.driver.get_screenshot_as_file('./picture/picture07.png')














