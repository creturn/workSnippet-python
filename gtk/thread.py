#!/usr/bin/env python
import threading
import time
import gobject
import gtk
gobject.threads_init()
class myThread(threading.Thread):
	def __init__(self, widgit):
		super(myThread, self).__init__()
		self.widgit = widgit
		self.quit = False
	def run(self):
		count = 0
		while not self.quit:
			print 'run num:%d'%count
			count += 1
			gobject.idle_add(self.updateLab, count)
			time.sleep(1)
	def updateLab(self,num):
		self.widgit.set_text('this is Num:%d'%num)
		return False


def main():
	w = gtk.Window()
	l = gtk.Label('test')
	w.add(l)
	w.show_all()
	w.connect("destroy", lambda _: gtk.main_quit())
	t = myThread(l)
	t.start()
	gtk.main()	
	t.quit = True

if __name__ == '__main__':
	main()