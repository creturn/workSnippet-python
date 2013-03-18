#!/usr/bin/env python 
#coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk

class Misc():
	 

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect('destroy',lambda w:gtk.main_quit())
		#self.window.set_default_size(700,400)
		self.init_ui()
		self.window.show()
	def get_text(self,widget,data=None):
		rs = self.entry.get_text()
		print rs
		self.lb_show.set_text(rs)
	#This function is init Gui Interface
	def init_ui(self):
		tabLay = gtk.Table(3,3,True)
		self.window.add(tabLay)

		toolTip = gtk.Tooltips()

		self.entry = gtk.Entry()

		img = gtk.Image()
		img.set_from_file('/home/return/.face')
		self.lb_show = gtk.Label('#')
		btn_1 = gtk.Button('One')
		btn_2 = gtk.Button('two')
		btn_3 = gtk.Button('three')
		btn_3.connect('clicked',self.get_text)
		toolTip.set_tip(btn_3,'this is my button !')
		tabLay.attach(btn_1,0,1,0,1)
		tabLay.attach(btn_2,1,2,1,2)
		tabLay.attach(btn_3,2,3,2,3)
		tabLay.attach(img,1,2,0,1)
		tabLay.attach(self.entry,0,1,2,3)
		tabLay.attach(self.lb_show,1,2,2,3)
		self.entry.show()
		self.lb_show.show()
		img.show()
		btn_1.show()
		btn_2.show()
		btn_3.show()
		tabLay.show()
	def run(self):
		gtk.main()


def main():
	msc = Misc()
	msc.run()

if __name__ == '__main__':
	main()
