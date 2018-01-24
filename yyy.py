#coding=utf-8
import unittest ,time 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class yyyweb(object):
    driver = webdriver.Firefox()
    def __init__(self):
        global driver
        driver = self.driver


    

    
    def login(self,logweb, logwindow, un, psw):  
        
        selurl = "http://shenyang.xikang.cn/ch/"
        driver.get(selurl)
        username = un
        password = psw
        driver.find_element_by_class_name(logweb).click()  
        driver.implicitly_wait(5)
        driver.switch_to_frame("myframe")
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id(logwindow).click()
        driver.implicitly_wait(5)
        time.sleep(2)
        assert '我的云医院' in driver.find_element_by_class_name("span_top").text

    def checkheight(self,edit,height,tar):
        
        driver.find_element_by_id(edit).click()
        driver.implicitly_wait(5)
        assert height in driver.find_element_by_id(tar).text

    def changeheight(self,edit,inputbox,height,save):
        
        driver.find_element_by_xpath("//li[@id='icon-wdzb']").click()#我的健康档案
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//a[@href='http://phrbrowser.xikang.com/phrbrowser/index/indexAction.html']").click()#我的健康档案
        driver.implicitly_wait(10)
        
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                driver.find_element_by_xpath(edit).click()
                driver.find_element_by_xpath(inputbox).clear()
                driver.find_element_by_xpath(inputbox).send_keys(height)
                driver.find_element_by_xpath(save).click()
                driver.implicitly_wait(5)
                try:
                    driver.find_element_by_xpath(edit)
                    find1 = True
                except:
                    find1 = False
                while find1 == True:  
                    print 'success'
                    break
                else:
                    print 'failed'
                    break





