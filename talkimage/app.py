#!/usr/bin/env python 
#coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk
import os
import xlwt
class MessageBox(object):
	def __init__(self):
		pass
	def showMsg(self,msg = '',title='信息提示'):
		msgBox = gtk.MessageDialog(None,gtk.DIALOG_DESTROY_WITH_PARENT,gtk.MESSAGE_INFO,gtk.BUTTONS_OK,title)
		msgBox.format_secondary_text(msg)
		msgBox.run()
		msgBox.destroy()

class TalkImageApp(gtk.Window):
	def __init__(self):
		super(TalkImageApp, self).__init__()
		self.prefixName = ''
		self.snum = 0
		self.initUI()
		self.initEvent()
	def initUI(self):
		self.set_title('TalkImage APP')
		# self.set_size_request(300,200)
		self.vbox = gtk.VBox()
		self.hbox = gtk.HBox()
		self.lab_prefix = gtk.Label('前缀: ')
		self.txt_prefix = gtk.Entry()
		self.hbox_prefix = gtk.HBox()
		self.hbox_prefix.pack_start(self.lab_prefix)
		self.hbox_prefix.pack_start(self.txt_prefix)
		self.vbox.pack_start(self.hbox_prefix)

		self.lab_snum = gtk.Label('编号: ')
		self.txt_snum = gtk.Entry()
		self.hbox_snum = gtk.HBox()
		self.hbox_snum.pack_start(self.lab_snum)
		self.hbox_snum.pack_start(self.txt_snum)
		self.vbox.pack_start(self.hbox_snum)

		self.lab_dirname = gtk.Label('目录: ')
		self.btn_dirname = gtk.FileChooserButton('选择将要转换目录')
		# 设置只选择目录
		self.btn_dirname.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
		self.hbox_dirname = gtk.HBox()
		self.hbox_dirname.pack_start(self.lab_dirname)
		self.hbox_dirname.pack_start(self.btn_dirname)
		self.vbox.pack_start(self.hbox_dirname)
		self.lab_filenum = gtk.Label("")
		self.vbox.pack_start(self.lab_filenum)
		self.btn_conver = gtk.Button("转换 ")
		self.vbox.pack_start(self.btn_conver)	
		self.add(self.vbox)
		self.show_all()
	def initEvent(self):
		self.connect('destroy', lambda w: gtk.main_quit())
		self.btn_conver.connect('clicked',self.btn_conver_handler)	
	#转换按钮点击事件
	def btn_conver_handler(self,widget,data=None):
		# 前缀
		prefix = self.txt_prefix.get_text()
		# 起始编号
		snum = self.txt_snum.get_text()
		# 获取当前选择的目录名，如果选择了则
		dirname = self.btn_dirname.get_filename() 
		if prefix != '' and snum != '' and dirname != None:
			self.prefixName = prefix
			self.snum = snum
			self.multDirScaner(dirname)
		else:
			msg = MessageBox()
			msg.showMsg('前缀，编号和目录不能为空！')
	def multDirScaner(self,dirname):
		self.getDirFileList(dirname + '/' + 'big')
		self.getDirFileList(dirname + '/' + 'mid')
		self.getDirFileList(dirname + '/' + 'sml')
		msg = MessageBox()
		msg.showMsg('图片已经转换完成！')
	def getDirFileList(self,dirname):
		#解决中文目录出错问题
		dirname = unicode(dirname,'utf8')
		try:
			fileList = os.listdir(dirname)
			if len(fileList) > 0:
				xlsFile = xlwt.Workbook()
				xlsFileTable = xlsFile.add_sheet(u'新旧参照表')
				xlsFileTable.write(0,0,u'原始文件名')
				xlsFileTable.write(0,1,u'新建文件名')
				snum = int(self.snum)
				columnNum = 1
				for f in fileList:
					if os.path.splitext(f.lower())[1] == '.jpg':
						#转换文件名
						# newName = self.prefixName + '_' + snum
						newName = '%s/%s_%d.jpg'%(dirname,self.prefixName,snum)
						oldName = '%s/%s'%(dirname,f)
						xlsFileTable.write(columnNum,1,'%s_%d.jpg'%(self.prefixName,snum))
						xlsFileTable.write(columnNum,0,f)
						os.rename(oldName,newName)
						snum = snum + 1
						columnNum = columnNum + 1
				xlsFile.save('%s/canzhaobiao.xls'%dirname)
		except:
			msg = MessageBox()
			msg.showMsg('%s文件夹不存在，或者无法访问!'%dirname)
	def run(self):
		gtk.main()



def main():
	app = TalkImageApp()
	app.run()

if __name__ == '__main__':
	main()
		