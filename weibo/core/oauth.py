#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: oauth.py
Descript: This is oauth2 g
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
import HttpUtil
import gtk
import webkit
import json
from urllib2 import urlparse
class oauth():
	def __init__(self):

		# 新浪oauthor认证配置
		self.APP_ID    = '1579593624'
		self.APP_ECRET = 'cd15dbd93fafdc06ae588ee0ff08fbb0'
		self.url_authorize = 'https://api.weibo.com/oauth2/authorize'
		self.url_access_token = 'https://api.weibo.com/oauth2/access_token'
		self.url_callback = 'http://weibo.creturn.com/callback.php'
		self.url_authorize = self.url_authorize + '?client_id=%s&response_type=code&redirect_uri=%s'%(self.APP_ID,self.url_callback)
		#UI初始化
		self.http = HttpUtil.http()
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.connect('destroy',self.close)
		self.win.set_default_size(580,400)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.webview = webkit.WebView()
		self.webview.set_size_request(580,400)
		self.webview.get_settings().set_property('enable-plugins',False)
		self.webview.get_settings().set_property('enable-developer-extras',False)
		self.webview.get_settings().set_property('enable-default-context-menu',False)
		self.webview.connect('navigation-requested',self.on_navigation_requested)
		self.webview.open(self.url_authorize) # 加载认证引导界面
		self.win.add(self.webview)
		self.win.show_all()

	#启动应用
	def run(self):
		gtk.main()
	# 关闭窗口
	def close(self,wiget = None):
		self.win.remove(self.webview)
		gtk.main_quit()
	# 监听webkit地址栏变化获取code
	def on_navigation_requested(self,view,frame,req,data=None):
		uri = req.get_uri()
		parse = urlparse.urlparse(uri)
		if self.url_callback.find(parse.hostname) > 0:
			self.getAccessToken(parse)
			return True
		return False
	#获取token
	def getAccessToken(self,parse):
		code = parse.query.split('=')
		if len(code) == 2:
			self.close()
			data = {
				'client_id':self.APP_ID,
				'client_secret':self.APP_ECRET,
				'grant_type':'authorization_code',
				'redirect_uri':self.url_callback,
				'code': code[1]
			}
			msg = json.loads(self.http.post(self.url_access_token, data))
			print msg

def main():
	oa = oauth()
	oa.run()
	pass
if __name__ == '__main__':
	main()




		