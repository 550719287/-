#coding=utf-8
import unittest ,time 
from appium import webdriver  
from selenium.webdriver.common.keys import Keys
from appium.webdriver.mobilecommand import MobileCommand

#1.9.0family
class ikeeper_Android(object): 

	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '4.2.2'
	desired_caps['deviceName'] = '04157df4949e551a'
	desired_caps['appPackage'] = 'com.xikang.utmostcare.family'
	desired_caps['appActivity'] = 'com.xikang.utmostcare.family.MainActivity'
	driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


	def login(self,username,psw):
		driver = self.driver
		print driver.contexts
		driver.find_element_by_xpath("//android.widget.EditText[@content-desc='请输入账号']").send_keys(username)
		driver.implicitly_wait(5)
		driver.find_element_by_xpath("//android.widget.EditText[@resource-id='password_input']").clear()
		driver.find_element_by_xpath("//android.widget.EditText[@resource-id='password_input']").send_keys(psw)
		driver.implicitly_wait(5)
		driver.find_element_by_xpath("//android.widget.Button[@content-desc='登 录 ']").click()

	def register(self):
		self.driver.find_element_by_xpath("//android.view.View[@content-desc='新用户注册']").click()
		#新注册页面

	def click_setting(self):
		
		self.driver.find_element_by_xpath("//android.view.View[@content-desc=' ']").click()
		#断言/用户信息
		assert '' in driver.find_element_by_xpath("").text

	def click_message_notice(self):
		driver = self.driver
		driver.find_element_by_xpath("//android.view.View[@content-desc='身高体重测量结果通知']").click()
		#断言

	def down(self):
		driver = self.driver
		driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='熙心照护']/android.view.View[10]/android.view.View[3]").click()
		#断言

	def click_family(self):
		driver = self.driver
		driver.find_element_by_xpath("//android.view.View[@content-desc='联系家人']").click()
		#断言 ，操作
	def click_photo(self):
		driver = self.driver
		driver.find_element_by_xpath("//android.view.View[@content-desc='照片分享']").click()
		#断言
	def click_myserver(self):
		driver = self.driver
		driver.find_element_by_xpath("//android.view.View[@content-desc='我的服务']").click()
		#断言，点击操作
	def click_addfamily(self):
		self.driver.find_element_by_xpath("//android.view.View[@content-desc='添加家人']").click()
		#断言，操作
	def click_myorder(self):
		self.driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='熙心照护']/android.view.View[15]/android.view.View[3]").click()
		#点击

	def run(self):
		pass
		

if __name__ == "__main__":  
	time.sleep(5)
	ikeeper_Android().login("18600000111","qwe123")


	#ikeeper_Android().run()