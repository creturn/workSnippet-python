#!/usr/bin/env python
#coding: utf-8 
#Autor: return Blog:www.creturn.com Date:2012.11.11
import gtk,urllib
from xml.dom import minidom
def init():
	global bufferText 
	global inputText
	win = gtk.Window()
	win.set_title('我的词典')
	win.connect('destroy',lambda w:gtk.main_quit())
	inputText = gtk.Entry()
	findBtn = gtk.Button('查询')
	viewText = gtk.TextView()
	inputText.connect('key-press-event',bindingKeys)
	hbox = gtk.HBox()
	vbox = gtk.VBox()
	scroll = gtk.ScrolledWindow()
	scroll.add(viewText)
	bufferText = gtk.TextBuffer()
	findBtn.connect('clicked',findWordEvent)
	viewText.set_buffer(bufferText)
	viewText.set_size_request(200,200)
	viewText.set_wrap_mode(gtk.WRAP_WORD_CHAR)
	hbox.set_size_request(200,30)
	hbox.pack_start(inputText,False)
	hbox.pack_start(findBtn,False)
	vbox.pack_start(hbox)
	vbox.pack_start(scroll)
	win.add(vbox)
	win.show_all()
	gtk.main()
def bindingKeys(widget,keyval):
		# print keyval
		if keyval.keyval == 65293:
			findWordEvent(None, None)

	 
def findWordEvent(widget,data=None):
	bufferText.set_text('正在查询...')
	word = inputText.get_text()
	xml = get_word_translate(word)
	bufferText.set_text('')
	doc = minidom.parseString(xml)
	dicList = doc.getElementsByTagName('acceptation')
	if len(dicList):
		for dic in dicList:
			bufferText.insert_at_cursor(dic.childNodes[0].nodeValue)
	else:
		bufferText.insert_at_cursor('查无此词')
def get_word_translate(word):
	urlApi = 'http://dict-co.iciba.com/api/dictionary.php?w=%s'%word
	result = urllib.urlopen(urlApi).read()
	return result
def main():
	init()
if __name__ == '__main__':
	main()
