#coding=utf-8
import time
 
def timeslong(func):
    def call():
    	i = 0
        while i < 5:
        	func()
        	i = i + 1
    return call

@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

f()