#! /usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
	def hello(self,widget,data=None):
		print 'HelloWorld'
	def delete_event(self,widget,event,data=None):
		print 'delete event occurred'
		return False
	# when windows destroy call this function
	def destroy(self,widget,data=None):
		gtk.main_quit()
		print 'destroy'
	# init function
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		# add delete callback function
		self.window.connect('delete_event',self.delete_event)
		#add destroy callback function 
		self.window.connect('destroy',self.destroy)
		# set window border
		self.window.set_border_width(10)
		#create a buuton
		self.button = gtk.Button('Hello World')
		self.button.connect('clicked',self.hello)
		self.window.add(self.button)		
		self.button.show()
		self.window.show()
	def main(self):
		gtk.main()

if __name__ == '__main__':
	hello = HelloWorld()
	hello.main()
