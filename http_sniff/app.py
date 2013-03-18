#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: app.py
Descript: http test 
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
from core import HttpUtil
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
def main():
	#url = 'http://www.12306.cn/mormhweb/'
	# url = 'https://dynamic.12306.cn/otsweb/loginAction.do?method=init'
	url = 'http://passport.baidu.com/'
	http = HttpUtil.http()
	loginHtml = http.get(url)
	print loginHtml
	open('login.js','w').write(loginHtml)


if __name__ == '__main__':
	main()