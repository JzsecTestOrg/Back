"""
Created on Fri Jul 17 11:38:25 2015

@author: jinghua
"""

from InterfaceTests import InterfaceTests
class Trade:
    #股份查询
    @staticmethod
    def funcNo301503():
        paramstest = {
            'op_station': '1%7Cfe80%3A%3Abe3a%3Aeaff%3Afebb%3A2a75%25wlan0%7Cbc%3A3a%3Aea%3Abb%3A2a%3A75%7C867567026087643%7C0000000000000000%7Cnull%7C%7C',
            'sessionid': sessionid ,
            'fund_account': 81106500059,
            'entrust_way': 'G',
            'branch_no': '0811',
            'cust_code': 81106500059,
            'password': 'encrypt_rsa%3A341edebdeef52e3d3cbdf92f5aa5af7a1e29c6f899fb421382b755a9184d18be0c57aacb3d33917996d41176ed3f42c04e85d555f9aa361fe270c3537d97c461fb6f8792c99426968529019f9cb0d568cb7f191df98f9dce767062e2cdfe5a7951ee6c7751d0e135fbda334ea1ca7ab185448de4ec5692deedef56ff1cadc7d5',
            #'password':'123123',
            'funcNo': 301503
        }
        path=imurl + '/portfolio/listmine'
        test=InterfaceTests()
        if iteration==True:
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
