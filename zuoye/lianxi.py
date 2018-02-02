from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import base64
import time

desirded_caps = {}
# 系统
desirded_caps['platformName'] = 'Android'
# 版本
desirded_caps['platformVersion'] = '5.1'
#设备号
desirded_caps['deviceName'] = '192.168.56.101:5555'
#包名
desirded_caps['appPackage'] = 'io.manong.developerdaily'
#启动名
desirded_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
# 解决中文输入问题
desirded_caps['unicodeKeyboard'] = True
desirded_caps['resetKeyboard'] = True


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desirded_caps)



# 判断是否安装软件
# if driver.is_app_installed('io.manong.developerdaily'):
#     driver.remove_app('io.manong.developerdaily')
# else:
#     driver.install_app('./Desktop/io.manong.developerdaily_3.0.3_liqucn.com.apk')


# 发送当前文件b.txt到手机sdcard目录下
# data = str(base64.b64encode('hello python!!!'.encode('utf-8')),'utf-8')
# driver.push_file('/sdcard/b.txt',data)


# 从手机sdcard目录拉取文件b.txt，存储到桌面并命名为phone.txt
# data = driver.pull_file('/sdcard/b.txt')
# phone_data = str(base64.b64decode(data),'utf-8')
# print(phone_data)
# 第一种
# file = open('/Users/yangjiaai/Desktop/phone.txt','a')
# file.write(phone_data)
# 第二种
# with open('/Users/yangjiaai/Desktop/phone.txt','a') as f:
#     f.write(phone_data)


# 判断模拟器中计算器是否包含”删除”，包含打印True， 不包含打印False
# 第一种
# data = driver.find_element_by_xpath("//*[contains(@text,'删除')]").text
# if '删除' == data:
#     print(True)
# else:
#     print(False)
# 第二种
# if '删除' in driver.page_source:
#     print(True)
# else:
#     print(False)


# 进入模拟器短信，给用户为13488834010的手机号连续发送三条短信，内容分别为123456 ，sd345，你好
# driver.find_element_by_id('com.android.mms:id/action_compose_new').click()
# driver.find_element_by_id('com.android.mms:id/recipients_editor').send_keys('13488834010')
# 第一种
# driver.find_element_by_id('com.android.mms:id/embedded_text_editor').send_keys('123456')
# driver.find_element_by_id('com.android.mms:id/send_button_sms').click()
# driver.find_element_by_id('com.android.mms:id/embedded_text_editor').send_keys('sd345')
# driver.find_element_by_id('com.android.mms:id/send_button_sms').click()
# driver.find_element_by_id('com.android.mms:id/embedded_text_editor').send_keys('你好')
# driver.find_element_by_id('com.android.mms:id/send_button_sms').click()
# 第二种
# data_list = {"123456",'sd345','你好'}
# for i in data_list:
#     driver.find_element_by_id('com.android.mms:id/embedded_text_editor').send_keys(i)
#     driver.find_element_by_id('com.android.mms:id/send_button_sms').click()



# 模拟器电话本新建用户 张三，要求必填信息为：姓名 电话 电子邮件 网址，保存后修改张三姓名改为李四
# 启动应用
# driver.start_activity('com.android.contacts','.activities.PeopleActivity')
# driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
# # driver.find_element_by_id('com.android.contacts:id/left_button').click()
# driver.find_element_by_xpath("//*[contains(@text,'姓名')]").send_keys('张三')
# driver.find_element_by_xpath("//*[contains(@text,'电话')]").send_keys('123456')
# driver.swipe(300,2334,300,488,3000)
# driver.find_element_by_xpath("//*[contains(@text,'电子邮件')]").send_keys('12345@163.com')
# driver.swipe(300,2334,300,488,3000)
# driver.find_element_by_xpath("//*[contains(@text,'网站')]").send_keys('www.itcast.com')
# driver.find_element_by_class_name('android.widget.ImageButton').click()
# driver.find_element_by_id('com.android.contacts:id/menu_edit').click()
# driver.find_element_by_xpath("//*[contains(@text,'张三')]").send_keys('李四')
# driver.find_element_by_class_name('android.widget.ImageButton').click()



# 进入模拟器设置页面向上由“存储”滑动到“更多”，之后通过屏幕的宽高比例，模拟向下滑动动作，输出当前屏幕内“存储”的坐标
# driver.start_activity('com.android.settings','.Settings')
# driver.swipe(300,2029,300,953,5000)
# print(driver.get_window_size())
# driver.swipe(300,986,300,1813,5000)
# time.sleep(3)
# get_value = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# print(get_value.location)



# 启动开发者头条app，通过显示等待方式点击“我的”按钮，之后将应用置于后台10秒，通过显示等待方式点击阅读，截取手机屏幕图片保存到当前目录
# driver.start_activity('io.manong.developerdaily','io.toutiao.android.ui.activity.MainActivity')
# WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'我的')]"))
# driver.find_element_by_xpath("//*[contains(@text,'我的')]").click()
# driver.background_app(5)
# read = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'阅读')]"))
# read.click()
# driver.get_screenshot_as_file('jietu.png')



# 启动开发者头条，打开通知栏，在通知栏内点击飞行模式，之后关闭通知栏，关闭开发者头条app，
# 打开设置页面，降低手机音量键到最低，更改手机网络模式为移动流量，截取手机屏幕保存到当前目录
# driver.start_activity('io.manong.developerdaily','io.toutiao.android.ui.activity.MainActivity')
# driver.open_notifications()
# driver.find_element_by_id('com.android.systemui:id/header').click()
# driver.find_element_by_xpath("//*[contains(@text,'飞行')]").click()
# driver.keyevent(3)
# driver.close_app()
#
# driver.start_activity('com.android.settings','.Settings')
#
# for i in range(6):
#     driver.keyevent(25)
#
# driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
# driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
# driver.find_element_by_id('android:id/switchWidget').click()
# driver.get_screenshot_as_file('jietu2.png')








driver.quit()