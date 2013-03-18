#!/usr/bin/env python
#coding: utf-8 
import json
import hashlib
import base64
import urllib2
class AndroidApi():
	"""
	Android Server Api for Client
	"""
	_http = None
	_host = ''
	def __init__(self,HTTP = None,HOST = ''):
		self._http = HTTP
		self._host = HOST

	# get Sms infomation
	# pcount page infomation num
	def getSms(self):
		api = self._host + 'sdctl/sms/threadlist/?page=1&pcount=20'
		data =  self.getData(api)
		return self.decode(data['content'])
	# get contacts
	def getContacts(self,page = 1,pcount = 200):
		api = self._host + 'sdctl/contacts/group/has_phone?page=%d&pcount=%d'%(page,pcount)
		data = self.getData(api)
		return self.decode(data['content'])

	# get phone infomation
	def getPhoneInfo(self):
		api = self._host + 'sdctl/device/overview/'
		return self.getData(api)
	def getScreen(self):
		api = self._host + 'sdctl/comm/screenshot/?q=70&m=2'
		return self._http.get(api)
	def login(self,key = ''):
		# get sign key
		api      = self._host + 'sdctl/query/deviceinfo/'
		data     = self.getData(api)
		md5_str  = key.upper() + data['key']
		password =  hashlib.md5(md5_str).hexdigest()
		# check login
		api      = self._host + 'sdctl/comm/checklogin/?key=%s&keeplogin=00'%password
		data     = self.getData(api)
		if data['pass'] == 1:
			print 'login success'
	# decode information
	def decode(self,data):
		data = json.loads(urllib2.unquote(base64.decodestring(data)))
		return data
	def getData(self,url):
		data = json.loads(self._http.get(url))
		return data
		# pass



def api(HTTP,HOST):
	return AndroidApi(HTTP,HOST)

