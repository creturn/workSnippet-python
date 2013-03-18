#!/usr/bin/env python
#coding: utf-8 
from core import HttpUtil
from core import AndroidApi
import sys
import Image
reload(sys)
sys.setdefaultencoding('utf-8')
def showSms(msg):
	for m in msg['list']:
		print 'User:',m['name'],'-',m['df']
def showContacts(contacts):
	print 'Count:',len(contacts['list'])
	for m in contacts['list']:
		print 'User:',m['name'],'-',m['phone']
	 	 
def main():
	host= 'http://192.168.5.105:8888/'
	http = HttpUtil.http()
 
	api = AndroidApi.api(http,host)
	api.login('admin')
	phoneInfo = api.getPhoneInfo()
	print phoneInfo
	# sms = api.getSms()
	# contacts = api.getContacts()
	# showContacts(contacts)
	open('screen.jpg','w').write(api.getScreen())
	img = Image.open('./screen.jpg');
	img.show()

if __name__ == '__main__':
	main()