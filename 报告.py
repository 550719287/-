if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(GetUserTest('test_get_user'))
    suite.addTest(GetUserTest('test_get_user2'))
    fr = open('res.html','wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
    report.run(suite)

if __name__=='__main__':
    # suite = unittest.makeSuite(GetUserTest) #运行类下面的test所有用例
    suite = unittest.defaultTestLoader.discover('.','unit*.py') #运行当前目录下，以unit开头的所有用例

    fr = open('res1.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
    runner.run(suite)

if __name__ == "__main__":

#suite = unittest.TestLoader().loadTestsFromTestCase(client)
#unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.makeSuite(client) #运行类下面的test所有用例
#suite = unittest.defaultTestLoader.discover('.','unit*.py') #运行当前目录下，以unit开头的所有用例
fr = open('D:\\Report_ikeepertest.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
runner.run(suite)