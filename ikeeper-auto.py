#coding=utf-8
import unittest ,time 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ikeeper(object):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = '0123456789ABCDEF'
    desired_caps['appPackage'] = 'com.xk.neu.usermanager'
    desired_caps['appActivity'] = 'com.xk.neu.usermanager.MainActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    def __init__(self):
        
        global driver
        driver = self.driver

	def login(self,username,psw):
		driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.xk.neu.usermanager:id/next']").click()
		#driver.find_element_by_xpath("//android.widget.ListView[@resource-id='com.xk.neu.usermanager:id/ble_device_list']/android.widget.RelativeLayout[2]").click()
		#根据设备进行更换
		timesleep(5)
		driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.xk.neu.usermanager:id/next']").click()
		timesleep(3)
		driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.xk.neu.usermanager:id/next']").click()
	def Health_records(self,blood_pressure,pulse_rate,blood_sugar,oxygen,weight,BMI,body_fat,muscle):
		#点击患者头像进入信息界面
		self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.xk.homescreen:id/image']").click()
		#断言查看基础信息是否正确

		assert 'blood_pressure' in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bw_num']").text

		assert 'pulse_rate' in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bw_num_2']").text

		assert 'blood_sugar' in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bs_num']").text

		assert 'oxygen' in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bo_num']").text

		assert 'weight' in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bo_num']").text

		assert "BMI" in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bo_num']").text

		assert 'body_fat' in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bodyfat_num_3']").text

		assert 'muscle' in driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xk.health.archives:id/tv_bodyfat_num_3']").text

	def message(self):
		#消息通知
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.xk.hSomescreen:id/ll_wdjf']/android.widget.ImageView[1]").click()
		assert '' in 
		
	def photo(self):
		#美好时光
		self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.xk.homescreen:id/ib_mhsg']").click()
		assert '' in 


	def server(self):
		#熙心服务
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.xk.homescreen:id/health_guide']/android.widget.ImageView[1]").click()
		assert '' in 

	def call_family(self):
		#联系家人
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.xk.homescreen:id/health_family']/android.widget.ImageView[1]").click()
		#点击家人进行呼叫
		self.driver.find_element_by_xpath("").click()
		#点击呼叫可选视频语音电话
		self.driver.find_element_by_xpath("").click()

	def health_reminder(self,remind):
		#健康提醒
		self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.xk.homescreen:id/iv_health_care']").click()
		#查看设置的提醒
		assert '' in driver.find_element_by_xpath("remind").text

	def Health_Encyclopedia(self):
		#健康百科
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.xk.homescreen:id/health_encyclopedia']/android.widget.ImageView[1]").click()

	def entertainment(self):
		#电台娱乐
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.xk.homescreen:id/ll_dtyl']/android.widget.ImageView[1]").click()
		#选择某个或几个内容点击查看跳转成功
		self.driver.find_element_by_xpath("").click()
		assert '' in self.driver.find_element_by_xpath("").text

	def setting(self):
		#设置
		self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.xk.homescreen:id/ll_setting']/android.widget.ImageView[1]").click()


