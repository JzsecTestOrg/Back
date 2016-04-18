#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import datetime
import time
import json
import configparser

class InterfaceTests:

    base_url='http://bapp.tlan.com.cn/'
    mobilephone='15501253701'
    password='Jzzq87654321'
    def __init__(self):                
        #if os.path.exists(os.path.join(os.getcwd(), 'interfaces.config')):
        #    config=configparser.RawConfigParser()
        #    with open(os.path.join(os.getcwd(), 'interfaces.config'), 'r') as cfgfile:
        #        config.readfp(cfgfile)
                #self.app_base_url=config.get('base_url', 'app_base_url')
                self.Bapp_base_url='http://t.a.jzsec.com'
                self.Capp_base_url='http://t.c.jzsec.com'
                self.mobilephone='15501253701'
                self.password='Jzzq87654321'
        #self.finalstate=True
        #self.authcodeurl="http://redisman.tlan.com.cn/?view&s=0&d=0&key=common_helpers_sms_reset_pass_verify_code_"
                #self.appVer=config.get('appVer', 'appVer')

    """
    generalParams = { 
        'token':'',b
        'mobilephone': ['' , '13911387297'],
        'dataAuth':['', '!@#$%^&*()'],
        'deviceCode':'python',
        'appVer':['', '1'],
        'appType':['', 'Android', 'IOS'],
        'envType':['', '20']
        }
    """
    applicationParams = {
        'pageNo':1,
        'pageSize':20,
        'sort':'ASC',
        'filter':''
        }

    
    def expandKey(self, input, key):
        output=[]
        for d in input:
            if isinstance(d[key], list):
                for v in d[key]:
                    nv=d.copy()
                    nv[key]=v
                    output.append(nv)

        if len(output) == 0:
            return input
                             
        return output
    def expand(self, params):
        output=[params]
        for k in params.keys():
            o = self.expandKey(output, k)
            if len(o) > 0:
                output=o
        return output

    def requestSucceeded(self, js):
        if js['code'] == 0:
            return True
        else:
            return False

    def get_login_token(self, mobile=None, password=None):
        params={}        
        params['token']=''
            
        params['mobilephone']=mobile
        params['appVer']='12'
        params['envType']='0'
        params['deviceType']='Android'
        params['deviceCode']='python'
        params['password']=password
        params['appType']='1'
        params['agree']='1'
        #print(params['appVer'])

        if mobile is None: 
            params['mobilephone']=self.mobilephone
        if password is None:
            params['password']=self.password
            #print(params['password'])
  
        succeeded,js=self.interface_test(self.Bapp_base_url + 'system/login', params)
        if succeeded:
            try:
                print(js['data'])
                print(js['data']['token'])
                return js['data']['token']
                

                #return js['data']['userId']
                #InterfaceTests.token=js['data']['token']
                #InterfaceTests.userId=js['data']['userId']
                #print(InterfaceTests.userId)
                
                
                
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
  
        succeeded,js=self.interface_test(self.app_base_url + 'system/login', params)  
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


    def interface_test(self, url, params, returnCodeFunc=None, log=None):
        try:
            
            if 'mobilephone' not in params.keys():
                params['mobilephone']=self.mobilephone                
            #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            response = requests.post(url, data=json.dumps(params), timeout=10)
            #response = requests.post(url, data=params, timeout=10)
            print('---------------------------------------------------------------------------')
            print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            print(url)
            print(json.dumps(params))
            if log is not None:
                log.write('---------------------------------------------------------------------------\n')
                log.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '\n')
                log.write(url+ '\n')
                #log.write(json.dumps(params) + '\n')

            #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            print('\nHTTP %d' % response.status_code)  
            #print(response.text)
            if log is not None:
                log.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+ '\n')
                log.write('\n%d\n' % response.status_code)
                #log.write(response.text+ '\n')
            if response.status_code == 200:
                js = response.json()
                if response.text == '':
                    self.finalstate= False
                    #return False,None
                #print((js['code']==0 or js['code']==100 or js['code']==1))
                #print(type(js['code']))
                if (int(js['code'])==0 or js['code']==100 or js['code']==1)==True:
                    pass
                else:
                    print(str(js['code'])+"code check faild")
                    self.finalstate= False
                print(response.text)
                jstest=(json.dumps(js,ensure_ascii=False))
                print(jstest)
                if log is not None:
                    #log.write(response.text + '\n')
                    log.write(jstest + '\n')
                #print(jstest.find(params['returnvalue']))
                #print(url.find("/system/login"))
                #print ("/system/login" in url)
                if ("/system/login" in url) == False:
                    print(params['returnvalue'])
                    if params['returnvalue']==None:
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
                        log.write('Request succeeded.\n') 
                return True,js
            else:
                response.raise_for_status()
           

        except Exception as e:
            print('')            
            print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            print(str(e))
            if log is not None:
                log.write(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+ '\n')
                log.write(str(e)+ '\n')
        
        return False,None


    def batch_interface_test(self, path, expandableParams, base_url=None, noexpandParams=None, returnCodeFunc=None, stopOnSucceed=False, interval=0.05):  

        if base_url is None:
            base_url=self.app_base_url
            url=base_url+path
            
        urlpasrs = requests.utils.urlparse(url)
        #file= urlpasrs.netloc.split('.')[0] + '_'.join(urlpasrs.path.split('/')) + '.log'
        file= "bapp" + "_" + datetime.datetime.today().strftime('%Y_%m_%d_%H') + '.log'
        #print(file)
        
        with open(file, 'a') as log:
            try:
                expanded = self.expand(expandableParams)
                if returnCodeFunc is None:
                    returnCodeFunc = self.requestSucceeded
                for p in expanded:
                    if noexpandParams is not None:
                        p=dict(p, **noexpandParams)
                    operationSucceeded, js = self.interface_test(url, p, returnCodeFunc=returnCodeFunc, log=log)
                    if stopOnSucceed & operationSucceeded:
                        return js
                    time.sleep(interval)   
            except:
                log.flush()

if __name__ == '__main__':
    #print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    test=InterfaceTests()   
    #test.batch_interface_test('follow/followlist', test.generalParams, returnCodeFunc=test.requestSucceeded)
    print(test.get_login_token())
    #print(test.get_login_userId())
    #print(test.getAuthCode())
    




    
    
    


    
