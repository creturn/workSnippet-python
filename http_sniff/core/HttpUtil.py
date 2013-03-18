#!/usr/bin/env python
#coding: utf-8 
import cookielib
import urllib2,urllib
import os
import gzip,StringIO
"""
HttpUtil是http的工具类,此类会缓存cookie,并且支持gzip页面
Blog: www.creturn Autor: Return 
"""
class HttpUtil():
	# http head信息
	head       = {}
	# cookie 
	cookie     = None
	# cookie存储路径
	cookieFile = ''
	# connect 
	opener     = None
	# init function
	def __init__(self):

		self.head       = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		self.cookieFile = './cookie.dat'
		self.cookie     = cookielib.MozillaCookieJar(self.cookieFile)
		self.opener     = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
		# self.initCookieFile()
	# create cookie file
	def initCookieFile(self):
		if not os.path.exists(self.cookieFile):
			os.mkdir(os.path.dirname(self.cookieFile))
	# http GET function
	def get(self,URL):
		return self.getResult(URL)
	# http POST function
	def post(self,URL,DATA):
		return self.getResult(URL, DATA)
	# connent httpserver and get result
	def getResult(self,URL,DATA = {},STATUS = 1):
		self.loadCookie()
		#result = urllib2.urlopen(URL)
		result = self.opener.open(urllib2.Request(URL,headers = self.head),urllib.urlencode(DATA))
		data = result.read()
		# if gzip uncode it
		if result.headers.get('content-encoding',None) == 'gzip':
			data = gzip.GzipFile(fileobj=StringIO.StringIO(data)).read()
		self.saveCookie()
		return data
	# save the cookie file
	def saveCookie(self):
		self.cookie.save(self.cookieFile,ignore_discard = True, ignore_expires = True)
	# setCookie
	def setCookie(self,key,val):
		pass
	# load cookie from the cookiefiile
	def loadCookie(self):
		try:
			self.cookie.load(ignore_discard = True, ignore_expires = True)
		except Exception:
			self.saveCookie()

def http():
	return HttpUtil()
