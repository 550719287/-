#coding=utf-8
import unittest ,time 
from selenium import webdriver  
from ikeeper_Android_auto import ikeeper_Android

class Mytest(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '4.2.2'
		desired_caps['deviceName'] = 'OVAMUSDINFHMDYJF'
		desired_caps['appPackage'] = 'com.xikang.utmostcare.family'
		desired_caps['appActivity'] = 'com.xikang.utmostcare.family.MainActivity'
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
		
		
	def test_run(self):
		driver = self.driver

 
		ikeeper_Android().login()
		driver.implicitly_wait(10)
		ikeeper_Android().run()


	def tearDown(self):
		pass

'''def report():
    filename = "D:\\Report_yyytest.html"
    fp = open(filename , "wb")
    testunit = unittest.TestSuite()
    testunit.addTest(Mytest('test_run'))
    HTMLTestRunner.HTMLTestRunner(
        stream = fp , 
        title = "Report" , 
        description = "Report_description").run(testunit)
'''
if __name__ == "__main__":
    #report()

	suite = unittest.TestLoader().loadTestsFromTestCase(Mytest)
	unittest.TextTestRunner(verbosity=2).run(suite)