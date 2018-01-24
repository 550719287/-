#coding=utf-8
import unittest
import time 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')  
 
   
class PythonOrgSearch1(unittest.TestCase):
    driver = webdriver.Firefox()

    def setUp(self):  
        global driver
        driver = self.driver
        #全局变量加入初始化模块
        
    def login(self):  
        
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
        cur_url = driver.current_url
        while(cur_url == "http://shenyang.xikang.cn/ch/"):
            self.driver.find_element_by_id("loginbutton").click()
            print u"网络不给力"
            time.sleep(3)
            break
        
    def loginfailed(self):
        
        try:
            driver.find_element_by_xpath("//button[@id=errorTryAgain]")
            find = True
        except:
            find = False
        while find == True:  
            driver.find_element_by_xpath("//button[@id=errorTryAgain]").click()
            time.sleep(10)   
    def changeheight(self):

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
        
    def test_run2(self):  
        
        selurl = "http://shenyang.xikang.cn/ch/"
        self.driver.get(selurl)
        self.loginfailed()
        time.sleep(5)
        self.login()
        self.loginfailed()
        driver.implicitly_wait(5)
        self.check_login_success()
        driver.implicitly_wait(5)
        time.sleep(5)
        self.changeheight()

    def tearDown(self):
        driver.quit()


def report():
    filename = "D:\\Report2.html"
    fp = open(filename , "wb")
    testunit = unittest.TestSuite()
    testunit.addTest(PythonOrgSearch1('test_run2'))
    HTMLTestRunner(stream = fp , title = "云医院web测试报告" , description = "详情").run(testunit)


if __name__ == "__main__":
    report()
