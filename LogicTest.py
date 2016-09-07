__author__ = 'jinghua'
# -*- coding: utf-8 -*-
import logging,os,sys,datetime
import xlrd,xlwt,json,requests
from InterfaceTests import InterfaceTests
from Common import *
from xlrd import open_workbook
from xlutils.copy import copy
from TradeTest import *
import pymysql

class LogicTest:
    def __init__(self):
        #    self.testCaseFile=None
        self.appVer='184'
        self.cappver='184'
        test=InterfaceTests()
        #userId=test.get_login_userId()
        returnparams=test.get_login_token('bapp')
        self.bapptoken=returnparams['bapptoken']
        self.client_id=test.returnparams['client_id']
        self.userId=test.returnparams['userId']
        print(self.userId)
        returnparams=test.get_login_token('capp')
        self.capptoken=returnparams['capptoken']
        self.cappuserId=returnparams['cappuserId']
        self.cappclient_id=returnparams['cappclient_id']
        print(self.bapptoken)
        returnparams=test.get_login_token('account')
        self.accountJsessionid=returnparams['jsessionid']
        self.accountUser_id=returnparams['user_id']
        print(self.accountJsessionid)
        print(self.accountUser_id)
        #取交易sesionid
        session=requests.Session()
        tradetest=TradeTest()
        self.sessionid=tradetest.login(session)
        print(self.sessionid)
        self.conn = pymysql.connect(host='10.10.183.173', port=3306, user='jinghua', passwd='jzzq_jinghua', db='xiaomitv',charset='utf8')


    def logRecord(self):
        log_file = os.path.join(os.getcwd(),'log/sas.log')
        log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
        logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(log_format)
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)



    def interfaceTest(self, num, api_module, api_purpose, api_host, request_url,request_data,check_point,request_method,request_data_type,api_client,s=None):
         headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                          'X-Requested-With' : 'XMLHttpRequest',
                          'Connection' : 'keep-alive',
                          'Referer' : 'http://' + api_host,
                          'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
                    }
         #根据不同的客户端替换掉不同的参数
         if request_data_type=="json":
             temp=json.loads(request_data)
             if api_client=="CAPP":
                 #print(request_data)
                 temp["appVer"]=self.cappver
                 temp["token"]=self.capptoken
                 temp["userId"]=self.cappuserId
                 temp["client_id"]=self.cappclient_id
                 temp["sessionid"]=self.sessionid
                 temp["cusid"]="81106500034"
                 #print(temp)

             elif api_client=="IM":
                 temp["appVer"]=self.appVer
                 temp["token"]=self.bapptoken
                 temp["userId"]=self.userId
                 temp["client_id"]=self.client_id
             request_data=json.dumps(temp)

         elif request_data_type=="dict":
             newlist=[]
             newdict={}
             #print(request_data)
             #print(request_data.split("&"))
             temp1=request_data.split("&")
             for i in range(len(temp1)):
                 newlist.append(temp1[i].split("="))
             #print(newlist)
             for i in newlist:
                 newdict[i[0]] = i[1]
             if api_client=="ACCOUNT":
                 newdict["jsessionid"]=self.accountJsessionid
                 newdict["user_id"]=self.accountUser_id
             elif api_client=="TRADE":
                 newdict["sessionid"]=self.sessionid
             print(newdict)
             request_data=newdict

             #print(":".join(["%s=%s" % (k,v) for k,v in request_data.split("&")]))




         if s == None:
              s = requests.session()
              #print(s)
         if request_method == 'POST':
              if api_client=="ACCOUNT":
                 url=api_host+request_url+";jsessionid="+self.accountJsessionid
                 r = s.post(url, data = request_data, headers = headers)         #由于此处数据没有经过加密，所以需要把Json格式字符串解码转换成**Python对象**
              elif api_client=="TRADE":
                 url=api_host+request_url+";jsessionid="+self.sessionid
                 r = s.post(url, data = request_data, headers = headers)

              elif request_url != '/login' :
                  r = s.post(url=api_host+request_url, data = request_data, headers = headers)         #由于此处数据没有经过加密，所以需要把Json格式字符串解码转换成**Python对象**

              elif request_url == '/login' :
                  s = requests.session()
                  r = s.post(url=api_host+request_url, data = request_data, headers = headers)          #由于登录密码不能明文传输，采用MD5加密，在之前的代码中已经进行过json.loads()转换，所以此处不需要解码
         elif request_method == 'GET':
              r = s.get(url=api_host+request_url, data = request_data, headers = headers)
         else:
              logging.error(num + ' ' + api_purpose + '  HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
              s = None
              return 400,s
         status = r.status_code
         #resp = r.text
         try:
             if request_method=="POST":
                resp =(json.dumps(r.json(),ensure_ascii=False))
             else:
                 resp = r.text
             print(resp)
         except Exception as e:
             print(str(e))
         try:
             if status == 200 :
                if check_point in resp:
                    logging.info(num + ' ' + api_module+ ' '+ api_purpose + ' 成功，' + str(status) + ', ' + str(resp))
                    return status, resp, s
                else:
                    logging.error(num + ' ' + api_module+ ' '+ api_purpose + ' 失败！！！，[' + str(status) + '], ' +str(api_host)+str(request_url) +' '+ str(resp)+' ' + str(request_data))
                    return 200, resp , None
             else:
                logging.error(num + ' ' + api_module+ ' '+ api_purpose + '  失败！！！，[' + str(status) + '],'+str(resp))
                return status, resp.decode('utf-8'), None
         except Exception as e:
             print(str(e))

    def runTest(self,testCaseFile,j):
          testCaseFile = os.path.join(os.getcwd(),testCaseFile)
          if not os.path.exists(testCaseFile):
              logging.error('测试用例文件不存在！')
              sys.exit()
          testCase = xlrd.open_workbook(testCaseFile)

          table = testCase.sheet_by_index(j)
          tableName=testCase.sheet_by_index(j).name

          errorCase = []                #用于保存接口返回的内容和HTTP状态码
          succeedCase = []
          statInfo = []
          statInfo.append(tableName)
          s = None
          startTime=time.strftime('%Y-%m-%d %H:%M:%S')
          d1=datetime.datetime.now()
          #读取sheet表中的每一行数据，并发post请求
          for i in range(1,table.nrows):
                if table.cell(i, 11).value.replace('\n','').replace('\r','') != 'Yes':
                    continue
                num = str(int(table.cell(i, 0).value)).replace('\n','').replace('\r','')
                api_module = table.cell(i, 1).value.replace('\n','').replace('\r','')
                api_purpose = table.cell(i, 2).value.replace('\n','').replace('\r','')
                api_host = table.cell(i, 3).value.replace('\n','').replace('\r','')
                request_url = table.cell(i, 4).value.replace('\n','').replace('\r','')
                request_data = table.cell(i, 5).value.replace('\n','').replace('\r','')
                check_point = table.cell(i, 6).value
                request_method = table.cell(i, 7).value.replace('\n','').replace('\r','')
                request_data_type = table.cell(i, 8).value.replace('\n','').replace('\r','')
                api_client = table.cell(i, 9).value.replace('\n','').replace('\r','')
                s = table.cell(i, 10).value.replace('\n','').replace('\r','')


                status, resp, s = self.interfaceTest(num, api_module,api_purpose, api_host, request_url, request_data, check_point, request_method, request_data_type,api_client)
                #如果状态码不为200或者返回值中没有检查点的内容，那么证明接口产生错误，保存错误信息。
                if status != 200 or check_point not in resp:
                    errorCase.append(("ERROR:" + ' ' + num + ' ' + api_module+ ' '+ api_purpose +' ' + "失败！！！", str(status), api_host+request_url, resp))
                else:
                    succeedCase.append((' ' + num + ' ' + api_module+ ' '+ api_purpose +' ' + "成功！！！", str(status), api_host+request_url, resp))

          endTime=time.strftime('%Y-%m-%d %H:%M:%S')
          d2=datetime.datetime.now()
          diffTime=d2.second-d1.second
          print("time" + str(diffTime))
          statInfo.append(len(errorCase))
          statInfo.append(len(errorCase)+len(succeedCase))
          statInfo.append(str(startTime))
          statInfo.append(str(endTime))
          statInfo.append(str(diffTime)+ ' ' + "s")
          statInfo.append("5min")
          print(statInfo)
          return errorCase,succeedCase,statInfo

    def writeExcel(self,testCaseFile,list,line):
        rb = open_workbook(testCaseFile)
        if not os.path.exists(testCaseFile):
            logging.error('测试用例文件不存在！')
            sys.exit()
        rs = rb.sheet_by_index(0)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for i in range(0,len(list)):
            ws.write(line,i,list[i])
            if i==3 or i==4:
                ws.col(i).width=5000
        wb.save(testCaseFile)
    def writeMysql(self,list,client):
        try:
            cur = self.conn.cursor()
            #cur.execute("INSERT INTO Jinghua_Tongji VALUES (NULL,\'" + client + "\','',\'" + list[0] + "\',\'" + list[1] + "\', \'" + list[2] + "\', \'" + list[3] + "\', \'" + list[4] + "\', \'" + list[5] + "\', \'" + list[6] + "\')")
            cur.execute("INSERT INTO Jinghua_Tongji (client_type,business_type,err_req_count,total_req_count,begin_time,finish_time,used_time,period) VALUES (\'" + str(client) + "\',\'" + str(list[0]) + "\'," + str(list[1]) + ", " + str(list[2]) + ", \'" + str(list[3]) + "\', \'" + str(list[4]) + "\', \'" + str(list[5]) + "\', \'" + str(list[6]) + "\')")
            #print("INSERT INTO Jinghua_Tongji (client_type,business_type,err_req_count,total_req_count,begin_time,finish_time,used_time,period) VALUES (\'" + str(client) + "\',\'" + str(list[0]) + "\'," + str(list[1]) + ", " + str(list[2]) + ", \'" + str(list[3]) + "\', \'" + str(list[4]) + "\', \'" + str(list[5]) + "\', \'" + str(list[6]) + "\')")
            #print(list)
            cur.close()
            self.conn.commit()
            #self.conn.close()
        except Exception as e:
            print(str(e))


    def main(self):
        tableCase = xlrd.open_workbook('TestCase/TestCase.xls')
        print(len(tableCase.sheets()))
        for i in range(1,len(tableCase.sheets())):
            errorTest,succeedTest,statInfo=self.runTest('TestCase/TestCase.xls',i)
            #list=["1",2,3,"4","5","6","7"]
            #self.writeExcel('TestCase/TestCase.xls',statInfo,i)
            self.writeMysql(statInfo,client="CAPP")
            #print(succeedTest)
            file=File()
            if len(errorTest) > 0:
                for test in errorTest:
                    file.writeFile(test,"TestCase/error.txt")

            for test in succeedTest:
                file.writeFile(test,"TestCase/succeed.txt")



if __name__ == '__main__':
    test1=LogicTest()
    test1.main()
