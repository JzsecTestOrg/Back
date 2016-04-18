__author__ = 'jinghua'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import time
import random

#mysql操作
class ConnMysql:
	def __init__(self):
		#测试环境
		#self.conn = pymysql.connect(host='10.10.35.201', port=3306, user='crm', passwd='crm@2015', db='crm',charset='utf8')
		#开发环境
		self.conn = pymysql.connect(host='10.10.87.38', port=3306, user='crm', passwd='crm@2015', db='crm',charset='utf8')

		#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
	def readFile(self):
		f=open(".\sql.txt",'r')
		alllines=f.readlines()
		f.close
		return([elem for elem in alllines if "#" not in elem])
		#sql=[elem for elem in alllines if "#" not in elem]
		#bprint(sql)
		#for eachline in alllines:
			#print(eachline)
	#插入im_user_relation

		
	def sqlFromFile(self):
		cur = self.conn.cursor()
		for eachline in self.readFile():
			cur.execute(eachline)
			print(eachline)
		# print cur.description	
		# r = cur.fetchall()
		 #print r
		# ...or...
		for r in cur:
			print(r)

		cur.close()
		self.conn.commit()
		self.conn.close()

	def sqlExecutive(self,sql):
		cur = self.conn.cursor()
		cur.execute(sql)
		print(sql)
		# print cur.description	
		# r = cur.fetchall()
		 #print r
		# ...or...
		for r in cur:
			print(r)

		cur.close()
		self.conn.commit()
		self.conn.close()


class File: 
	def writeFile(self,input,type=None):
		#打开模式列表：
		#w      以写方式打开，
		#a      以追加模式打开 (从 EOF 开始, 必要时创建新文件)
		#r+     以读写模式打开
		#w+     以读写模式打开 (参见 w )
		#a+     以读写模式打开 (参见 a )
		#rb     以二进制读模式打开
		#wb     以二进制写模式打开 (参见 w )
		#ab     以二进制追加模式打开 (参见 a )
		#rb+    以二进制读写模式打开 (参见 r+ )
		#wb+    以二进制读写模式打开 (参见 w+ )
		#ab+    以二进制读写模式打开 (参见 a+ )
		try:
			f = open('tpm.txt', 'a+')
			#for i in range(10):
			#	f.write(time.strftime('%Y-%m-%d %H:%M:%S'))
			#	f.write(' ' + str(random.randint(0, i)) + '\n')
			f.write(' ' + str(input) + '\n')
			f.close()
		except Exception as e:
			print(e)

	def readFile(self,returnvalue=None):
		try:
			f = open('tpm.txt')
			# read方式读取
			s = f.read()
			#print(s, '\n\n\n')
			#print(f.tell())
			#上面读取完后指针移动到最后，通过seek将文件指针移动到文件头
			f.seek(0)
			#使用readline每次读取一行
			alllines=f.readlines()
			#while(True):
			#	line = f.readline()
			#	print(line)
			#	if(len(line) == 0):
			#		break
			f.close()
			if returnvalue is "file":
				return(s)
			else:
				return([elem for elem in alllines])
		except Exception as e:
			print(e)

class SimpleFunc:
	"""docstring for"""
	def getDictKey(self,inputdict):
		listtmp=[]
		for key in inputdict:
			#print("key=%s , value=%s" % (key, inputdict[key]))
			listtmp.append(key)
			#print(inputdict["results"])
			#self.getDictKey(list(inputdict[key]).pop())
			#print(list)
		return(listtmp)
		

if __name__ == '__main__':
    #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    #test=ConnMysql()
    #test.sqlFromFile()
    list1=['2016-02-25 16:30:54 0\n', '2016-02-25 16:30:54 1\n', '2016-02-25 16:30:54 2\n', '2016-02-25 16:30:54 3\n']
    list2=['2017-02-25 16:30:54 0\n', '2016-02-25 16:30:54 1\n', '2016-02-25 16:30:54 2\n', '2016-02-25 16:30:54 3\n']
    test=File()
    test.writeFile(list1)
    print(test.readFile())
    #print(test.readFile())
    