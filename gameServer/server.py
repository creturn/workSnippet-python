#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: server.py
Descript: 游戏服务端处理
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
from twisted.internet import epollreactor
epollreactor.install()
    
from twisted.internet.protocol import Factory,Protocol
from twisted.internet import reactor
class gameSocket(Protocol):
    #有新用户连接至服务器
    def connectionMade(self):
        print 'New Client'
    
    #客户端断开连接
    def connectionLost(self,reason):
        print 'Lost Client'
    
    #收到客户端发送数据
    def dataReceived(self, data):
        print 'Get data:' + str(data)
        #向该客户端发送数据
        self.transport.write('bingo!i got your msg:'+ str(data))
if __name__=='__main__':
    f = Factory()
    f.protocol = gameSocket
    reactor.listenTCP(5200,f)
    print 'server started...'
    reactor.run()