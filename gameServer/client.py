#!/usr/bin/env python2.7
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: client.py
Descript: 游戏客户端模拟
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""

import socket,stackless
sockIndex = 1
def connToServer ():
    global sockIndex
    #创建一个socket连接到127.0.0.1:5200，并发送内容
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 5200))
    conn.send("hi,I'm NO."+ str(sockIndex))
    print sockIndex
    sockIndex = sockIndex + 1
    while True:
        #等待服务端返回数据，并输出
        rev = conn.recv(1024)
        print 'get server msg:' + str(rev)
        stackless.schedule()
	    
#先来500个并发试试
for i in range(0,500):
    stackless.tasklet(connToServer)()
stackless.run()