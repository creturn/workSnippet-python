#!/usr/bin/env python

import sys
try:
	import pygtk
	pygtk.require('2.0')
except:
	print 'can not import gtk 3.0'
try: 
	import gtk
	import gtk.glade
except:
	print 'can not import gtk'
	sys.exit(1)

class HelloWorldGtk:
	def __init__(self):
		
		builder = gtk.Builder()
		builder.add_from_file('./test.glade')
		builder.connect_signals(self)
		# self.gladefile = './test.glade'
		#self.window = gtk.glade.XML(self.gladefile)
		# self.win = self.window.get_widget('window_main')
		self.win = builder.get_object('window_main')
		self.notebook = 
		self.win.show()
		if self.win:
			self.win.connect('destroy',gtk.main_quit)
		else:
			print 'not suscess'
		
if __name__ == '__main__':
	hwg = HelloWorldGtk()
	gtk.main()