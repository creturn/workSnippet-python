#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class EventBox():
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title('Event Box By: return')
		window.connect('destroy',lambda w: gtk.main_quit())
		window.set_border_width(10)


		event_box = gtk.EventBox()
		window.add(event_box)
		event_box.show()

		label = gtk.Label('Click here to quit,quit,quit')
		event_box.add(label)
		label.show()

		label.set_size_request(110,20)
		event_box.set_events(gtk.gdk.BUTTON_PRESS_MASK)
		event_box.connect('button_press_event',lambda w,e:gtk.main_quit())
		event_box.realize()
		event_box.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND1))
		event_box.modify_bg(gtk.STATE_NORMAL,event_box.get_colormap().alloc_color('green'))
		window.show()

def main():
	gtk.main()
	return 0

if __name__ == '__main__':
	EventBox()
	main()