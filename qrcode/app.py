#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: app.py
Descript: qrcode 二维码生成和解析 需要qrencode,zbar库
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""
import qrencode
import zbar
import Image
def encode():
	# ver,size,img = qrencode.encode("学你妹的长")  #默认大小
	ver,size,img = qrencode.encode_scaled("学你妹的长",128) #指定大小
	img.save('./code.png')
def decode():
	scanner = zbar.ImageScanner()
	scanner.parse_config("enable")
	pil = Image.open('./q.png').convert('L')
	width,height = pil.size
	print 'Size:',width,height
	raw = pil.tostring()
	image = zbar.Image(width,height,'Y800',raw)
	scanner.scan(image)
	data = ''
	for symbol in image:
		data += symbol.data
	del(image)
	print data
def main():
	decode()
	
if __name__ == '__main__':
	main()