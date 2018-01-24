#!/usr/bin/python
#coding:utf-8
import urllib
import urllib2
import cookielib
import re
import requests
import sys

#发送get请求
url = "http://passport.xikang.com/cas/login-with-ch?service=http%3A%2F%2Fwww.xikang.cn%2Fj_spring_cas_security_check"
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()


foundH1user = re.findall('<input type=\"hidden\" name=\"lt\" value=\"(.*)\" />', res); #正则匹配登陆令牌
foundH1user1 = re.findall('jsessionid=(.*)\?service', res); #正则匹配jsessionid

yzm= foundH1user[0]  #cas登陆令牌

jsessionid='jsessionid='+foundH1user1[0]
print jsessionid

referer = 'http://passport.xikang.com/cas/login-with-ch;'+jsessionid+'?service=http%3A%2F%2Fwww.xikang.cn%2Fj_spring_cas_security_check';
print referer
hosturl = referer;
posturl = referer;


#获取cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
h = urllib2.urlopen(hosturl)



#消息头
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
           'Referer' : 'http://passport.xikang.com/cas/login-with-ch?service=http%3A%2F%2Fwww.xikang.cn%2Fj_spring_cas_security_check',
           'Host':'passport.xikang.com',
           'Content-Type':'application/x-www-form-urlencoded',
           'Accept':'text/html, application/xhtml+xml, */*',
           'Accept-Language':'zh-CN',
           'Connection':'Keep-Alive',
          }
#消息体
postData = {'userType' : 'all',
      'lt' : yzm,
      '_eventId' : 'submit',
      'username' : '15800000004',
      'password' : '123456a',
      'verCode' : '',
      'browserVersion': 'Microsoft Internet Explorer'
      }


print postData
print headers
print posturl

#发送post登陆请求
postData = urllib.urlencode(postData)
req = requests.post(posturl,data=postData,headers=headers,allow_redirects=False)
print req.headers["Location"]

#发送重定向302的get请求
url = req.headers["Location"]
req = urllib2.Request(url)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
type=sys.getfilesystemencoding()
print res.decode('UTF-8').encode(type)


#验证登陆是否成功
foundH1user3 = re.findall('</a></span><span title="(.*)">', res);
username=foundH1user3[0].decode('UTF-8')

if username==u'赵云':
    print u"cas登陆验证成功"
else:
    print u"cas登陆验证失败"
