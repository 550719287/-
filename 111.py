#coding=utf-8
import unittest ,time 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import sys

class ikeeper(object):
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '7.1.1'
	desired_caps['deviceName'] = '14105036c824342a078e'
	desired_caps['appPackage'] = 'com.xikang.acornapppublichealth'
	desired_caps['appActivity'] = 'com.xikang.acorncommonlib.Activity.ReadCardActivity'
	driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

	def login(self,username,psw):
		pass

if __name__ == "__main__":  
	time.sleep(5)
	ikeeper_Android().login("18600000111","qwe123")