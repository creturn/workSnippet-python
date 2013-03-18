#coding: utf-8

###########################################
#	机器人类，模拟游戏中的人物进行游戏测试
###########################################
import socket
import struct
import time
import hashlib
serverStatus 	= {'1':'顺畅','2':'正常','3':'繁忙','4':'爆满'}
loginStatus 	= {'0':'登录失败','1':'登录成功','2':'登录失败，防沉迷'}

class robot:

	#初始化操作
	def __init__(self):
		self.ctString = '小日本是中国的，苍井空是世界的！'
		self.showMsg('Robot Init:')
		self.host = '127.0.0.1'			#网关地址
		self.port = 8777					#网关端口
		self.init_socket()
	#初始化socket连接
	def init_socket(self):
		self.showMsg('Init Socket')
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.host, self.port))

	#向网关发起请求，获取游戏服务器地址
	def getGameServer(self):
		Cmd = 60010	
		sendPackInfo = self.pack(Cmd,'')
		self.sendPack(sendPackInfo)
		rs = self.recvPack()
		packHead = rs[0:6]	#包头
		packBody = rs[6:]	#包体
		self.showMsg('PackLen:')
		self.showMsg(struct.unpack('!I',packHead[0:4]))
		self.showMsg('Cmd:')
		self.showMsg(struct.unpack('!H',packHead[4:6]))
		self.showMsg('分线号：')
		self.showMsg(struct.unpack('B',packBody[2:3]))
		self.showMsg('IP地址：')
		ipLen = struct.unpack('!H',packBody[3:5])
		ipLen = ipLen[0]+5
		ipaddress = struct.unpack(str(ipLen-5)+'s',packBody[5:ipLen])
		ipaddress = ipaddress[0]
		self.showMsg(ipaddress)
		self.showMsg('Port:')
		ipPort = struct.unpack('!H',packBody[ipLen:ipLen+2])
		ipPort = ipPort[0]
		self.showMsg(ipPort)
		self.showMsg('状态：')
		status = struct.unpack('!B',packBody[ipLen+2:ipLen+3])
		status = status[0]
		self.showMsg(serverStatus[str(status)])
		self.showMsg('在线人数：')
		pnum = struct.unpack('!H',packBody[ipLen+3:ipLen+5])
		self.showMsg(pnum[0])
		return ipaddress,ipPort

	def loginGame(self):
		# 协议号:10000	登录
		# c >> s:
		#     int:16 服务器标识
		#     int:32 平台用户ID
		#     int:32 unix时间戳
		#     string 平台用户账号
		#     string ticket 	

		ServerInfo = self.getGameServer()
		Cmd          = 10000
		Accid        = 16
		AccName      = 'return001'
		nowTime      = time.time()
		TicketSub    = 'SDFSDESF123DFSDF'
		TicketStr    = str(Accid)+AccName+str(nowTime)+TicketSub
		TicketStrMd5 =  self.md5(TicketStr)	#md5(accid+accname+nowtime+safeCode)
		PackBody     = str(struct.pack('!H',1))		#服务器标识
		PackBody     = PackBody + str(struct.pack('!I',Accid))
		PackBody     = PackBody + str(struct.pack('!I',nowTime))

		PackBody     = PackBody + str(self.packString(str(AccName)))
		PackBody     = PackBody + str(self.packString(TicketStrMd5))
		sendPackInfo = self.pack(Cmd,PackBody)
		self.converServer(ServerInfo[0],ServerInfo[1])		#切换服务器
		self.sendPack(sendPackInfo)							#发送服务器数据包
		rs = self.recvPack()								#接收数据包
		# s >> c:		登录反馈信息
		#     int:16 
		#         0 => 失败 
		#         1 => 成功
		#         2 => 失败 - 离线时间还没超过5小时（防沉迷）
		#     int:32 系统时间戳
		#     int:16 循环次数
		#     array(
		# 	int:32 角色ID
		# 	int:16 状态   (玩家状态: 0正常、1禁止)
		# 	int:16部落
		# 	int:16 职业
		# 	int:16 性别
		# 	int:16 等级
		# 	string 名字
		head = rs[0:6]
		body = rs[6:]
		self.showMsg(loginStatus[str(self.getStr(struct.unpack('!H',body[0:2])))])	#登录状态
		sTime = time.localtime(self.getStr(struct.unpack('!I',body[2:6])))
		self.showMsg('服务器时间：'+time.strftime('%Y-%m-%d %H:%M:%S',sTime))
		self.showMsg('重复次数：'+str(self.getStr(struct.unpack('!H',body[6:8]))))
		self.showMsg('角色ID:'+str(self.getStr(struct.unpack('!I',body[8:12]))))
		self.showMsg('状态:'+str(self.getStr(struct.unpack('!H',body[12:14]))))
		self.showMsg('部落:'+str(self.getStr(struct.unpack('!H',body[14:16]))))
		self.showMsg('职业:'+str(self.getStr(struct.unpack('!H',body[16:18]))))
		self.showMsg('性别:'+str(self.getStr(struct.unpack('!H',body[18:20]))))
		self.showMsg('等级:'+str(self.getStr(struct.unpack('!H',body[20:22]))))
		self.showMsg('名字:'+body[24:24+self.getStr(struct.unpack('!H',body[22:24]))])
		####################################
		#选择角色进入
		self.entryRoles(1,self.getStr(struct.unpack('!I',body[8:12])))
		self.loopDoAction()
	#选择角色进入游戏
	def entryRoles(self,sn,roleid):
		Cmd = 10004
  		# 协议号:10004
		# c >> s:
		#     int:16 服务器标识
		#     int:32 角色ID
		sendPackInfo = struct.pack('!H',sn)
		sendPackInfo = str(sendPackInfo) + str(struct.pack('!I',roleid))
		sendPackInfo = self.pack(Cmd,sendPackInfo)
		self.sendPack(sendPackInfo)
		rs = self.recvPack()
		pass
	#获取玩家信息
	def getUserInfo(self):
		Cmd = 13001
		sendPackInfo = self.pack(Cmd,'')
		self.sendPack(sendPackInfo)
		rs = self.recvPack()
	#发送心跳包
	def sendHeart(self):
		Cmd = 10006
		sendPackInfo = struct.pack('!I',time.time())
		sendPackInfo = self.pack(Cmd,sendPackInfo)
		self.sendPack(sendPackInfo)
		self.recvPack()
		pass
	#处理登入后做的动作
	def loopDoAction(self):
		self.chart()		#聊天喊话
		pass
	#聊天
	def chart(self):
		Cmd = 11010
		#ctString = '小日本是中国的，苍井空是世界的！'
		sendPackInfo = self.packString(self.ctString)
		sendPackInfo = self.pack(Cmd,sendPackInfo)
		self.sendPack(sendPackInfo)
		self.recvPack()
		pass

	#跳转连接新的服务器
	def converServer(self,ipaddress,ipPort):
		self.socket.close()
		self.host = ipaddress
		self.port = ipPort
		self.init_socket()
		pass
	#md5加密信息
	def md5(self,stringMd5):
		return hashlib.md5(stringMd5).hexdigest()
	#解包数据
	def unpack(self,rePack):
		packHead = rePack[0:6]	#取包头
		packBody = rePack[6:]	#取包内容
	#打包字符串
	def packString(self,pStr):
		plen  = len(pStr)
		pPack = struct.pack(str(plen) + 's',pStr)
		pPack = struct.pack('!H',len(pPack)) + pPack
		return pPack
	#打包数据
	def pack(self,cmd,data):
		packLen = len(data)+6
		pack = struct.pack('!I',packLen)+struct.pack('!H',cmd)
		if len(data) > 0:
			pack = pack+data
		return pack
	#发送数据包
	def sendPack(self,packInfo):
		self.showMsg('send Pack Info ..')
		if len(packInfo):
			self.socket.send(packInfo)
	#接收数据包
	def recvPack(self):
		return self.socket.recv(1024)
	#取数组或者列表第N个数据
	def getStr(self,strs, getnum = 0):
		return strs[getnum] 
	#析构函数，用于释放socket连接
	def __del__(self):
		self.showMsg('Close The Socket')
		self.socket.close()
	def showMsg(self,msg,out=None):
		print msg
		pass

def getRobot():
	return robot()
#入口函数
		
def main():
	rb = robot()
	rb.loginGame()


if __name__ == '__main__':
	main()