#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time , unittest
class PythonOrgSearch(unittest.TestCase):  

	def setUp(self):  
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '4.4.2'
		desired_caps['deviceName'] = '127.0.0.1:62001'
		desired_caps['appPackage'] = 'xikang.cdpm.patient'
		desired_caps['appActivity'] = 'xikang.cdpm.patient.LoadingActivity'
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

	def changeheight(self):
		driver = self.driver
		height = '180'
		driver.find_element_by_id("xikang.cdpm.patient:id/main_raidobutton_tab3").click()
		time.sleep(3)
		driver.find_element_by_id("xikang.cdpm.patient:id/tab4").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("xikang.cdpm.patient:id/generalInfoButton").click()
		driver.implicitly_wait(5)
		driver.find_element_by_id("xikang.cdpm.patient:id/button2").click()
		time.sleep(5)
		driver.implicitly_wait(5)
		driver.find_element_by_id("xikang.cdpm.patient:id/et_generalinfo_update_heightvalue").clear()
		driver.find_element_by_id("xikang.cdpm.patient:id/et_generalinfo_update_heightvalue").send_keys(height)
		driver.implicitly_wait(5)
		driver.find_element_by_id("xikang.cdpm.patient:id/button2").click()
		driver.implicitly_wait(5)
		time.sleep(5)
		

	def checkheight(self):
		driver = self.driver
		driver.find_element_by_id("xikang.cdpm.patient:id/button2").click()
		driver.implicitly_wait(5)
		assert '180.0' in driver.find_element_by_id("xikang.cdpm.patient:id/et_generalinfo_update_heightvalue").text
		'''driver = self.driver
		driver.find_element_by_id("xikang.cdpm.patient:id/button2").click()
		driver.implicitly_wait(5)
		height = driver.find_element_by_id("xikang.cdpm.patient:id/et_generalinfo_update_heightvalue").text
		while height == "180.0":
			print "ok"
			break
		else:
			print "wrong"'''


	def login(self,un,psw):
		driver = self.driver
		username = un
		password = psw
		driver.find_element_by_xpath("//an1droid.widget.TextView[contains(@text,'掌上云医院')]").click()
		driver.implicitly_wait(10)
		time.sleep(10)
		driver.find_element_by_id("xikang.cdpm.patient:id/main_raidobutton_tab4").click()
		driver.implicitly_wait(10)
		driver.find_element_by_id("xikang.cdpm.patient:id/layout_avatar").click()
		driver.implicitly_wait(5)
		try:
			driver.find_element_by_id("xikang.cdpm.patient:id/login_user_account")
			findlog = True
		except:
			findlog = False
		while findlog == True:
			driver.find_element_by_id("xikang.cdpm.patient:id/login_user_account").clear()
			driver.find_element_by_id("xikang.cdpm.patient:id/login_user_account").send_keys(username)
			driver.implicitly_wait(5)
			driver.find_element_by_id("xikang.cdpm.patient:id/login_user_password").clear()
			driver.find_element_by_id("xikang.cdpm.patient:id/login_user_password").send_keys(password)
			driver.implicitly_wait(5)
			driver.find_element_by_id("xikang.cdpm.patient:id/loginButton").click()
			time.sleep(5)
			break
		else:
			driver.find_element_by_id("xikang.cdpm.patient:id/back_button").click()
			time.sleep(5)
	def welcome(self):
		driver = self.driver
		try:
			driver.find_element_by_id("xikang.cdpm.patient:id/introduction_enter_button")
			find = True
		except:
			find = False
			while find == True:
				driver.find_element_by_id("xikang.cdpm.patient:id/introduction_enter_button").click()
				driver.implicitly_wait(5)
				driver.find_element_by_id("xikang.cdpm.patient:id/mask_bt").click()
				driver.implicitly_wait(5)
				break

	def run1(self):
		driver = self.driver
		
		self.welcome()
		time.sleep(3)
		self.login('15800000004','123456a')
		driver.implicitly_wait(5)
		time.sleep(5)
		self.changeheight()
		driver.implicitly_wait(5)
		
		self.checkheight()
		time.sleep(3)
	


	def tearDown(self):
		pass


if __name__ == "__main__":  
    suite = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch)
    unittest.TextTestRunner(verbosity=2).run(suite)