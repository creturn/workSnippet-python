#!/usr/bin/env python
#coding: utf-8 

import PIL.Image as Image
import os
class ImageUtil:
	def __init__(self,scenepath):
		# 小图宽度
		self.sizeX           = 300
		# 小图高度
		self.sizeY           = 300
		# 高度有多少行
		self.sizeH           = 0
		# 高度有多少列
		self.sizeW           = 0
		#拼接图片存放位置
		self.imageDirPath    = ''
		# 拼接后图片的总宽度
		self.toImageWidth    = 0
		# 拼接后图片的总高度
		self.toImageHeight   = 0
		# 拼接图片后存放的位置
		self.toImageSavePath = ''
		self.scenePath       = scenepath
		self.scenes          = []
	# 获取需要转换成大图的图片大小
	def getToImageSize(self):
		tmpX = []
		tmpY = []
		imgList = os.listdir(self.imageDirPath)
		tmpList = []
		# 过滤出目标文件
		for img in imgList:
			if img.find('pic') == 0:
				# 分割文件名
				tmpList.append(img.replace('pic','').replace('.jpg','').split('_')) 
		if len(tmpList) > 0:
			# 计算行和列
			for size in tmpList:
				tmpX.append(int(size[0]))
				tmpY.append(int(size[1]))
			self.sizeH = max(tmpY) + 1
			self.sizeW = max(tmpX) + 1
			print "当前地图有: %d行,%d列"%(self.sizeW,self.sizeH)
			# 计算目标大图长宽
			self.toImageWidth  = self.sizeX * self.sizeW 
			self.toImageHeight = self.sizeY * self.sizeH
			print "原图大小： %s X %s"%(self.toImageWidth,self.toImageHeight)
			self.convert()
		return self
	# 开始转换
	def convert(self):
		toImage = Image.new('RGBA',(self.toImageWidth,self.toImageHeight))
		for y in xrange(0,self.sizeH):
			for x in xrange(0,self.sizeW):
				fname = 'pic%s_%s.jpg'%(x,y)
				fname = self.imageDirPath + '/' + fname
				try:
					fromImage = Image.open(fname)
					toImage.paste(fromImage,(x*self.sizeX,y*self.sizeY))
				except :
					print "出错啦：" + fname
		toImage.save(self.toImageSavePath)
		print "保存在：" + self.toImageSavePath
	# 获取场景文件数和目录
	def getScene(self):
		sceneList = os.listdir(self.scenePath)
		tmpList = []
		for d in sceneList:
			if os.path.isdir(self.scenePath + "/" +d):
				if os.path.isdir(self.scenePath + "/" + d + "/front"):
					tmpList.append(d)
		print "找到场景：%d个"%(len(tmpList))
		self.scenes = tmpList
		return self
	# 批量转换场景
	def convertScenes(self):
		for s in self.scenes:
			print "正在转换场景:" + s
			self.imageDirPath = self.scenePath + "/" + s + '/front'
			self.toImageSavePath = self.scenePath + "/" + s + "/" + s + ".jpg"
			self.getToImageSize()
		
		
def main():
	path = './scene'
	imgUtl = ImageUtil(path)
	imgUtl.getScene().convertScenes()


if __name__ == '__main__':
	main()