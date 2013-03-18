#! /usr/bin/env python
#coding: utf-8

# By: return  blog:www.creturn.com Date: 2012.10.31 

import socket, sys,string
from struct import *

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr(a):
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b
#out put info
def showPacket(s,s_ip='',s_port='',d_ip='',d_port=''):
	if not (int(s_port) > 8000 and int(s_port) < 9000):
		pass
	else:
		if len(s):
			#print s
			print 'IP:' + s_ip + ':' + s_port + ' > ' + d_ip + ':' + d_port
			print 'Packet Data Len:%d'%(len(s))
			showGameProtol(s[4:6])
			showHex(s)
#show Game Protocol
def showGameProtol(s):
	gp_num = unpack('!H',s)
	print 'Game Protocal Num:%d'%(gp_num[0])
#out put hex data
def showHex(s):
	print 'Data:'
	out = []
	for i in s:
		 rs = unpack('!B',i)
		 rs = '%.2x'%(rs[0])
		 out.append(rs)
	if len(out) > 16 :
		for i in xrange(0,len(out)/16):
			print string.join(out[i*16:(i*16)+16],' ')
	else:
		print string.join(out,' ')

#out put info
def sniffer():
	#create a AF_PACKET type raw socket (thats basically packet level)
	#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
	try:
		s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
	except socket.error , msg:
		print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		s.close()
		sys.exit()

	# receive a packet
	try:
		while True:
			packet = s.recvfrom(65565)

			#packet string from tuple
			packet = packet[0]
			
			#parse ethernet header
			eth_length = 14
			
			eth_header = packet[:eth_length]
			eth = unpack('!6s6sH' , eth_header)
			eth_protocol = socket.ntohs(eth[2])
 
			#Parse IP packets, IP Protocol number = 8
			if eth_protocol == 8 :
				#Parse IP header
				#take first 20 characters for the ip header
				ip_header = packet[eth_length:20+eth_length]
				
				#now unpack them :)
				iph = unpack('!BBHHHBBH4s4s' , ip_header)

				version_ihl = iph[0]
				version = version_ihl >> 4
				ihl = version_ihl & 0xF

				iph_length = ihl * 4

				ttl = iph[5]
				protocol = iph[6]
				s_addr = socket.inet_ntoa(iph[8]);
				d_addr = socket.inet_ntoa(iph[9]);
				
				if d_addr != '127.0.0.1' and s_addr != '127.0.0.1':
					continue
				#print s_addr + '>' + d_addr
				
				#TCP protocol
				if protocol == 6 :
					t = iph_length + eth_length
					tcp_header = packet[t:t+20]

					#now unpack them :)
					tcph = unpack('!HHLLBBHHH' , tcp_header)
					
					source_port = tcph[0]
					dest_port = tcph[1]
					sequence = tcph[2]
					acknowledgement = tcph[3]
					doff_reserved = tcph[4]
					tcph_length = doff_reserved >> 4
					
					h_size = eth_length + iph_length + tcph_length * 4
					data_size = len(packet) - h_size
					
					#get data from the packet
					data = packet[h_size:]
					
					showPacket(data,str(s_addr),str(source_port),str(d_addr),str(dest_port))

				#ICMP Packets
				elif protocol == 1 :
					u = iph_length + eth_length
					icmph_length = 4
					icmp_header = packet[u:u+4]

					#now unpack them :)
					icmph = unpack('!BBH' , icmp_header)
					
					icmp_type = icmph[0]
					code = icmph[1]
					checksum = icmph[2]
					
					#print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)
					
					h_size = eth_length + iph_length + icmph_length
					data_size = len(packet) - h_size
					
					#get data from the packet
					data = packet[h_size:]
					
					showPacket(data,str(s_addr),str(source_port),str(d_addr),str(dest_port))

				#UDP packets
				elif protocol == 17 :
					u = iph_length + eth_length
					udph_length = 8
					udp_header = packet[u:u+8]

					#now unpack them :)
					udph = unpack('!HHHH' , udp_header)
					
					source_port = udph[0]
					dest_port = udph[1]
					length = udph[2]
					checksum = udph[3]
					
					
					h_size = eth_length + iph_length + udph_length
					data_size = len(packet) - h_size
					
					#get data from the packet
					data = packet[h_size:]
					
					showPacket(data,str(s_addr),str(source_port),str(d_addr),str(dest_port))


				#some other IP packet like IGMP
				else :
					print 'Protocol other than TCP/UDP/ICMP'
					s.close()
	except KeyboardInterrupt:
		print 'close sniffer'
		

def main():
	sniffer()

if __name__ == '__main__':
	main()
