#encoding=utf-8

import urllib2
import cookielib
import urllib
import re
import sys
import webbrowser
'''模拟登录'''
reload(sys)
sys.setdefaultencoding("utf-8")
# 防止中文报错
CaptchaUrl = "https://health.10086.cn/sfi/s/code/1512023084885/getImageCode?openId=1"
PostUrl = "https://health.10086.cn/sfi/s/wechat/question/saveWechatQuestion"
# 验证码地址和post地址
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
# 将cookies绑定到一个opener cookie由cookielib自动管理
picture = opener.open(CaptchaUrl).read()
# 用openr访问验证码地址,获取cookie
local = open('E:/image.jpg', 'wb')
local.write(picture)
local.close()
# 保存验证码到本地
SecretCode = raw_input('验证码: ')

# 打开保存的验证码图片 输入
postData = {
'imageCode': SecretCode,
'smsCode':'',
'data':'{"imageCode":"111","smsCode":"sdmjfbskf","manageId":"2","manageName":"11","typeId":"2","typeName":"11","questionId":"6","questionName":"","hospitalId":3275,"latitude":41.80864478,"longitude":123.43279092,"openid":"","channelCode":"wechat_main","questionType":"","hospitalName":"","sex":"女","name":"","education":"研究生","pay":"公费医疗","medicalRecord":"","telephone":"","awardStatus":"","result1":3,"result2":"","result3":5,"result4":4,"result5":4,"result6":4,"result7":4,"result8":4,"result9":5,"result10":"","result11":"","result12":3,"result13":4,"result14":3,"result15":4,"result16":3,"result17":5,"result18":"7","result19":4,"result20":"","result21":2,"result26":"","result27":"","result28":"","result29":"","result30":"","result31":"","result32":"","result33":"","result34":"","result35":"","result36":"","result37":"","result38":"","result39":"","result40":"","result41":"","result42":"","result43":"","result44":"","result45":"","result46":"","result47":"","result48":"","result49":"","result50":"","age":"60岁以上"}',
}
headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Connection': 'keep-alive',
'Connection-Length': '1875',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'DNT': '1',
'Host': 'health.10086.cn',
'Referer': 'https://health.10086.cn/questionnaire/all/record.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
'X-Requested-With': 'XMLHttpRequest'
}
# 根据抓包信息 构造headers
data = urllib.urlencode(postData)
# 生成post数据 ?key1=value1&key2=value2的形式
request = urllib2.Request(PostUrl, data, headers)
# 构造request请求
try:

	response = opener.open(request)
	result = response.read()
	print result
	webbrowser.open(response)
	# 打开登录后的页面
except urllib2.HTTPError, e:
	print e.code
	# 利用之前存有cookie的opener登录页面