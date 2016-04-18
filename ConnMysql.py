__author__ = 'jinghua'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
#mysql操作

class ConnMysql:
	def __init__(self):
		#测试环境
		self.conn = pymysql.connect(host='10.10.35.201', port=3306, user='crm', passwd='crm@2015', db='crm',charset='utf8')
		#开发环境
		#self.conn = pymysql.connect(host='10.10.87.38', port=3306, user='crm', passwd='crm@2015', db='crm',charset='utf8')

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

if __name__ == '__main__':
    #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    test=ConnMysql()
    test.sqlFromFile()