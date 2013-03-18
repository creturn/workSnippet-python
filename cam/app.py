#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: app.py
Descript: 从摄像头取图片,采用opencv库
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""

import cv

def main():
	cam = cv.CaptureFromCAM(0)
	cv.GrabFrame(cam)
	im = cv.RetrieveFrame(cam)
	cv.SaveImage('./test.jpg',im)
if __name__ == '__main__':
	main()