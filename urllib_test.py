#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import cookielib

def hello():
	request = urllib2.Request("http://www.baidu.com")
	response = urllib2.urlopen(request)
	print response.read()

def hello_url_error():
	request = urllib2.Request('http://www.xxxxx.com')
	try:
	    urllib2.urlopen(request, timeout=2)
	except urllib2.URLError, e:
	    print e.reason
	print("hello_url_error finish")

# hello_url_error()

def hello_http_error():
	req = urllib2.Request('http://blog.csdn4.net/cqcre')
	try:
	    urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.code
	    print e.reason
	except urllib2.URLError, e:
	    print e.reason
	else:
	    print "OK"
	print("hello_http_error finish")

# hello_http_error()

def hello_cookie():
	#声明一个CookieJar对象实例来保存cookie
	cookie = cookielib.CookieJar()
	#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
	handler=urllib2.HTTPCookieProcessor(cookie)
	#通过handler来构建opener
	opener = urllib2.build_opener(handler)
	#此处的open方法同urllib2的urlopen方法，也可以传入request
	response = opener.open('http://www.baidu.com')
	for item in cookie:
	    print 'Name = '+item.name
	    print 'Value = '+item.value

# hello_cookie()

def hello_cookie_file():
	#设置保存cookie的文件，同级目录下的cookie.txt
	filename = 'cookie.txt'
	#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
	cookie = cookielib.MozillaCookieJar(filename)
	#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
	handler = urllib2.HTTPCookieProcessor(cookie)
	#通过handler来构建opener
	opener = urllib2.build_opener(handler)
	#创建一个请求，原理同urllib2的urlopen
	response = opener.open("http://www.baidu.com")
	#保存cookie到文件
	cookie.save(ignore_discard=True, ignore_expires=True)

# hello_cookie_file()

def hello_read_cookie_file():
	#创建MozillaCookieJar实例对象
	cookie = cookielib.MozillaCookieJar()
	#从文件中读取cookie内容到变量
	cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
	#创建请求的request
	req = urllib2.Request("http://www.baidu.com")
	#利用urllib2的build_opener方法创建一个opener
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	response = opener.open(req)
	print response.read()

# hello_read_cookie_file()