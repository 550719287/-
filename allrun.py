#coding=utf-8
import unittest ,time 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf8')  
   
class PythonOrgSearch1(object):  
    driver = webdriver.Firefox()
 
    def login(self):  
        driver = self.driver
        username = "15800000004"
        password = "123456a"
        driver.find_element_by_class_name("a_but_on").click()  
        driver.implicitly_wait(5)
        driver.switch_to_frame("myframe")
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("loginbutton").click()
        driver.implicitly_wait(5)
        time.sleep(2)
        
    def check_login_success(self):
        driver = self.driver
        cur_url = driver.current_url
        while(cur_url == "http://shenyang.xikang.cn/ch/"):
            self.driver.find_element_by_id("loginbutton").click()
            print "wrong"
            time.sleep(3)
            break
        
    def loginfailed(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//button[@id=errorTryAgain]")
            find = True
        except:
            find = False
        while find == True:  
            driver.find_element_by_xpath("//button[@id=errorTryAgain]").click()
            time.sleep(10)   
    def changeheight(self):
        driver = self.driver
        '''  tset_use
        driver.get("http://shenyang.xikang.cn/member/cas/login/index.html")'''

        '''   test_use
        driver.find_element_by_id("username").send_keys("15800000004")
        driver.find_element_by_id("password").send_keys("123456a")
        driver.find_element_by_class_name("regBtn").click()
        driver.implicitly_wait(5)
        '''

        assert "我的云医院" in driver.find_element_by_xpath("//span[@class='span_top']").text
        driver.find_element_by_xpath("//li[@id='icon-wdzb']").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//a[@href='http://phrbrowser.xikang.com/phrbrowser/index/indexAction.html']").click()
        driver.implicitly_wait(10)
        
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:

                driver.switch_to_window(handle)
                driver.find_element_by_xpath("//a[@href='#']").click()
                driver.find_element_by_xpath("//input[@id='height']").clear()
                driver.find_element_by_xpath("//input[@id='height']").send_keys('180')
                driver.find_element_by_xpath("//a[@class='saveBtn']").click()
                driver.implicitly_wait(5)
                
                try:
                    driver.find_element_by_xpath("//a[@href='#']")
                    find1 = True
                except:
                    find1 = False
                while find1 == True:  
                    print 'success'
                    break
                else:
                    print 'failed'
                    break
        
    def run2(self):  
        driver = self.driver
        selurl = "http://shenyang.xikang.cn/ch/"
        self.driver.get(selurl)
        self.loginfailed()
        time.sleep(5)
        self.login()
        self.loginfailed()
        driver.implicitly_wait(5)
        self.check_login_success()
        driver.implicitly_wait(5)
        
        self.changeheight()

class PythonOrgSearch(object):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'xikang.cdpm.patient'
    desired_caps['appActivity'] = 'xikang.cdpm.patient.LoadingActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


    def changeheight(self):
        driver = self.driver
        height = '180'
        driver.find_element_by_id("xikang.cdpm.patient:id/main_raidobutton_tab3").click()
        time.sleep(3)
        driver.find_element_by_id("xikang.cdpm.patient:id/tab4").click()
        driver.implicitly_wait(5)
        driver.find_element_by_id("xikang.cdpm.patient:id/generalInfoButton").click()
        driver.implicitly_wait(5)
               
                

    def checkheight(self):
        driver = self.driver
        driver.find_element_by_id("xikang.cdpm.patient:id/button2").click()
        driver.implicitly_wait(5)
        assert '180.0' in driver.find_element_by_id("xikang.cdpm.patient:id/et_generalinfo_update_heightvalue").text


    def login(self,un,psw):
        driver = self.driver
        username = un
        password = psw
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'掌上云医院')]").click()
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
    

  