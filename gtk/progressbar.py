#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

def progress_timeout(pbobj):
	if pbobj.activity_check.get_active():
		pbobj.pbar.pulse()
	else:
		new_valu = pbobj.pbar.get_fraction()+0.01
		if new_valu > 1.0:
			new_valu = 0.0
		pbobj.pbar.set_fraction(new_valu)
	return True

class ProgressBar():
	def toggle_show_text(self, widget, data=None):
		if widget.get_active():
			self.pbar.set_text('Some Text')
		else:
			self.pbar.set_text('')
	def toggle_activity_mode(self, widget, data=None):
		if widget.get_active():
			self.pbar.pulse()
		else:
			self.pbar.set_fraction(0.0)
	def toggle_orientation(self,widget,data=None):
		if self.pbar.get_orientation() == gtk.PROGRESS_LEFT_TO_RIGHT:
			self.pbar.set_orientation(gtk.PROGRESS_RIGHT_TO_LEFT)
		elif self.pbar.get_orientation() == gtk.PROGRESS_RIGHT_TO_LEFT:
			self.pbar.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
	def destroy_progress(self,widget,data=None):
		object.source_remove(self.timer)
		self.timer = 0
		gtk.main_quit()

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_resizable(True)

		self.window.connect('destory',self.destroy_progress)
		self.window.set_title('ProgressBar Exp By:return')
		self.window.set_border_width(0)
		vbox = gtk.VBox(False,5)
		vbox.set_border_width(10)
		self.window.add(vbox)
		vbox.show()

		align = gtk.Alignment(0.5,0.5,0,0)
		vbox.pack_start(align,False,False,5)
		align.show()

		self.pbar = gtk.ProgressBar()
		align.add(self.pbar)
		self.pbar.show()
		self.window.show()


def main():
	gtk.main()
	return 0

if __name__ == '__main__':
	main()
			