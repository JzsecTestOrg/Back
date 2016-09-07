# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:38:25 2015

@author: lijunhui
"""
#import pandas
import os, sys
import string
from pytesseract import pytesseract
import requests
import datetime
import time
import json
import configparser
import random
import threading
import math
import subprocess

#from RsaUtils import *
from io import BytesIO
from PIL import Image, ImageOps
from pytesseract import *
from InterfaceTests import InterfaceTests
from Common import *

#from imasterQuoteHelper import QuoteHelper
#from imasterTradeHelper import TraderHelper

class TradeTest:
    def __init__(self):
        self.verifycodepath = 'http://123.59.79.146:8089/servlet/NewImage'
        self.path = 'http://123.59.79.146:8089/servlet/json'
        self.trade=True
        self.capppath = 'http://t.c.jzsec.com'

        self.template = {
            'branch_no': '0811',
            'fund_account': '81106500059',
            'cust_code': '81106500059',
            'sessionid': 'abcQD150aHQI3cXb3stev',
            'stock_account': '',
            'stock_code': '',
            'exchange_type': '',
            'entrust_way': 'G',
            'op_station': '192.168.88.85',
        }

    def get_publickey(self,session=None):
        params = {'funcNo': '1000000'}
        response = session.get(self.path, params=params).json()

        if response['error_no'] == '0':
            return response['results'][0]


    def get_captcha(self,session=None):
        r = random.randint(99999999, 9999999999)
        params = {
            'r': r,
            'mobileKey': r
        }

        response = session.get(self.verifycodepath, params=params)
        return r, response


    def recognize_captcha(self,r=None, data=None):
        if data is None:
            return '0000'
        file = 'd:/code_{}.png'.format(r)
        with open(file, 'wb') as f:
            f.write(data)

        mem = BytesIO()
        mem.write(data)
        mem.seek(0)

        captcha = pytesseract.image_to_string(Image.open(mem), config='digits')
        print(captcha)
        return captcha


    def login(self,session=None):
        publickey = self.get_publickey(session=session)
        error_no = '1'

        while error_no != '0':
            r, response = self.get_captcha(session)
            if 'JSESSIONID' in response.cookies.keys():
                self.template['sessionid'] = response.cookies['JSESSIONID']
            ticket = self.recognize_captcha(r, response.content)
            params = {
                'branch_no': '',
                'input_content': 81106500034,
                'ticket': ticket,
                'entrust_way': 9,
                'phone_no': 18645222222,
                'op_station': '18645222222',
                'input_type': 1,
                'mobileKey': r,
                'content_type': '',
                'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
                'funcNo': 300100,
                'account_type': 'credit_userInfo'
            }
            headers = {
                'User-Agent': 'Mozilla/5.0(Linux;U;Android 2.2.1;en-us;Nexus One Build.FRG83) AppleWebKit/553.1(KHTML,like Gecko) Version/4.0 Mobile Safari/533.1',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Expect': '100-continue',
                'Connection': 'Keep-Alive'
            }
            ret = session.post(self.path, data=params, headers=headers).json()
            error_no = ret['error_no']
            if error_no != '0':
                print(ret)
            time.sleep(3)
            if error_no == '0' :
                return ret['DataSet'][0]['jsessionid']
    def onquote(md):
        print(md)


if __name__ == '__main__':     
    session=requests.Session()
    tradetest=TradeTest()
    sessionid=tradetest.login(session)
#     market = MarketHelper(cb=onquote)
#     ret = market.quote(stocks=['SZ:000001|SZ:000002|SZ:000004|SZ:000006'])
#     print(ret)
    headers = {
            'User-Agent': 'Mozilla/5.0(Linux;U;Android 2.2.1;en-us;Nexus One Build.FRG83) AppleWebKit/553.1(KHTML,like Gecko) Version/4.0 Mobile Safari/533.1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Expect': '100-continue',
            'Connection': 'Keep-Alive'
        }
    #股份查询
    funcNo301503 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            #'password':'123123',
            'funcNo': 301503,
            'returnvalue':'error_info\": \"股份查询成功',
            'returncheck' : ['stock_name', 'float_yk_per', 'cost_amount', 'cost_balance', 'last_price', 'stock_code', 'market_value', 'exchange_type', 'float_yk', 'cost_price', 'stock_account', 'exchange_type_name', 'enable_amount', 'share_otd'],
            'Regexp1':'.*results.*share_otd.*stock_account.*enable_amount.*',
            'Regexp2':'.*error_no.{3,4}0.*'
    }
    #response = requests.post("http://123.59.79.146:8089/servlet/json;jsessionid=" + sessionid , data=paramstest,headers=headers)
    #print(json.dumps(paramstest))
    #print(response.json())
    test=InterfaceTests()
    returnparams=test.get_login_token('capp')
    #print(returnparams)
    capptoken=returnparams['capptoken']
    cappuserId=returnparams['cappuserId']
    cappclient_id=returnparams['cappclient_id']
    print(capptoken)

    #资金查询
    funcNo301504 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'money_type':'0',
            'funcNo': 301504,
            'returncheck' :['fetch_balance', 'current_balance', 'money_type_name', 'market_val', 'assert_val', 'enable_balance', 'money_type', 'frozen_balance'],
            'returnvalue':'error_info\": \"资金查询成功'
        }
    #证券信息获取
    funcNo400000 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 400000,
            'returncheck' :['handflag', 'downprice', 'stock_name', 'stock_account', 'stock_code', 'fund_account', 'fundbal', 'lastprice', 'upprice', 'fundavl', 'moneytype', 'stkmaxqty', 'exchange_type', 'orgid', 'stkavl'],
            'returnvalue':'error_info\": \"证券信息获取成功'
        }

    #买入委托成功
    funcNo301501 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301501,
            'entrust_amount':100,
            'stock_account':'A421348695',
            'entrust_bs':0,
            'entrust_price':12.33,
            'exchange_type':2,
            'returncheck' :['entrust_no', 'batch_no', 'report_no'],
            'returnvalue':'error_no\": \"0"'
        }
    #卖出委托成功
    funcNo301501s = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600000',
            'funcNo': 301501,
            'entrust_amount':100,
            'stock_account':'A421348695',
            'entrust_bs':0,
            'entrust_price':18.02,
            'exchange_type':0,
            'returncheck' :['entrust_no', 'batch_no', 'report_no'],
            'returnvalue':'error_info\": \"委托已提交'
        }
    #撤单委托查询
    funcNo301515 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301515,
            'returncheck' :['stock_name', 'entrust_date', 'stock_account', 'entrust_state', 'business_balance', 'entrust_time', 'entrust_amount', 'business_amount', 'entrust_state_name', 'entrust_no', 'business_price', 'exchange_type', 'entrust_price', 'entrust_type', 'exchange_type_name', 'entrust_bs', 'cancel_amount', 'report_no', 'cancel_flag', 'entrust_name', 'stock_code', 'entrust_type_name'],
            'returnvalue':'error_info\": \"委托查询成功'
        }
    bool,temp=test.interfaceTest(tradetest.path + ";jsessionid=" + sessionid,funcNo301515,trade="trade")
    entrust_no=temp['results'][0]['entrust_no']
    print(entrust_no)
    #撤单委托成功
    funcNo301502 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301502,
            'exchange_type':2,
            'entrust_no':entrust_no,
            'batch_flag':0,
            'returnvalue':'error_no\": \"-30150299'
        }
    #今日委托查询
    funcNo301508 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301508,
            'returncheck' :['stock_name', 'entrust_date', 'stock_account', 'entrust_state', 'business_balance', 'entrust_time', 'entrust_type', 'business_amount', 'entrust_state_name', 'entrust_no', 'business_price', 'exchange_type', 'entrust_price', 'entrust_amount', 'exchange_type_name', 'entrust_bs', 'cancel_amount', 'report_no', 'cancel_flag', 'entrust_name', 'stock_code', 'entrust_type_name'],
            'returnvalue':'error_info\": \"委托查询成功'
        }
    #今日成交查询
    funcNo301509 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301509,
            'returncheck' :['real_status', 'stock_name', 'entrust_type', 'stock_account', 'business_price', 'fare0', 'business_balance', 'business_date', 'exchange_type_name', 'fare2', 'report_no', 'entrust_no', 'exchange_type', 'entrust_type_name', 'real_status_name', 'business_time', 'entrust_name', 'stock_code', 'business_amount', 'fare1', 'entrust_bs'],
            'returnvalue':'error_info\": \"当日成交查询成功'
        }
    #历史委托查询
    funcNo301510 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301510,
            'begin_time':'2016-02-10',
            'end_time':'2016-02-16',
            'returnvalue':'error_info\": \"历史委托查询成功'
        }
    #历史成交查询
    funcNo301511 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301511,
            'begin_time':'2016-02-10',
            'end_time':'2016-02-16',
            'returnvalue':'error_info\": \"历史成交查询成功'
        }
    #对帐单查询
    funcNo301520 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301520,
            'begin_date':'2016-02-10',
            'end_date':'2016-02-16',
            'returnvalue':'error_info\": \"对帐单查询成功'
        }
    #当日资金流水查询
    funcNo301516 = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500034,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500034,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            'stock_code':'600004',
            'funcNo': 301516,
            'returnvalue':'error_info\": \"当日资金流水查询成功'
        }

    """小额贷"""
    loanF410624 = {
        "custid": "81106500034",
        "appType": "11",
        "appVer": "102",
        "deviceCode": "",
        "deviceType": "Android",
        "mobilephone": "13300000001",
        "envType": "1",
        "token": capptoken,
        "userId": "772",
        "roleCode": "811",
        "roleName": "西宁市西关路营业部",
        "province": "青海",
        "city": "西宁市",
        "client_id": "imaster_772",
        "trdpwd": "NpSaMnUOkIiGJ2Usk1FL_3DWpn2W6M8P2OIfWhInuTQiHfYVhoGFUhgRAZe1rITYRtEhdxxIultExZCN1b7GeTgkKG_xBrpzIk6BwBZLDWT3hdtmtMnEHvz3k_3JXk4IItcfKOTctoERzcspiQRfa8uV81pr3QJnGVOymiZI87I",
        "sidipwd": "encrypt_rsa:4b879a085b287d021abf08b8c926ff7b4bf2ae965049a0cee46d25b944c25c625a9cad649f6d16f1ce4a5e4e3ec05859938eb225129cbf35b8653891a8c271f411c62b52cc1f2ee077d90e2a60804cd4da34e7a71bfa5970bc8dc89d5218ec7921a64213d64a9d983478679b36c113a16ee2e917eee3a4fc0a879183295da008",
        "branch_no": "0811",
        'returnvalue':'MSG\": \"股票质押客户额度查询成功'
        }

    loanF410625 = {
        "custid": "81106500034",
        "appType": "11",
        "appVer": "102",
        "deviceCode": "",
        "deviceType": "Android",
        "mobilephone": "13300000001",
        "endflag": "1",
        "envType": "1",
        "token": capptoken,
        "userId": "772",
        "roleCode": "811",
        "roleName": "西宁市西关路营业部",
        "province": "青海",
        "city": "西宁市",
        "client_id": "imaster_772",
        "trdpwd": "NpSaMnUOkIiGJ2Usk1FL_3DWpn2W6M8P2OIfWhInuTQiHfYVhoGFUhgRAZe1rITYRtEhdxxIultExZCN1b7GeTgkKG_xBrpzIk6BwBZLDWT3hdtmtMnEHvz3k_3JXk4IItcfKOTctoERzcspiQRfa8uV81pr3QJnGVOymiZI87I",
        "sidipwd": "encrypt_rsa:4b879a085b287d021abf08b8c926ff7b4bf2ae965049a0cee46d25b944c25c625a9cad649f6d16f1ce4a5e4e3ec05859938eb225129cbf35b8653891a8c271f411c62b52cc1f2ee077d90e2a60804cd4da34e7a71bfa5970bc8dc89d5218ec7921a64213d64a9d983478679b36c113a16ee2e917eee3a4fc0a879183295da008",
        "branch_no": "0811",
        'returnvalue':'MSG\": \"股票质押债务合约查询成功'
        }

    loanF410637 = {
        "custid": "81106500034",
        "appType": "11",
        "appVer": "102",
        "deviceCode": "",
        "deviceType": "Android",
        "mobilephone": "13300000001",
        "endflag": "1",
        "envType": "1",
        "begindate":20160218,
        "enddate":20160218,
        "token": capptoken,
        "userId": "772",
        "roleCode": "811",
        "roleName": "西宁市西关路营业部",
        "province": "青海",
        "city": "西宁市",
        "client_id": "imaster_772",
        "trdpwd": "NpSaMnUOkIiGJ2Usk1FL_3DWpn2W6M8P2OIfWhInuTQiHfYVhoGFUhgRAZe1rITYRtEhdxxIultExZCN1b7GeTgkKG_xBrpzIk6BwBZLDWT3hdtmtMnEHvz3k_3JXk4IItcfKOTctoERzcspiQRfa8uV81pr3QJnGVOymiZI87I",
        "sidipwd": "encrypt_rsa:4b879a085b287d021abf08b8c926ff7b4bf2ae965049a0cee46d25b944c25c625a9cad649f6d16f1ce4a5e4e3ec05859938eb225129cbf35b8653891a8c271f411c62b52cc1f2ee077d90e2a60804cd4da34e7a71bfa5970bc8dc89d5218ec7921a64213d64a9d983478679b36c113a16ee2e917eee3a4fc0a879183295da008",
        "branch_no": "0811",
        'returnvalue':'MSG\": \"金易贷业务申请单查询成功'
        }
    loanF410627 = {
        "custid": "81106500034",
        "appType": "11",
        "appVer": "102",
        "deviceCode": "",
        "deviceType": "Android",
        "mobilephone": "13300000001",
        "envType": "1",
        "token": capptoken,
        "userId": "772",
        "roleCode": "811",
        "roleName": "西宁市西关路营业部",
        "province": "青海",
        "city": "西宁市",
        "client_id": "imaster_772",
        "trdpwd": "NpSaMnUOkIiGJ2Usk1FL_3DWpn2W6M8P2OIfWhInuTQiHfYVhoGFUhgRAZe1rITYRtEhdxxIultExZCN1b7GeTgkKG_xBrpzIk6BwBZLDWT3hdtmtMnEHvz3k_3JXk4IItcfKOTctoERzcspiQRfa8uV81pr3QJnGVOymiZI87I",
        "sidipwd": "encrypt_rsa:4b879a085b287d021abf08b8c926ff7b4bf2ae965049a0cee46d25b944c25c625a9cad649f6d16f1ce4a5e4e3ec05859938eb225129cbf35b8653891a8c271f411c62b52cc1f2ee077d90e2a60804cd4da34e7a71bfa5970bc8dc89d5218ec7921a64213d64a9d983478679b36c113a16ee2e917eee3a4fc0a879183295da008",
        "branch_no": "0811",
        'returnvalue':'MSG\": \"产品信息查询成功'
        }
    loanF410642 = {
        "custid": "81106500034",
        "appType": "11",
        "appVer": "102",
        "deviceCode": "",
        "deviceType": "Android",
        "mobilephone": "13300000001",
        "producttype":0,
        "envType": "1",
        "token": capptoken,
        "userId": "772",
        "roleCode": "811",
        "roleName": "西宁市西关路营业部",
        "province": "青海",
        "city": "西宁市",
        "client_id": "imaster_772",
        "trdpwd": "NpSaMnUOkIiGJ2Usk1FL_3DWpn2W6M8P2OIfWhInuTQiHfYVhoGFUhgRAZe1rITYRtEhdxxIultExZCN1b7GeTgkKG_xBrpzIk6BwBZLDWT3hdtmtMnEHvz3k_3JXk4IItcfKOTctoERzcspiQRfa8uV81pr3QJnGVOymiZI87I",
        "sidipwd": "encrypt_rsa:4b879a085b287d021abf08b8c926ff7b4bf2ae965049a0cee46d25b944c25c625a9cad649f6d16f1ce4a5e4e3ec05859938eb225129cbf35b8653891a8c271f411c62b52cc1f2ee077d90e2a60804cd4da34e7a71bfa5970bc8dc89d5218ec7921a64213d64a9d983478679b36c113a16ee2e917eee3a4fc0a879183295da008",
        "branch_no": "0811",
        'returnvalue':'MSG\": \"金易贷可质押证券持仓查询成功'
        }

    loanMultif410629 =  {
        "custid": "81106500034",
        "appType": "11",
        "appVer": "102",
        "deviceCode": "",
        "deviceType": "Android",
        "mobilephone": "13300000001",
        "envType": "1",
        "token": capptoken,
        "userId": "772",
        "roleCode": "811",
        "roleName": "西宁市西关路营业部",
        "province": "青海",
        "city": "西宁市",
        "client_id": "imaster_772",
        "trdpwd": "AHXWXEQclm4PWKyAPMGTCVj7ByMDd_wqPu78Up2w_fvhi1e1wa_acRm6I1njdFaGeFZIfSwwd3ldCgzKc6yFB7oXwatzefm-J05ZATywkLXP1aTuxp7mmCn_AKTTfpb0VB6YOgsquJAixJW3SoAoEd-7O2yMVsXmnffKL9dJXKQ",
        "sidipwd": "encrypt_rsa:2c52fe290a2311990b1ae053f6472cc9e1f8c0b479f1eef64b40e216a6b11bbf4e33aae1685bbec1a3f1f02dba98cb26d2b621557d9ee3aa745a491382108d530fb63b3dfba3eaa169005043d3df78f69ae9150d873227fbfef0d81728c99aac85811e57634632aeefc31f1ee4faf94500fd14ce2ee3e0e34d86054448227233",
        "branch_no": "0811",
        'returnvalue':'code\": 0',
        "loans": [{
                "fundid": "81106500034",
                "stkname": "中粮生化",
                "market": 0,
                "stkcode": "000930",
                "secuid": "0104021859",
                "orderqty": 1200,
                "orderamt": 5165,
                "producttype": "1",
                "ghdays": 366,
                "funduse": ""}]
    }

    #股份查询-->资金查询-->证券信息获取-->买入委托成功
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301503,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301504,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo400000,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301501,trade=trade)
    #股份查询-->资金查询-->证券信息获取-->卖出委托成功
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301503,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301504,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo400000,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301501s,trade=trade)
    #委托查询-->撤单委托成功
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301515,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301502,trade=trade)
    #查询今日委托-->查询今日成交-->查询历史委托-->查询历史成交-->查询对账单-->查询当日资金流水
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301508,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301509,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301510,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301511,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301520,trade=trade)
    test.interfaceTest(path + ";jsessionid=" + sessionid,funcNo301516,trade=trade)
    #小额贷
    #我的融资查询-->股票质押客户额度查询-->股票质押债务合约查询成功-->金易贷业务申请单查询成功-->产品信息查询成功
    test.interfaceTest(capppath + "/loan/f410624",loanF410624,trade=trade)
    test.interfaceTest(capppath + "/loan/f410625",loanF410625,trade=trade)
    test.interfaceTest(capppath + "/loan/f410637",loanF410637,trade=trade)
    test.interfaceTest(capppath + "/loan/f410627",loanF410627,trade=trade)
    #股票质押资金周转-->金易贷可质押证券持仓查询-->股票质押客户额度查询-->股票质押申请成功
    test.interfaceTest(capppath + "/loan/f410642",loanF410642,trade=trade)
    test.interfaceTest(capppath + "/loan/f410624",loanF410624,trade=trade)
    test.interfaceTest(capppath + "/loan/multif410629",loanMultif410629)
    #股票质押买卖股票-->金易贷可质押证券持仓查询-->股票质押客户额度查询-->股票质押申请成功
    test.interfaceTest(capppath + "/loan/f410642",loanF410642,trade=trade)
    test.interfaceTest(capppath + "/loan/f410624",loanF410624,trade=trade)
    test.interfaceTest(capppath + "/loan/multif410629",loanMultif410629)

    #接口返回数据格式校验
    #test.regularTest(path + ";jsessionid=" + sessionid,funcNo301503,trade=trade)
    trade=InterfaceTests()
    #股份查询-->资金查询-->证券信息获取-->买入委托成功
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo301503,trade=trade)
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo301504,trade=trade)
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo400000,trade=trade)
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo301501,trade=trade)
    #卖出委托成功
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo301501s,trade=trade)
    #委托查询-->撤单委托成功
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo301515,trade=trade)
    #查询今日委托-->查询今日成交-->查询对账单
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo301508,trade=trade)
    trade.tradeCheck(path + ";jsessionid=" + sessionid,funcNo301509,trade=trade)
  
