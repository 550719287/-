#coding=utf-8
import unittest ,time 
from appium import webdriver  
from selenium.webdriver.common.keys import Keys
from appium.webdriver.mobilecommand import MobileCommand
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#1.9.0family


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '14105036c824342a078e'
desired_caps['appPackage'] = 'com.xikang.acornapppublichealth'
desired_caps['appActivity'] = 'com.xikang.acorncommonlib.Activity.ReadCardActivity'
#desired_caps['unicodeKeyboard'] = False
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


driver.find_element_by_id('com.xikang.acornapppublichealth:id/btn_select_resident').click()
driver.implicitly_wait(5)
#contexts = driver.contexts
#print contexts
driver.find_element_by_xpath('//android.widget.Spinner[@resource-id=\"com.xikang.acornapppublichealth:id/resident_filter_spinner\"]').click()
driver.implicitly_wait(5)

driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.xikang.acornapppublichealth:id/txtvSpinner\" and @text=\"姓名\"]').click()

driver.tap([(448,115),(884,165)])
#print contexts
#driver.back()
time.sleep(3)

driver.find_element_by_xpath('//android.widget.EditText[@resource-id=\"com.xikang.acornapppublichealth:id/resident_entry_text\"]').send_keys(u"陶映阳")

driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.xikang.acornapppublichealth:id/resident_search_btn\"]').click()
