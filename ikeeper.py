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

    #def login(self,username,psw):
