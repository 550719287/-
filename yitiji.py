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
desired_caps['unicodeKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


driver.find_element_by_id('com.xikang.acornapppublichealth:id/btn_select_resident').click()
driver.implicitly_wait(5)

'''driver.find_element_by_xpath('//android.widget.Spinner[@resource-id=\"com.xikang.acornapppublichealth:id/resident_filter_spinner\"]').click()
driver.implicitly_wait(5)

driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.xikang.acornapppublichealth:id/txtvSpinner\" and @text=\"姓名\"]').click()

driver.tap([(448,115),(884,165)])
#print contexts
#driver.back()
time.sleep(3)

driver.find_element_by_id('com.xikang.acornapppublichealth:id/resident_entry_text').send_keys(u"陶映阳")
driver.implicitly_wait(5)
driver.tap([(448,115),(884,165)])

driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.xikang.acornapppublichealth:id/resident_search_btn\"]').click()'''

driver.find_element_by_xpath('//android.widget.ListView[@resource-id=\"com.xikang.acornapppublichealth:id/content_view\"]/android.widget.LinearLayout[1]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.xikang.acornapppublichealth:id/btn_modify_persionalfiles\"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.Spinner[@resource-id=\"com.xikang.acornapppublichealth:id/nation_filter_spinner\"]').click()
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element_by_xpath('//android.widget.TextView[@text=\"布依族\"]').click()
driver.implicitly_wait(5)
driver.tap([(276,540),(451,599)])
driver.swipe(451,785,451,242,8000)
driver.implicitly_wait(5)
driver.swipe(451,723,451,211,8000)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.CheckBox[@resource-id=\"com.xikang.acornapppublichealth:id/check_payworker_modify\"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//android.widget.Spinner[@resource-id=\"com.xikang.acornapppublichealth:id/disease_filter_spinner1\"]').click()
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element_by_xpath('//android.widget.TextView[@text=\"慢性阻塞性肺疾病\"]').click()
contexts = driver.contexts
print contexts
driver.implicitly_wait(5)
driver.back()
driver.find_element_by_xpath('//android.widget.EditText[@resource-id=\"com.xikang.acornapppublichealth:id/edit_disease_description_modify1\"]').clear()
