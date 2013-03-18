#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

#Convenience functions

def make_menu_item(name, callback, data=None):
	item = gtk.MenuItem(name)
	item.connect('activate',callback,data)
	item.show()
	return item

def scale_set_default_values(scale):
	scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
	scale.set_digits(1)
	scale.set_value_pos(gtk.POS_TOP)
	scale.set_draw_value(True)

class RangeWidgets():
	def cb_pos_menu_select(self,item,pos):
		self.hscale.set_value_pos(pos)
		self.vscale.set_value_pos(pos)
	def cb_update_menu_select(self,item,policy):
		self.hscale.set_update_policy(policy)
		self.vscale.set_update_policy(policy)
	def cb_digits_scale(self,adj):
		self.hscale.set_digits(adj.value)
		self.vscale.set_digits(adj.value)
	def cb_page_size(self,get,set):
		set.page_size = get.value
		set.page_incr = get.value
		set.emit('changed')
	def cb_draw_value(self,button):
		self.hscale.set_draw_value(button.get_active())
		self.vscale.set_draw_value(button.get_active())


	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)		
		self.window.connect('destroy',lambda w: gtk.main_quit())
		self.window.set_title('Range Contrals Exp By: return')
		#self.window.set_default_size(400,600)
		box1 = gtk.VBox(False,0)
		self.window.add(box1)
		box1.show()

		box2 = gtk.HBox(False, 10)
		box2.set_border_width(10)
		box1.pack_start(box2,True,True,0)
		box2.show()

		adj1 = gtk.Adjustment(0.0,0.0,101.0,0.1,1.0,1.0)
		self.vscale = gtk.VScale(adj1)
		scale_set_default_values(self.vscale)
		box2.pack_start(self.vscale,True,True,0)
		self.vscale.show()

		self.window.show()

def main():
	gtk.main()
	return 0

if __name__ == '__main__':
	RangeWidgets()
	main()