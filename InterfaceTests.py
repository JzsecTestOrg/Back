__author__ = 'jinghua'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import datetime
import time
import json
import re
import configparser

class InterfaceTests:


    def __init__(self):

        #测试环境
        # self.bappurl='http://t.a.jzsec.com'
        # self.cappurl='http://t.c.jzsec.com'
        # self.mobilephone='18010161483'
        # self.password='qaz123'

        #开发环境
        self.cappurl='http://capp.tlan.com.cn'
        self.bappurl='http://bapp.tlan.com.cn'
        self.mobilephone='18010161483'
        self.password='qaz123'

        self.cappmobilephone='13300000008'
        self.capppassword='qaz123'
        self.returnparams={}
        self.finalstate=True
        self.charactor='982412348324932743231984349832479324１３３４３５ｊｚｚｑｈｌｗｓｙｂ九州证券너만이 날 웃게 하는&“；；《&○【※□◎{\and 1=1 select* from b_user'
        self.empty=''

    def requestSucceeded(self, js):
        if js['code'] == 0:
            return True
        else:
            return False

    def get_login_token(self, client=None, mobile=None, password=None):
        params={}
        params['token']=''
        if client=='bapp' or client=='client_id':
            params['mobilephone']=self.mobilephone
            params['password']=self.password
        else:
            params['mobilephone']=self.cappmobilephone
            params['password']=self.capppassword
        params['appVer']='94'
        params['envType']='0'
        params['deviceType']='Android'
        params['deviceCode']='python'
        params['appType']='1'
        params['agree']='1'
        #print(params['appVer'])
        if client=='bapp' or client=='client_id':
            succeeded,js=self.interfaceTest(self.bappurl + '/system/login', params)
        else:
            succeeded,js=self.interfaceTest(self.cappurl + '/cuser/login', params)

        if succeeded:
            try:
                print(js['data'])

                if client=='bapp':
                    print(js['data']['token'])
                    self.returnparams['bapptoken']=js['data']['token']
                    self.returnparams['userId']=js['data']['userId']
                    print(js['data']['userInfo']['client_id'])
                    self.returnparams['client_id']=js['data']['userInfo']['client_id']
                    #return js['data']['userInfo']['client_id']
                elif client=='capp':
                    #print('capp')
                    print(js['data']['token'])
                    self.returnparams['capptoken']=js['data']['token']
                    self.returnparams['cappuserId']=js['data']['userId']
                    print(js['data']['client_id'])
                    self.returnparams['cappclient_id']=js['data']['client_id']
                return self.returnparams


            except:
                return ''
    def get_login_userId(self, mobile=None, password=None):


        params={}
        params['token']=''


        if mobile is None:
                params['mobilephone']=self.mobilephone
        if password is None:
                params['password']=self.password


        params['mobilephone']=mobile
        params['appVer']='12'
        params['envType']='0'
        params['deviceType']='Android'
        params['deviceCode']='python'
        params['password']=password
        params['appType']='1'
        params['agree']='1'
        #print(params['appVer'])

        succeeded,js=self.interfaceTest(self.bappurl + '/system/login', params)
        if succeeded:
            try:
                return js['data']['userId']
                #return js['data']['userId']
                #InterfaceTests.token=js['data']['token']
                #InterfaceTests.userId=js['data']['userId']
                #print(InterfaceTests.userId)
            except:
                return ''

    def getAuthCode(self, mobile=None):
        params={}
        params['mobilephone']=mobile
        params['appVer']='12'
        params['envType']='0'
        params['deviceType']='Android'
        params['deviceCode']='python'
        params['appType']='1'
        #print(mobile)
        if mobile is None:
                params['mobilephone']=self.mobilephone
        #print(self.mobilephone)
        url=self.authcodeurl + str(params['mobilephone'])
        #print(url)
        response = requests.get(url,timeout=10)
        #print(response.text)


    def interfaceTest(self, url, params,returnvalue=None,returnCodeFunc=None, log=None,trade=None):

        try:
            print(returnvalue)
            self.finalstate=True
            #if 'mobilephone' not in params.keys():
            #    params['mobilephone']=self.mobilephone
            #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            if trade is not None:
                response = requests.post(url, data=params, timeout=10)
            else:
                response = requests.post(url, data=json.dumps(params), timeout=10)
            print('---------------------------------------------------------------------------')
            print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            print(url)
            print(json.dumps(params))
            file= "bapp" + "_" + datetime.datetime.today().strftime('%Y_%m_%d_%H') + '.log'
            log=open('./log/' + file, 'a')
            logerr=open('./log/' + file + '.failed', 'a')
            log500=open('./log/' + file + '.500', 'a')
            if log is not None and response.status_code == 200:
                log.write('---------------------------------------------------------------------------\n')
                log.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                log.write(url + '\n')
                log.write(json.dumps(params) + '\n')

            else:
                log500.write('---------------------------------------------------------------------------\n')
                log500.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                log500.write(url + '\n')
                log500.write(json.dumps(params) + '\n')
                #logerr.write(unicode(json.dumps(params), 'gbk') + '\n')
                #log.write(json.dumps(params) + '\n')
                #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            print('\nHTTP %d' % response.status_code)
            #print(response.text)
            if log is not None and response.status_code==200:
                log.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+ '\n')
                log.write('\n%d\n' % response.status_code)
                #log.write(response.text+ '\n')
            else:
                log500.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+ '\n')
                log500.write('\n%d\n' % response.status_code)

            if response.status_code == 200:
                js = response.json()
                if response.text == '':
                    self.finalstate= False
                jstest=(json.dumps(js,ensure_ascii=False))
                #if ( jstest.find("获取成功") != -1):
                #    pass
                #else:
                #    print("获取成功 check faild")
                #    self.finalstate= False
                print(response.text)

                print(jstest)
                if log is not None and response.status_code==200:
                    #log.write(response.text + '\n')
                    log.write(jstest + '\n')
                else:
                    log500.write(jstest + '\n')
                #print(jstest.find(params['returnvalue']))
                #print(url.find("/system/login"))
                #print ("/system/login" in url)
                if ("/login" in url) == False:
                    #print(jstest.find("获取成功"))
                    print(params['returnvalue'])
                    if params['returnvalue']==None :
                        pass
                    else:
                        if jstest.find(params['returnvalue']) == -1:
                            self.finalstate=False
                            print(str(params['returnvalue']) + "is not found")
                            #return False,None
                #if (returnCodeFunc is not None) and returnCodeFunc(js):
                #    if log is not None:
                #        log.write('Request succeeded.\n')
                #print(self.finalstate)

                if log is not None:

                    if self.finalstate==True:
                        print('Request succeeded.')
                        log.write('Request succeeded.\n')
                    else:
                        print('Request failed.')
                        logerr.write('---------------------------------------------------------------------------\n')
                        logerr.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                        logerr.write(url+ '\n')
                        logerr.write(json.dumps(params)+ '\n')
                        logerr.write(params['returnvalue']+ '\n')
                        logerr.write(jstest + '\n')
                        logerr.write('Request failed.\n')

                return True,js
            else:
                response.raise_for_status()
            log.close()


        except Exception as e:
            print('')
            print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            print(str(e))
            print("done")
            if log is not None:
                log.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+ '\n')
                log.write(str(e)+ '\n')

        return False,None

    def iterationTest(self, url, params, returnCodeFunc=None, log=None):
        print(params.items())
        print(params.__len__())
        #for i in range(params.__len__()):
        for k,value in params.items():
            paramscharactor=params.copy()
            paramsempty=params.copy()
            paramscharactor[k]=self.charactor
            paramsempty[k]=self.empty
            #print (k,value)
            print (json.dumps(paramscharactor))
            print (json.dumps(paramsempty))
            self.interfaceTest(url , paramscharactor)
            self.interfaceTest(url , paramsempty)

    def regularTest(self, url, params, returnCodeFunc=None, log=None,trade=None):
            bool,temp=self.interfaceTest(url,params,trade=trade)
            print(params['Regexp1'])
            print(str(temp))
            p1 = re.compile("r"+params['Regexp1'])
            p2 = re.compile("r"+params['Regexp2'])
            print(p1.search(str(temp)))
            print(p2.search(str(temp)))

    def tradeCheck(self, url, params, returnCodeFunc=None, log=None,trade=None):
            bool,temp=self.interfaceTest(url,params,trade=trade)
            #print(temp['results'][0].keys())
            #print(params['returncheck'])
            try:
                if (sorted(temp['results'][0].keys())==sorted(params['returncheck'])) is True and temp['error_no']=="0" :
                    print("pass")
                else:
                    file= "bapp" + "_" + datetime.datetime.today().strftime('%Y_%m_%d_%H') + '.log'
                    logerr=open('./log/' + file + '.failed', 'a')
                    logerr.write('---------------------------------------------------------------------------\n')
                    logerr.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                    logerr.write(url+ '\n')
                    logerr.write(json.dumps(params)+ '\n')
                    logerr.write(str(sorted(temp['results'][0].keys()))+ '\n')
                    logerr.write(str(temp) + '\n')
                    logerr.write('Request failed.\n')
            except Exception as e:
                print(e)



class MainLogic(InterfaceTests):
    def scenelogicTest(self, url, params, inputp,outputp,returnCodeFunc=None, log=None):
        print(params.items())
        print(params.__len__())

        print(inputp)
        print(outputp)
        #for i in range(inputp.__len__()):
        for k,value in inputp.items():
                params["returnvalue"]=outputp[k]
                params[k[:len(k)-1]]=inputp[k]
                self.interfaceTest(url , params)
        #if isinstance(inputp,dict):
        #    print(inputp.keys())
        #else:
        #    print("is not a dict")



if __name__ == '__main__':
    #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    test=InterfaceTests()
    #test.batch_interface_test('follow/followlist', test.generalParams, returnCodeFunc=test.requestSucceeded)
    #print(test.get_login_token('capp'))
    #print(test.get_login_token('owner'))
    print(test.get_login_token('bapp'))
    #print(test.get_login_token('client_id'))
    #print(test.get_login_userId())
    #print(test.getAuthCode())












