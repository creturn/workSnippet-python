#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: app.py
Descript: 微博linux客户端
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
import webkit
import gtk
import os
import urllib2
from urllib2 import urlparse
class appMainUI():
	
	ROOT_PATH = os.getcwd()
	def __init__(self):
		self.init_ui()
	def init_ui(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.connect('destroy',self.close)
		self.win.set_default_size(580,400)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.webview = webkit.WebView()
		self.webview.connect('navigation-requested',self.on_navigation_requested)
		self.webview.set_size_request(580,400)
		self.webview.get_settings().set_property('enable-plugins',False)
		self.webview.get_settings().set_property('enable-developer-extras',False)
		self.webview.get_settings().set_property('enable-default-context-menu',False)
		# 加载主ui界面
		main_ui_url = 'file://' + self.ROOT_PATH+'/ui/main.html'
		self.webview.open(main_ui_url)
		self.win.add(self.webview)
		self.win.show_all()
	def close(self,wiget = None):
		self.win.remove(self.webview)
		gtk.main_quit()
	def on_navigation_requested(self,view,frame,req,data=None):
		uri = req.get_uri()
		parse = urlparse.urlparse(uri)
		if parse.scheme == 'callback':
			json = urllib2.urlopen('https://api.weibo.com/2/statuses/home_timeline.json?count=100&access_token=2.00s4MqTCW9otiBb803d5cc58LOZL_E').read()	
			self.js('HomeSet(%s)'%json)
			return True
		return False
	def js(self,script):
		self.webview.execute_script(script)
	def run(self):
		gtk.main()
		pass

def main():
	app = appMainUI()
	app.run()
if __name__ == '__main__':
	main()