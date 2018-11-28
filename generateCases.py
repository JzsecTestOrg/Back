# -*- coding: utf-8 -*-
__author__ = 'xuwen'
#modify---jinghua
import os
import xlsxwriter
import sys
import copy
from InterfaceTests import InterfaceTests
import xlrd,xlwt,json,requests,time,datetime,pymysql


class generateCases():
    def __init__(self):
        self.worspace = 'D:\PHP\Workspace\svn\prod\/'
        self.products = ['bapp']
        self.common_params = {'bapp':['CaseID', 'deviceCode', 'mobilephone', 'userId', 'token', 'dataAuth', 'appVer', 'appType', 'envType']}
        self.cases = {}
        self.caseid = 1
        self.test=InterfaceTests()
        self.NOWTIMEFORMAT = '%Y-%m-%d-%H'
        #测试环境
        #self.connTest = pymysql.connect(host='10.10.22.78', port=3306, user='crm', passwd='crm@2015', db='crm',charset='utf8')
        #开发环境
        self.connDev = pymysql.connect(host='10.10.87.38', port=3306, user='crm', passwd='crm@2015', db='crm',charset='utf8')
        self.bappparams ={
        "mobilephone" : "18010161483",
        "userId" : "075783d2a772a1f5ad12cac9f9eccdea",
        "token" : "18010161483",
        "dataAuth" : "12",
        "envType" : "0",
        "deviceType" : "Android",
        "deviceCode" : "python",
        "appType" : "1",
        "appVer" : "V3.3.0.01"
        }
        self.cappparams ={
        "mobilephone" : "13300000001",
        "userId" : "6b4f9f85012b304979c9413300000001",
        "token" : "13300000001",
        "dataAuth" : "12",
        "envType" : "0",
        "deviceType" : "Android",
        "deviceCode" : "python",
        "appType" : "1",
        "appVer" : "V3.3.0.01"
        }

    def case_data(self):
        for i in self.products:
            self.cases[i] = {}
            directory = self.worspace + i + '/controllers/'
            for file in os.listdir(directory):
                if(os.path.isfile(os.path.join(directory,file)) and file[0] != '.' and file != 'BaseController.php'):
                    controller = file.split('.')[0]
                    self.cases.get(i)[controller] = {}
                    path = os.path.join(directory,file)
                    interface_list = {}
                    interface = ''
                    title = []
                    result = []
                    params_count = 0

                    with open(path, "r") as f:
                        lines = f.readlines()
                    for line in lines:
                        if(line.__contains__('action') and line.__contains__('()') and not line.__contains__('//') and not line.__contains__('*') and not line.__contains__(';') and not line.__contains__('before')):
                            interface = path.split('/')
                            interface = interface[len(interface) - 1].split('.')[0].lower()
                            interface = interface + '/' +line.split('action')[1].split('()')[0].lower()
                            interface_list[interface] = [self.common_params.get(i)]
                        elif(line.__contains__('checkAppVer')):
                            interface = 'system/checkappver'
                            interface_list[interface] = [self.common_params.get(i)]
                        elif(line.__contains__('before')):
                            interface = 'before'
                        if(line.__contains__('getParam') and interface != 'before'):
                            param = ''
                            try:
                                param = line.split('getParam')[1].split("'")[1]
                            except:
                                param = line.split('getParam')[1].split("\"")[1]
                            if(param not in interface_list[interface][0]):
                                interface_list_copy = copy.deepcopy(interface_list[interface])
                                interface_list_copy[0].append(param)
                                interface_list[interface] = interface_list_copy
                    for k in interface_list.keys():
                        interface_list_copy = copy.deepcopy(interface_list)
                        params_count = len(interface_list_copy[k][0]) - 1
                        interface_list_copy[k][0].append('Code_Result')
                        interface_list_copy[k][0].append('Message')
                        interface_list_copy[k][0].append('Data')
                        interface_list_copy[k][0].append(params_count)
                        interface_list[k] = interface_list_copy[k]
                    for line in lines:
                        if(line.__contains__('action') and line.__contains__('()') and not line.__contains__('//') and not line.__contains__('*') and not line.__contains__(';') and not line.__contains__('before')):
                            self.caseid = 1
                            interface = path.split('/')
                            interface = interface[len(interface) - 1].split('.')[0].lower()
                            interface = interface + '/' +line.split('action')[1].split('()')[0].lower()
                        elif(line.__contains__('checkAppVer')):
                            interface = 'system/checkappver'
                            interface_list[interface] = [self.common_params.get(i)]
                        elif(line.__contains__('before')):
                            interface = 'before'
                        if(line.__contains__('jsonReturn') and interface != 'before'):
                            try:
                                result = []
                                code = line.split('jsonReturn(')[1].split(',')[0]
                                try:
                                    message = line.split('jsonReturn(')[1].split(',')[1].split("'")[1]
                                except:
                                    message = line.split('jsonReturn(')[1].split("'")[1]

                                if(len(message) == 1):
                                    message = ''
                                else:
                                    try:
                                        message = unicode(message[1])
                                    except:
                                        pass
                                result.append(unicode(str(self.caseid),'utf8'))
                                for r in range(0, len(interface_list[interface][0]) - 5):
                                    result.append(u'')

                                result[1]=(unicode(self.bappparams['deviceCode'],'utf8'))
                                result[2]=(unicode(self.bappparams['mobilephone'],'utf8'))
                                result[3]=(unicode(self.bappparams['userId'],'utf8'))
                                result[4]=(unicode(self.bappparams['token'],'utf8'))
                                result[5]=(unicode(self.bappparams['dataAuth'],'utf8'))
                                result[6]=(unicode(self.bappparams['appVer'],'utf8'))
                                result[7]=(unicode(self.bappparams['appType'],'utf8'))
                                result[8]=(unicode(self.bappparams['envType'],'utf8'))
                                #print result
                                    #result.append(unicode(self.bappparams['deviceCode'],'utf-8'))
                                result.append(u'%s'%code)
                                result.append(unicode(message,'utf8'))
                                result.append(u'')
                                #print result
                                interface_list[interface].append(result)
                            except Exception as e:
                                print "case_data" + str(e)
                            self.caseid = self.caseid + 1
                self.cases[i][controller] = interface_list
        return self.cases

    def generate_case(self):
        data = generateCases().case_data()
        for product in data.keys():
            for controller in data.get(product).keys():
                isExist=True
                dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Interface/' + product
                if(os.path.exists(dir) == False):
                    os.mkdir(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Interface/' + product)
                file = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Interface/' + product + '/' + controller + '.xlsx'
                caseFile = xlrd.open_workbook(file)
                for elem in caseFile._sheet_names:
                    try:
                        caseFile.sheet_by_name(elem)._position
                        #caseFile.sheet_by_name(987987)._position
                    except Exception as e:
                        print str(e)
                        isExist=False

                if isExist == True:
                    continue
                #新建工作簿
                workbook = xlsxwriter.Workbook(file)
                summary_format = workbook.add_format({
                'bold': 2,
                'border': 1,
                'align': 'left',
                'valign': 'vcenter',
                'font_name': 'Calibri',
                'font_size': 15,
                'font_color': 'black',
                'bg_color': '#006699'})

                summary_info_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'left',
                'valign': 'vcenter',
                'font_name': 'Calibri',
                'font_size': 11,
                'font_color': 'black',
                'bg_color':'#66ccff'})

                title_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'font_name': 'Calibri',
                'font_size': 11,
                'font_color': 'black',
                'bg_color':'#006699'})

                info_format = workbook.add_format({
                'bold': 0,
                'border': 1,
                'align': 'left',
                'valign': 'vcenter',
                'font_name': u'黑体',
                'font_size': 11,
                'bg_color':'#66ccff'})

                for i in data.get(product).get(controller).keys():
                    #新建每个接口对应的工作表
                    worksheet = workbook.add_worksheet(i.split('/')[1])
                    colomns = len(data.get(product).get(controller).get(i)[0]) - 1
                    rows_cases = len(data.get(product).get(controller).get(i)) - 1
                    #工作表宽高格式设定
                    rightcolomn = chr(ord('A') + colomns - 1)
                    worksheet.set_column('A:' + rightcolomn, 15)
                    for j in range(1, 50):
                        worksheet.set_row(j, 20)
                    worksheet.merge_range('A1:B1', 'Interface', summary_format)
                    worksheet.merge_range('C1:' + rightcolomn + '1', i, summary_info_format)
                    worksheet.merge_range('A2:B2', 'Params_Count', summary_format)
                    worksheet.merge_range('C2:' + rightcolomn + '2', colomns - 4, summary_info_format)

                    worksheet.merge_range('A3:' + rightcolomn + '3', '')

                    for m in range(0, len(data.get(product).get(controller).get(i))):
                        colomn = 'A'
                        for n in range(0, len(data.get(product).get(controller).get(i)[m])):
                            row = m + 4
                            if(m == 0 and n < (len(data.get(product).get(controller).get(i)[m]) - 1)):
                                worksheet.write(colomn + str(row), data.get(product).get(controller).get(i)[m][n], title_format)
                                colomn = chr(ord(colomn) + 1)
                            elif(m != 0):
                                list1=data.get(product).get(controller).get(i)[m][n]
                                worksheet.write(colomn + str(row), data.get(product).get(controller).get(i)[m][n], info_format)
                                colomn = chr(ord(colomn) + 1)
            #     #关闭工作簿
                workbook.close()

    def traverse_dir(self):
        dirList=[]
        data = generateCases().case_data()
        for product in data.keys():
            dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Interface/' + product
            if(os.path.exists(dir) == False):
                os.mkdir(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Interface/' + product)
            for files in os.walk(dir):
                print files
            for elem in files[2]:
                     dirList.append(files[0] + "/" + elem)
            return dirList

    def operate_mysql(self,evn,sql):
        conn=u''
        try:
            if evn == "test":
                conn = self.connTest
            elif evn == "dev":
                conn = self.connDev

            cur = conn.cursor()
            cur.execute(sql)
            print(sql)
            for r in cur:
                print(r)
            cur.close()
            conn.commit()
            #conn.close()
        except Exception as e:
            print e



    def check_result(self,checkPoint,interface,caseid,status,resp,):
        errorCase500=[]
        errorCase=[]
        succeedCase=[]
        #如果状态码不为200或者返回值中没有检查点的内容，那么证明接口产生错误，保存错误信息。
        if status != 200:
            errorCase500.append(("ERROR:" + ' ' + interface + ' '+ caseid + ' ' + checkPoint+ ' ' + "FAILED!!!", str(status), resp))
        elif not resp.__contains__(checkPoint):
            errorCase.append(("ERROR:" + ' ' + interface + ' '+ caseid + ' ' + checkPoint+ ' ' + "FAILED!!!", unicode(str(status),"utf-8"), resp))
        else:
            succeedCase.append(("SUCC:" + ' ' + interface + ' '+ caseid + ' ' + checkPoint+ ' ' + "SUCCESS", str(status) , resp))
        filetime=time.strftime(self.NOWTIMEFORMAT, time.localtime(time.time()))
        dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/Interface/'
        filerr=open(dir + "error" + filetime + ".txt",'a+')
        filerr500=open(dir + "error500" + filetime + ".txt",'a+')
        filesucc=open(dir + "succ" + filetime + ".txt",'a+')
        if len(errorCase) > 0:
            for test in errorCase:
                #for temp in test:
                #    print temp
                #    print type(temp)
                    #temp.encode('GBK','ignore')
                filerr.write(str(test) + "\n")
        filerr.close()
        if len(errorCase500) > 0:
            for test in errorCase500:
                filerr500.write(str(test) + "\n")
        filerr500.close()
        for test in succeedCase:
            filesucc.write(str(test).encode('utf-8') + "\n")
        filesucc.close()

    def run_case(self,caseFilList):
        params={}
        for elem in caseFilList:
            if not os.path.exists(elem):
                logging.error('测试用例文件不存在！')
                sys.exit()
            #针对每一个excel文件
            caseFile = xlrd.open_workbook(os.path.join(os.getcwd(),elem))
            print  elem
            for elem in caseFile._sheet_names:
                #针对每一个excel文件中的sheet表
                caseSheet=caseFile.sheet_by_name(elem)
                #table = testCase.sheet_by_index(j)
                #print testCase.sheet_by_index(0).name
                #print caseSheet.name
                #print caseSheet.nrows
                print caseSheet.ncols
                errorCase = []                #用于保存接口返回的内容和HTTP状态码
                succeedCase = []
                statInfo = []
                statInfo.append(caseFile)
                s = None
                startTime=time.strftime('%Y-%m-%d %H:%M:%S')
                d1=datetime.datetime.now()
                #读取sheet表中的每一行数据，并发post请求
                for i in range(4,caseSheet.nrows):
                    for j in range(1,caseSheet.ncols):
                        try:
                            params[str(caseSheet.cell(3,j).value)] = str((caseSheet.cell(i, j).value)).replace('\n','').replace('\r','')
                        except Exception as e:
                            print "Exception" + " line = " + str(i) + str(e)
                    del params["Message"]
                    print "http://bapp.tlan.com.cn/" + str(caseSheet.cell(0,2).value)
                    #print params
                    print json.dumps(params)
                    paramscount= int(caseSheet.cell(1,2).value)+2
                    checkPoint = caseSheet.cell(i,paramscount).value.replace('\n','').replace('\r','')
                    data = caseSheet.cell(i,paramscount+1).value.replace('\n','').replace('\r','')
                    interface = (caseSheet.cell(0,2).value)
                    caseid = str(caseSheet.cell(i, 0).value).replace('\n','').replace('\r','')
                    #response = requests.post("http://bapp.tlan.com.cn/" + str(caseSheet.cell(0,2).value), data=params, timeout=10)
                    if data == u'':
                        status, resp = self.test.interfaceTest(u"http://bapp.tlan.com.cn/" + caseSheet.cell(0,2).value.replace("controller",""), json.dumps(params))
                    else:
                        self.operate_mysql("dev",data)
                        status, resp = self.test.interfaceTest(u"http://bapp.tlan.com.cn/" + caseSheet.cell(0,2).value.replace("controller",""), json.dumps(params))
                    try:
                        if len(resp) >1000:
                            checkPoint = caseSheet.cell(i,paramscount-1).value.replace('\n','').replace('\r','')
                    except Exception as e:
                        print str(e)
                    print checkPoint
                    print status,resp
                    self.check_result(checkPoint,caseid,interface,status,resp)
                    params.clear()



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    generateCases().generate_case()
    #print generateCases().traverse_dir()
    temp=generateCases().traverse_dir()
    print temp
    print generateCases().run_case(temp)
