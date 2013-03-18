#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: server.py
Descript: 服务端
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
# 链接列表
import socket,threading
connectionList = {}

def sendMessage(msg):
	global connectionList
	for connection in connectionList.values():
		connection.send(msg)

def delConnection(item):
	global connectionList
	del connectionList['connection'+item]

class talkRoom(threading.Thread):
	def __init__(self, con,index,name):
		super(talkRoom, self).__init__()
		self.conn = con
		self.name = name
		self.index = index
		self.buffer = ''
	def run(self):
		while True:
			self.buffer = self.conn.recv(1024)
			if self.buffer == 'close':
				return
			sendMessage(str(self.index)+':'+self.buffer)
			print self.name ,'say:',self.buffer
	def __del__(self):
		print 'login out:%s'%self.name
		self.conn.close()


class server(object):
	def __init__(self):
		self.socket = None
	def run(self):
		print 'Runing server...'
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.bind(('192.168.0.198',33797))
		self.socket.listen(50)
		global connectionList
		i = 0
		while True:
			connect,address = self.socket.accept()
			username = address[0]
			connectionList['connection%d'%i] = connect
			client = talkRoom(connect,i,username)
			client.start()
			i += 1
			print '用户：',username,'登入'

	def __del__(self):
		self.socket.close()
		


def main():
	s = server()
	s.run()
	pass

if __name__ == '__main__':
	main()