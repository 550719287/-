def report():
	filename = "D:\\Report_ikeepertest.html"
	fp = open(filename , "wb")
	testunit = unittest.TestSuite()
	testunit.addTest(client('test_getMembers_8')）
	HTMLTestRunner.HTMLTestRunner(
		stream = fp , 
		title = "Report" , 
		description = "Report_description").run(testunit)