#coding=utf-8
import unittest ,time 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class yunjia(object):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'xikang.cdpm.patient'
    desired_caps['appActivity'] = 'xikang.cdpm.patient.LoadingActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    def __init__(self):
        
        global driver
        driver = self.driver

    def login(self,un,pw):

    	driver.find_element_by_id("android:id/text1").send_keys(un)
    	driver.find_element_by_id("android:id/text2").send_keys(pw)
    	driver.find_element_by_id("android:id/closeButton").click()

    def dialogue(self,name):

    	driver.find_element_by_xpath("//an1droid.widget.TextView[contains(@text,name)]").click()
    	driver.find_element_by_id("com.xikang.pregnant_doctor:id/chatting_content_et").send_keys("测试ing!？")
    	driver.find_element_by_id("com.xikang.pregnant_doctor:id/chatting_content_et").send_keys(ENTER)
    	#输入发送消息
    	driver.find_element_by_id("com.xikang.pregnant_doctor:id/chatting_attach_btn").click()
    	driver.find_element_by_id("com.xikang.pregnant_doctor:id/chatting_mode_btn").click()
    	#语音图片按钮
    	driver.find_element_by_id("com.xikang.pregnant_doctor:id/btn_left").click()
    	#返回

    def complimentary_service(self,name):

    	driver.find_element_by_id("com.xikang.pregnant_doctor:id/imageview").click()
        #会员
        driver.find_element_by_id("com.xikang.pregnant_doctor:id/tv_follow").click()
        #关注我
        driver.find_element_by_id("com.xikang.pregnant_doctor:id/gift_btn").click()
        #赠送按钮有多个，标识一样
        driver.find_element_by_xpath("//android.widget.RadioButton[contains(@text,name)]").click()
        #Xpath路径不确定，点击选择服务
        driver.find_element_by_id("com.xikang.pregnant_doctor:id/gift_btn").click()
        #确定赠送
        driver.find_element_by_id("com.xikang.pregnant_doctor:id/tv_ing").click()
        #服务中页面
        driver.find_element_by_id("")




