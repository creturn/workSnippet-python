#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class NoteBook():
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect('destroy',lambda w: gtk.main_quit())
		self.window.set_title('NoteBook Exp By:return')
		self.window.set_border_width(10)

		table = gtk.Table(3,6,False)
		#self.window.add(table)

		#create new notebook
		notebook = gtk.Notebook()
		notebook.set_tab_pos(gtk.POS_TOP)
		self.window.add(notebook)
		#table.attach(notebook,0,6,0,1)
		notebook.show()

		lb_tab = gtk.Label('Domain')
		lb_tab.show()
		lb_button = gtk.Button('This Button from page')
		lb_button.show()
		# add a new page tab
		notebook.append_page(lb_button,lb_tab)

		lb_tab_pwd = gtk.Label('Paasword')
		lb_tab_pwd.show()
		lb_inc = gtk.Label('If you can see this show you win\nif you canfand')
		lb_inc.show()
		notebook.append_page(lb_inc,lb_tab_pwd)
		table.show()
		self.window.show()
	def run(self):
		gtk.main()



def main():
	nb = NoteBook()
	nb.run()
if __name__ == '__main__':
	main()
