#!/usr/bin/env python
#coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk
import pymongo,time

class BaseTreeView:
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title('sample')
		self.window.set_size_request(200,300)
		self.window.connect('destroy',lambda w:gtk.main_quit())


		#create tree
		self.treestore = gtk.TreeStore(str,str)
		con = pymongo.Connection('127.0.0.1',27017)
		db = con.hsxy_dev
		dbList = db.base_goods.find().limit(20)
		for i in dbList:
			# print i
			piter = self.treestore.append(None,[i['goods_name'],i['sell_price']])
		# for parent in range(4):
		# 	piter = self.treestore.append(None,['parent %i' % parent])
		# 	for child in range(3):
		# 		#self.treestore.append(piter,['child %i of parent %i' % (child, parent)])
		# 		pass

			

		#create a treeView use the tree TreeStore
		self.treeView  = gtk.TreeView(self.treestore)

		#create TreeVIewColumn to display the data
		self.tvcolumn = gtk.TreeViewColumn('装备名称')
		self.tvcolumn2 = gtk.TreeViewColumn('装备价格')

		#add tvcolumn to treeView

		self.treeView.append_column(self.tvcolumn)
		self.treeView.append_column(self.tvcolumn2)

		#create a cellRendererText to Render the data
		self.cell = gtk.CellRendererText()
		self.cell2 = gtk.CellRendererText()
		#add the cell to the tvcolumn adn allow it to expnad
		self.tvcolumn.pack_start(self.cell,True)
		self.tvcolumn2.pack_start(self.cell2,True)
		self.tvcolumn.add_attribute(self.cell,'text',0)
		self.tvcolumn2.add_attribute(self.cell2,'text',1)
		#make it searchable
		self.treeView.set_search_column(0)

		#allow sorting on the column
		self.tvcolumn.set_sort_column_id(0)
		#allow drag and drop reordering of rows
		self.treeView.set_reorderable(True)
		self.window.add(self.treeView)
		self.window.show_all()
		# dbListNews = db.base_goods.find().sort('goods_id').limit(10)
		# for goods in dbListNews:
		# 	self.treestore.append(None,[goods['goods_name']])
		# 	time.sleep(1)

def main():
	gtk.main()
if __name__ == '__main__':
	tv = BaseTreeView()
	main()