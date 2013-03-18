#!/usr/bin/env python
#encoding=utf-8
import threading
import urllib2
import time
class Producer(threading.Thread):

    def __init__(self, threadname, uid):
        threading.Thread.__init__(self, name = threadname)
        self.uid = uid

    def run(self):
    	 
        sid = urllib2.urlopen('http://192.168.0.191/user.php').read()
        for rd in range(20):
	        status = urllib2.urlopen('http://192.168.0.191/test.php?sid=%s'%sid).read()
	        if status == '':
	        	print 'losses session'
	       		print status + ':' + sid
	        time.sleep(0.2)

 

# Main thread

def main():
	maxClient = 500
	for i in range(maxClient):
		producer = Producer('Producer%d'%i, i)
    	producer.start()
    

    
if __name__ == '__main__':
    main()