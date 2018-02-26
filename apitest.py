
#coding = utf-8

from thrift import Thrift   
#from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.transport import THttpClient 
import time
import sys   
sys.path.append('D:/thrift/gen-py')  
import ttypes
import UserService
import traceback
import logging
import unittest
'''sys.path.append('D:/thrift/gen-py/XKCommon')
from ttypes import *'''

class Mytest(unittest.TestCase):

	transport = THttpClient.THttpClient('10.32.173.200', 8085, '/XK_Phr_Proxy/UserServlet')  # ip  port projectname
	transport = TTransport.TBufferedTransport(transport)
	protocol = TBinaryProtocol.TBinaryProtocol(transport)
	client = UserService.Client(protocol)
	def setUp(self):
		pass
		
	
	def test_run(self):
		client = self.client
		
		#client.getAccountInfosByDeviceId('wifidc:44:27:96:e9:ea') 
		self.assertRaises(HealthServiceException,client.getAccountInfosByDeviceId,'awifidc:44:27:96:e9:ea')
			




	def test_2(self):
		pass


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

	suite = unittest.makeSuite(Mytest)
	unittest.TextTestRunner(verbosity=2).run(suite)