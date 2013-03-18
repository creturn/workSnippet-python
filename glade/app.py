#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: app.py
Descript: glade UI test
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
import pygtk
pygtk.require("2.0")
import gtk
def main():
	builder = gtk.Builder()
	builder.add_from_file('ui/new.glade')
	builder.connect_signals({'on_window_destroy':gtk.main_quit})
	win = builder.get_object('window')
	win.show()
	gtk.main()
if __name__ == '__main__':
	main()
