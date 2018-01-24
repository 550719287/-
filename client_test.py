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

transport = THttpClient.THttpClient('10.32.173.200', 8085, '/XK_Phr_Proxy/UserServlet')  # ip  port projectname
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = UserService.Client(protocol)
transport.open()  
#log = open(time.strftime('%Y-%m-%d',time.localtime(time.time()))+".txt",'wb')
a = ttypes.AccountInfo()
a.userId = 'M5A1CFEDBE4B09F03008C774D'
a.accountName = '15040344536'
a.password = '123456'
a.deviceId = 'awifidc:44:27:96:e9:ea'

print 'start'
assert client.getMemberHealthInfo('M5A1CFEDBE4B09F03008C774D') is not None

print 'end'
transport.close()
