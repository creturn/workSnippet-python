#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: test.py
Descript: test
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
import webkit
import gtk
view = webkit.WebView()
view.open('http://www.baidu.com')
view.set_size_request(680,400)
view.get_settings().set_property('enable-plugins',False)
view.get_settings().set_property('enable-developer-extras',False)
view.get_settings().set_property('enable-default-context-menu',False)
win = gtk.Window()
win.connect('destroy',lambda w: gtk.main_quit)
win.add(view)
win.show_all()
gtk.main()