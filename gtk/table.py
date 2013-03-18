#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Table:
	def callback(self,widget,data=None):
		print 'hello again %s'%data
	def delete_event(self,widget,event,data=None):
		gtk.main_quit()
		return False
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('Table Exp By:return')
		self.window.connect('delete_event',self.delete_event)
		self.window.set_border_width(10)
		table = gtk.Table(2,2,True)
		self.window.add(table)
		button = gtk.Button('Button 1')
		button.connect('clicked',self.callback,'button 1')

		table.attach(button,0,1,0,1)
		button.show()


		#create second button
		button = gtk.Button('Button 2')
		button.connect('clicked',self.callback,'Button 2')
		table.attach(button,1,2,0,1)
		button.show()

		button = gtk.Button('Quit')
		button.connect('clicked',lambda W: gtk.main_quit())
		table.attach(button,0,2,1,2)
		button.show()
		table.show()
		self.window.show()


def main():
	gtk.main()
	return 0

if __name__ == '__main__':
	Table()
	main()
		