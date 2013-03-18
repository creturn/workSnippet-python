#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Dialog():
	def __init__(self):
		message = gtk.MessageDialog(None,0,gtk.MESSAGE_INFO,gtk.BUTTONS_OK,'test')
		message.connect('destroy',lambda w:gtk.main_quit())
		message.set_markup("Sample message, could contain pango markup")
		message.show()
	def run(self):
		gtk.main()

def main():
	d = Dialog()
	d.run()


if __name__ == '__main__':
	main()
		