from selenium import webdriver
sel = selenium.webdriver.Chrome()
loginurl = 'http://weibo.com/'
    #open the login in page
sel.get(loginurl)
time.sleep(10)

    #sign in the username
try:
    sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[1]/div[1]/input").send_keys('yourusername')
    print 'user success!'
except:
    print 'user error!'
time.sleep(1)
    #sign in the pasword
try:
	sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[2]/div[1]/input").send_keys('yourPW')
   # print 'pw success!'
except:
    print 'pw error!'
time.sleep(1)
    #click to login
try:
    sel.find_element_by_xpath("//div[@id='pl_login_form']/div/div[2]/div[6]/a").click()
    print 'click success!'
except:
    print 'click error!'
time.sleep(3)

