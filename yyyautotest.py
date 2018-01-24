#coding=utf-8
import unittest ,time 
from allrun import PythonOrgSearch1
from allrun import PythonOrgSearch
import HTMLTestRunner
   
class Mytest(unittest.TestCase):
    

        def setUp(self):
            pass

        def run1(self):
            self = PythonOrgSearch1()

            self.run2()

        def run2(self):
            self = PythonOrgSearch()

            self.run1()

        def test_run(self):
            self.run1()
            self.run2() 

        def tearDown(self):
            pass


def report():
    filename = "D:\\Report_yyytest.html"
    fp = open(filename , "wb")
    testunit = unittest.TestSuite()
    testunit.addTest(Mytest('test_run'))
    HTMLTestRunner.HTMLTestRunner(
        stream = fp , 
        title = "Report" , 
        description = "Report_description").run(testunit)

if __name__ == "__main__":
    report()