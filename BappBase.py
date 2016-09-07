"""
Created on Fri Jul 17 11:38:25 2015

@author: jinghua
"""

from InterfaceTests import *

#测试环境
bappurl='http://t.a.jzsec.com'
cappurl='http://t.c.jzsec.com'
imurl='http://mt.jzsec.com'
# 开发环境
# bappurl='http://bapp.tlan.com.cn'
# cappurl='http://capp.tlan.com.cn'
# imurl='http://immanager.tlan.com.cn'
class Capp:

    """V2.0组合"""
    #我的组合列表
    @staticmethod
    def portfolioListmine(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/listmine'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #组合持仓查询
    @staticmethod
    def portfolioListholdings(iteration,mobilephone,appVer,envType,token,client_id,deviceType,userId,deviceCode,appType,symbols,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbols']=symbols
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/listholdings'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #发表博主观点
    @staticmethod
    def portfolioAddcomment(iteration,mobilephone,appVer,envType,token,client_id,deviceType,userId,deviceCode,appType,symbol,content,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['content']=content
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/addcomment'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #创建组合
    @staticmethod
    def portfolioCreate(iteration,mobilephone,appVer,envType,token,client_id,deviceType,userId,deviceCode,appType,name,cash,rbs,stock_market,stock_symbol,stock_name,prev_weight,target_weight,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['name']=name
        params['cash']=cash
        params['rbs']=rbs
        params['stock_market']=stock_market
        params['stock_symbol']=stock_symbol
        params['stock_name']=stock_name
        params['prev_weight']=prev_weight
        params['target_weight']=target_weight
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/create'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #博主观点列表
    @staticmethod
    def portfolioListcomments(iteration,mobilephone,appVer,envType,token,client_id,deviceType,userId,deviceCode,appType,symbol,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/listcomments'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #关注组合
    @staticmethod
    def portfolioAddfavourite(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,symbol,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/addfavourite'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #我的关注列表
    @staticmethod
    def portfolioListfavourites(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,symbol,owner,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['owner']=owner
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/listfavourites'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #取消关注
    @staticmethod
    def portfolioDeletefavourite(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,symbol,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/deletefavourite'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #组合详情
    @staticmethod
    def portfolioDetails(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,symbol,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/details'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #组合调仓
    @staticmethod
    def portfolioRebalance(iteration,mobilephone,cappver,envType,token,client_id,deviceType,userId,deviceCode,appType,name,cash,rbs,stock_market,stock_symbol,stock_name,prev_weight,target_weight,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['name']=name
        params['cash']=cash
        params['rbs']=rbs
        params['stock_market']=stock_market
        params['stock_symbol']=stock_symbol
        params['stock_name']=stock_name
        params['prev_weight']=prev_weight
        params['target_weight']=target_weight
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/rebalance'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #所有组合列表
    @staticmethod
    def portfolioListall(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/listall'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #组合调仓历史记录
    @staticmethod
    def portfolioRebalancinghistories(iteration,mobilephone,appVer,envType,token,client_id,deviceType,userId,deviceCode,appType,symbol,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/rebalancinghistories'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #组合调仓历史记录
    @staticmethod
    def portfolioRebalancinghistoriespaged(iteration,mobilephone,appVer,envType,token,client_id,deviceType,userId,deviceCode,appType,symbol,pageSize,page,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['page']=page
        params['pageSize']=pageSize
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/rebalancinghistoriespaged'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #通过组合名称或编号搜索组合
    @staticmethod
    def portfolioSearch(iteration,mobilephone,appVer,envType,token,client_id,deviceType,userId,deviceCode,appType,symbol,input,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['client_id']=client_id
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['symbol']=symbol
        params['input']=input
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/search'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    """V2.0 Capp"""
    #发送验证码
    @staticmethod
    def cuserSendauthcode(iteration,mobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/sendauthcode'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #注册接口
    @staticmethod
    def cuserRegister(iteration,mobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,verifyCode,password,verifyPassword,fromwhichsys,nickName,agree,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['verifyCode']=verifyCode
        params['password']=password
        params['verifyPassword']=verifyPassword
        params['fromwhichsys']=fromwhichsys
        params['nickName']=nickName
        params['agree']=agree
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/register'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #登录接口
    @staticmethod
    def cuserLogin(iteration,mobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,password,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['password']=password
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/login'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #获取指定单页接口
    @staticmethod
    def sysstaticGetonepage(iteration,mobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/sysstatic/getonepage'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #模糊获取经纪人
    @staticmethod
    def cuserSearchbroker(iteration,mobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/searchbroker'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #通过手机号获取客户号
    @staticmethod
    def cuserGetcustid(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/getcustid'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #投资大师开户保存证件号
    @staticmethod
    def cuserSaveidentity(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,openMobile,idno,custname,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['openMobile']=openMobile
        params['idno']=idno
        params['custname']=custname
        params['returnvalue']=returnvalue
        path=cappurl + 'cuser/saveidentity'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #检验找回密码验证码
    @staticmethod
    def cuserCheckresetpasscode(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,verifyCode,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['verifyCode']=verifyCode
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/checkresetpasscode'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #重置密码
    @staticmethod
    def cuserResetpass(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,password,verifyCode,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['password']=password
        params['verifyCode']=verifyCode
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/resetpass'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #通过客户号获取手机号
    @staticmethod
    def cuserGetmobilephone(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,custId,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['custId']=custId
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/getmobilephone'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #验证登录token
    @staticmethod
    def cuserLoginbytoken(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/loginbytoken'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #投资大师意见反馈
    @staticmethod
    def cuserSendadvice(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,content,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['content']=content
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/sendadvice'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #获取营业部列表
    @staticmethod
    def roleRolelist(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/role/rolelist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #登录是否需要验证码
    @staticmethod
    def cuserIsneedverify(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/isneedverify'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #开户状态变更/流程记录
    @staticmethod
    def cuserUpdateprogress(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,progress,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['progress']=progress
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/updateprogress'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #投资大师开户选择经纪人及营业部
    @staticmethod
    def cuserRegsavebroker(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,bid,role,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['bid']=bid
        params['role']=role
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/regsavebroker'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #找回密码短信验证码
    @staticmethod
    def cuserSendresetpasscode(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/sendresetpasscode'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股申购输入页面
    @staticmethod
    def newshareInput(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/input'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股申购请求提交页面
    @staticmethod
    def newshareConfirm(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['enddate']="20160229"
        params['shares']=[
        {
            "market":"0",
            "stkcode":"300500",
            "price":20.91,
            "qty":1000
        }]
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/confirm'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #待上市新股列表
    @staticmethod
    def newshareTobelisted(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/tobelisted'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股申购历史
    @staticmethod
    def newshareApplyhistory(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/applyhistory'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股申购主页数据
    @staticmethod
    def newshareProfile(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/profile'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股申购中签历史
    @staticmethod
    def newshareF411560(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['begindate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/f411560'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股申购中签历史
    @staticmethod
    def newshareF411547(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['begindate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/f411547'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股申购中签历史
    @staticmethod
    def newshareF411518(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['begindate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/f411518'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #新股信息明细
    @staticmethod
    def newshareDetails(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['stock_code']="002790"
        params['password']="qaz123"
        params['custid']="81106500202"
        params['trdpwd']="g0JvSpX0Tx4SoCKVGPib3quuIazVkFzmf8bACPfQGxJ0jo1xRdK2Iiq3GP9ghYGoRR-khCX0POIWdChsL-y_cfXQ67m8WNYMYX7-DGdXrlhh5q3Krilnmjl5cDlqguyEFymVO6i-Cv47qn2D187GYkts3lAcvOQxn9_uDWZrgmU"
        params['market']="0"
        params['strdate']="20160210"
        params['begindate']="20160210"
        params['enddate']="20160229"
        params['returnvalue']=returnvalue
        path=cappurl + '/newshare/details'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #检查客户号是否已被绑定
    @staticmethod
    def cuserCheckcustidbind(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,cust_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_id']=cust_id
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/checkcustidbind'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #客户号绑定
    @staticmethod
    def cuserBindnewcustid(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,cust_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_id']=cust_id
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/bindnewcustid'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #全局唯一索引查询开户信息（查询中登 ）
    @staticmethod
    def cuserCheckcanopen(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['province']="北京"
        params['roleName']="北京分公司"
        params['idno']="80310000049"
        params['custname']="王小三"
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/checkcanopen'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #查询更新身份证进度
    @staticmethod
    def cuserGetfreshidstatus(iteration,mobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/getfreshidstatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #上传新身份证信息
    @staticmethod
    def cuserUploadnewidentity(iteration,cappmobilephone,cappver,cenvType,capptoken,deviceType,userId,deviceCode,cappType,custid,trdpwd,id_code,id_begain_date,id_end_date,cust_name,id_addr,id_iss_agcy,id_sex,id_birthday,id_front_bucket,id_front_key, id_back_bucket,id_back_key,id_inhand_bucket,id_inhand_key,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=cenvType
        params['token']=capptoken
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=cappType
        params['returnvalue']=returnvalue
        params['custid']=custid
        params['trdpwd']=trdpwd
        params['id_code']=id_code
        params['id_begain_date']=id_begain_date
        params['id_end_date']=id_end_date
        params['cust_name']=cust_name
        params['id_addr']=id_addr
        params['id_iss_agcy']=id_iss_agcy
        params['id_sex']=id_sex
        params['id_birthday']=id_birthday
        params['id_front_bucket']=id_front_bucket
        params['id_front_key']=id_front_key
        params['id_back_bucket']=id_back_bucket
        params['id_back_key']=id_back_key
        params['id_inhand_bucket']=id_inhand_bucket
        params['id_inhand_key']=id_inhand_key

        path=cappurl + '/cuser/uploadnewidentity'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)


    #各分支机构佣金协议H5页面
    @staticmethod
    def cuserBrokeragedoc(iteration,cappmobilephone,cappver,cenvType,capptoken,deviceType,userId,deviceCode,cappType,role_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=cenvType
        params['token']=capptoken
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=cappType
        params['role_id']=role_id
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/brokeragedoc'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #查看身份证信息，同时返回是否有身份证正在更新
    @staticmethod
    def cuserGetidentity(iteration,cappmobilephone,cappver,cenvType,capptoken,deviceType,userId,deviceCode,cappType,custid,trdpwd,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=cenvType
        params['token']=capptoken
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=cappType
        params['custid']=custid
        params['trdpwd']=trdpwd
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/getidentity'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #风险测评H5接口
    @staticmethod
    def cuserRiskevaluation(iteration,cappmobilephone,cappver,cenvType,capptoken,deviceType,userId,deviceCode,cappType,fromid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=cenvType
        params['token']=capptoken
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=cappType
        params['from']=fromid
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/riskevaluation'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #处理投诉信息
    @staticmethod
    def cuserComfirmcomplaint(iteration,cappmobilephone,cappver,cenvType,capptoken,deviceType,userId,deviceCode,cappType,broker_name,content,contact_name,contact_mobile,broker_mobile,cert_num,attachments,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=cenvType
        params['token']=capptoken
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=cappType
        params['broker_name']=broker_name
        params['content']=content
        params['contact_name']=contact_name
        params['contact_mobile']=contact_mobile
        params['broker_mobile']=broker_mobile
        params['cert_num']=cert_num
        params['attachments']=attachments
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/confirmcomplaint'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #交易日及交易时间段获取
    @staticmethod
    def portfolioIstradingday(iteration,cappmobilephone,cappver,cenvType,capptoken,deviceType,userId,deviceCode,cappType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=cenvType
        params['token']=capptoken
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=cappType
        params['returnvalue']=returnvalue
        path=cappurl + '/portfolio/istradingday'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #注册短信验证码
    @staticmethod
    def cuserSendauthcode(iteration,cappmobilephone,cappver,cenvType,capptoken,deviceType,userId,deviceCode,cappType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=cenvType
        params['token']=capptoken
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=cappType
        params['returnvalue']=returnvalue
        path=cappurl + '/cuser/sendauthcode'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)









class Bapp:

    def __init__(self):

        self.bappurl='http://t.a.jzsec.com'

    """V2.0 IM"""
    #IM同意添加好友
    @staticmethod
    def friendConfirmfriend(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,myClientId,fClientId,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['myClientId']=myClientId
        params['fClientId']=fClientId
        path=imurl + '/friend/confirmfriend'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM申请好友操作接口
    @staticmethod
    def friendFriendapply(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,fromid,targetid,fromtype,targettype,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['fromid']=fromid
        params['targetid']=targetid
        params['fromtype']=fromtype
        params['targettype']=targettype
        path=imurl + '/friend/friendapply'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params,returnvalue)
        else:
            test.iterationTest(path, params,returnvalue)


    #IM获取好友列表
    @staticmethod
    def namelistGetfriendlist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/namelist/getfriendlist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM获取好友or群成员详情
    @staticmethod
    def namelistGetimuserdetail(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,target_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['target_client_id']=target_client_id
        params['returnvalue']=returnvalue
        path=imurl + '/namelist/getimuserdetail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #IM通过通讯录获取通讯录
    @staticmethod
    def namelistGetimphonebook(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,phone_book,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['phone_book']=phone_book
        params['returnvalue']=returnvalue
        path=imurl + '/namelist/getimphonebook'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM获取被申请列表
    @staticmethod
    def namelistInvmelist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/namelist/invmelist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM获取所有有效的对话ID
    @staticmethod
    def namelistGetconvlist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/namelist/getconvlist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM删除好友操作接口
    @staticmethod
    def friendFrienddelete(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,fromid,targetid,deletetype,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['fromid']=fromid
        params['targetid']=targetid
        params['deletetype']=deletetype
        params['returnvalue']=returnvalue
        path=imurl + '/friend/frienddelete'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM邀请好友进群
    @staticmethod
    def groupAddmember(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,tclient_ids,gid,user_name,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['tclient_ids']=tclient_ids
        params['gid']=gid
        params['user_name']=user_name
        params['returnvalue']=returnvalue
        path=imurl + '/group/addmember'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM 确认/驳回 群邀请（个人）
    @staticmethod
    def groupUserconfirm(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,gid,agree,fclientid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['fclientid']=fclientid
        params['gid']=gid
        params['agree']=agree
        params['returnvalue']=returnvalue
        path=imurl + '/group/userconfirm'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM 管理员同意邀请进群
    @staticmethod
    def groupManagerconfirm(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,gid,agree,tclient_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['gid']=gid
        params['agree']=agree
        params['tclient_id']=tclient_id
        params['returnvalue']=returnvalue
        path=imurl + '/group/managerconfirm'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM创建普通群
    @staticmethod
    def groupCreategroup(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,client_ids,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['client_ids']=client_ids
        params['returnvalue']=returnvalue
        path=imurl + '/group/creategroup'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #拉好友进群好友列表
    @staticmethod
    def namelistGroupfriendlist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,group_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['group_id']=group_id
        params['returnvalue']=returnvalue
        path=imurl + '/namelist/groupfriendlist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM个人聊天详情页接口
    @staticmethod
    def namelistPersondetail(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,room_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['room_id']=room_id
        params['returnvalue']=returnvalue
        path=imurl + '/namelist/persondetail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #创建默认群
    @staticmethod
    def groupCreatedefaultgroup(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,bid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['bid']=bid
        params['returnvalue']=returnvalue
        path=imurl + '/group/createdefaultgroup'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #Capp用户加入默认群
    @staticmethod
    def groupJoindefaultgroup(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,bid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['bid']=bid
        path=imurl + '/group/joindefaultgroup'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM 群所有成员所有组合列表
    @staticmethod
    def groupMemberportfolios(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,gid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['gid']=gid
        params['returnvalue']=returnvalue
        path=imurl + '/group/memberportfolios'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM 群邀请列表
    @staticmethod
    def groupGroupinvlist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,username,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['username']=username
        params['returnvalue']=returnvalue
        path=imurl + '/group/groupinvlist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)




    #IM 用户所在的群
    @staticmethod
    def groupGrouplist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/group/grouplist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #获取群组合基本信息
    @staticmethod
    def groupGetfolio(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,gid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['gid']=gid
        params['returnvalue']=returnvalue
        path=imurl + '/group/getfolio'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #IM 修改群信息
    @staticmethod
    def groupUpdategroup(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,gid,content,type,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['gid']=gid
        params['content']=content
        params['type']=type
        params['returnvalue']=returnvalue
        path=imurl + '/group/updategroup'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #IM 安卓获取静音会话列表
    @staticmethod
    def androidGetnodisturblistmember(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,conv_ids,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['conv_ids']=conv_ids
        params['returnvalue']=returnvalue
        path=imurl + '/group/androidgetnodisturblistmember'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #经纪人离职再挂靠成功
    @staticmethod
    def groupBuseron(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,bid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['bid']=bid
        path=imurl + '/group/buseron'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #查询免打扰和是否显示真实姓名
    @staticmethod
    def groupGuerystatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/group/querystatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #系统消息免打扰
    @staticmethod
    def groupSetmuteall(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,status,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['status']=status
        params['returnvalue']=returnvalue
        path=imurl + '/group/setmuteall'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #手机号搜索联系人
    @staticmethod
    def friendSfbyphone(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,searchphone,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['searchphone']=searchphone
        params['returnvalue']=returnvalue
        path=imurl + '/friend/sfbyphone'
        print(imurl)
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #单个会话设置免打扰
    @staticmethod
    def groupSetmuteone(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,status,gid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['status']=status
        params['gid']=gid
        params['returnvalue']=returnvalue
        path=imurl + '/group/setmuteone'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #单个会话免打扰状态查询
    @staticmethod
    def groupQuerystatusone(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,gid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['gid']=gid
        params['returnvalue']=returnvalue
        path=imurl + '/group/querystatusone'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #检查某手机号及Token组合是否已登录
    @staticmethod
    def systemChecktoken(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=imurl + '/system/checktoken'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #capp 股票、组合搜索
    @staticmethod
    def portfolioSearchsp(iteration,mobilephone,appver,cenvType,token,deviceType,userId,deviceCode,appType,input,type,count,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appver
        params['envType']=cenvType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['input']=input
        params['type']=type
        params['count']=count
        params['returnvalue']=returnvalue
        path=imurl + '/portfolio/searchsp'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)











    """V2.0 Bapp"""
    #app初始化
    @staticmethod
    def systemInit(iteration,mobilephone,envType,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """客户页面从通讯录导入客户"""
        params={}
        params['mobilephone'] = mobilephone
        params['envType']=envType
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/system/init'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
            return test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #发送验证码
    @staticmethod
    def systemSendauthcode(iteration,mobilephone,appver,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/system/sendauthcode'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #登录
    @staticmethod
    def systemLogin(iteration,mobilephone,appver,envType,token,deviceType,userId,deviceCode,appType,password,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['password']=password
        params['returnvalue']=returnvalue
        path=bappurl + '/system/login'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #注册接口
    @staticmethod
    def systemRegister(iteration,mobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,verifyCode,password,verifyPassword,fromwhichsys,nickName,agree,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['verifyCode']=verifyCode
        params['password']=password
        params['verifyPassword']=verifyPassword
        params['fromwhichsys']=fromwhichsys
        params['nickname']=nickName
        params['agree']=agree
        params['returnvalue']=returnvalue
        path=bappurl + '/system/register'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #114版获取经纪人推荐列表的统计数据
    @staticmethod
    def syssharelinkShowstatistics(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """客户页面从通讯录导入客户"""
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/syssharelink/showstatistics'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)



    #客户
    @staticmethod
    def bcustomer_getcuserbymobilephones(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,customerMobilephones,returnvalue=None,inputp=None,outputp=None):
        """客户页面从通讯录导入客户"""
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['customerMobilephones']=customerMobilephones
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/getcuserbymobilephones'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bcustomer_modifycustomers(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,customers,returnvalue=None,inputp=None,outputp=None):
        """手动添加客户"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['customers']=customers
        params['returnvalue']=returnvalue
        #print(bappurl)
        path=bappurl + '/bcustomer/modifycustomers'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    @staticmethod
    def bcustomer_syncnew (iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/syncnew'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bcustomer_syncnewnotice (iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cid,returnvalue=None,inputp=None,outputp=None):
        """更新客户列表信息"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cid']=cid
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/syncnewnotice'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #注册

    @staticmethod
    def bcustomer_getcuserbymobilephones(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,customerMobilephones,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['customerMobilephones']=customerMobilephones
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/getcuserbymobilephones'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    #代办
    @staticmethod
    def follow_followlist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,flag=None):
        """获取待办列表"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['flag']=flag
        params['returnvalue']=returnvalue
        path=bappurl + '/follow/followlist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def message_messagelist(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,flag,returnvalue=None,inputp=None,outputp=None):
        """获取系统消息信息"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['flag']=flag
        params['returnvalue']=returnvalue
        path=bappurl + '/message/messagelist'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def followdone_followdones(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,flag,returnvalue=None,inputp=None,outputp=None):
        """获取跟进信息"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['flag']=flag
        params['returnvalue']=returnvalue
        path=bappurl + '/followdone/followdones'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #推荐
    @staticmethod
    def syssharelink_getproduct(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取推荐产品列表（new）"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/syssharelink/getproduct'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)



    @staticmethod
    def bkpi_gethistorykpi(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取历史业绩"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/bkpi/gethistorykpi'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bkpi_getkpibymonth(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取本月业绩"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/bkpi/getkpibymonth'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_changeinfo(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,value,appType,key,returnvalue=None,inputp=None,outputp=None):
        """更新联系人信息
            "key":"address"：更新地址信息
            "key":"mail"：更新邮件信息
            "key":"nickname"：更新昵称信息
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['value']=deviceCode
        params['appType']=appType
        params['key']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/changeinfo'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_getuserstatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取身份证上传和认证相关信息
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/getuserstatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def sysattachment_ucloudtoken(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """身份证信息验证
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/sysattachment/ucloudtoken'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_uploadconfirm(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,role_id,returnvalue=None,inputp=None,outputp=None):
        """身份证信息核对
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['role_id']=role_id
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/uploadconfirm'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    def system_editinfo(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,sex,issue_authority,identityNum,validity,name,returnvalue=None,inputp=None,outputp=None):
        """身份证信息提交
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['sex']=sex
        params['issue_authority']=issue_authority
        params['identityNum']=identityNum
        params['validity']=validity
        params['name']=name
        params['returnvalue']=returnvalue
        path=bappurl + '/system/editinfo'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)




    @staticmethod
    def train_train(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,chapterId,returnvalue=None,inputp=None,outputp=None):
        """在线培训获取相关信息
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['chapterId']=chapterId
        params['returnvalue']=returnvalue
        path=bappurl + '/train/train'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bcustomer_getbrokerageresults(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取佣金调整记录信息
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/getbrokerageresults'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def sysstatic_getonepage(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,title,returnvalue=None,inputp=None,outputp=None):
        """获取经纪宝的相关说明内容
        title的取值分别为：brokerage，bapp_sign，brokers_manage，what_is_full_commission
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['title']=title
        params['returnvalue']=returnvalue
        path=bappurl + '/sysstatic/getonepage'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)



    @staticmethod
    def finance_monthearn(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,date,returnvalue=None,inputp=None,outputp=None):
        """查询月收入详细
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['date']=date
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/monthearn'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def finance_mywithdraw(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,date,returnvalue=None,inputp=None,outputp=None):
        """查询我的支取
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['date']=date
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/mywithdraw'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def finance_withdraw(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """经纪人提现接口
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/withdraw'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)


    @staticmethod
    def system_resetpass(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,password,verifyPassword,verifyCode,returnvalue=None,inputp=None,outputp=None):
        """重置密码
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['verifyPassword']=verifyPassword
        params['password']=password
        params['verifyCode']=verifyCode
        params['returnvalue']=returnvalue
        path=bappurl + '/system/resetpass'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    @staticmethod
    def bcustomer_getmycusers115(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,customerMobilephones,returnvalue=None,inputp=None,outputp=None):
        """获取客户详情
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['customerMobilephones']=customerMobilephones
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/getmycusers115'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bcustomer_getmyimusers(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,client_id,returnvalue=None,inputp=None,outputp=None):
        """通过经纪人手机号查询其客户资料
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['client_id']=client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/getmyimusers'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def syssharelink_getproduct(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取推荐信息
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/syssharelink/getproduct'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def syssharelink_showstatistics(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """推荐列表
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/syssharelink/showstatistics'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def syssharelink_showsrecomdetails(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,kind,returnvalue=None,inputp=None,outputp=None):
        """获取推荐列表中的详细状态
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['kind']=kind
        params['returnvalue']=returnvalue
        path=bappurl + '/syssharelink/showsrecomdetails'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bkpi_gethistorykpi(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取历史业绩
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/bkpi/gethistorykpi'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bkpi_getkpibymonth(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取本月业绩
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/bkpi/getkpibymonth'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_getbuserinfo(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取个人信息
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/getbuserinfo'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_getuserstatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取经纪人挂靠状态
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/getuserstatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def bcustomer_getbrokerageresults(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取佣金调整记录
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/bcustomer/getbrokerageresults'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def system_getinvitecode(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """获取邀请码
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/system/getinvitecode'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_saveavater(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,filePath,bucket,authorization,key,url,returnvalue=None,inputp=None,outputp=None):
        """保存上传头像
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['filePath']=filePath
        params['bucket']=bucket
        params['authorization']=authorization
        params['filePath']=filePath
        params['key']=key
        params['url']=url
        path=bappurl + '/buser/saveavater'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_changeinfo(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,key,value,returnvalue=None,inputp=None,outputp=None):
        """修改昵称"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['key']=key
        params['value']=value
        path=bappurl + '/buser/changeinfo'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_getlastexpress(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        """已寄出快递"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/getlastexpress'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    @staticmethod
    def buser_contractmail(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,mail,returnvalue=None,inputp=None,outputp=None):
        """确认并发送合同"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['mail']=mail
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/contractmail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    """v2.1"""

    #经纪人本月业绩的客户交易额v2.0.1
    @staticmethod
    def financeThismonthperf201(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,date,kind,page,returnvalue=None,inputp=None,outputp=None):
        """确认并发送合同"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['date']=date
        params['kind']=kind
        params['page']=page
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/thismonthperf201'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #获取客户指定月份交易详情（210新增）
    @staticmethod
    def financeGetcustmonthtradedetailhperf201(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,date,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        """确认并发送合同"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['date']=date
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/getcustmonthtradedetail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #114版本获取经纪人的财务数据
    @staticmethod
    def financeGetbidfininfo(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):

        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/getbidfininfo'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    @staticmethod
    def buserSaveregisterfile(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,filePath,bucket,authorization,key,url,returnvalue=None,inputp=None,outputp=None):
        """保存上传头像
        """
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['filePath']=filePath
        params['bucket']=bucket
        params['authorization']=authorization
        params['filePath']=filePath
        params['key']=key
        params['url']=url
        path=bappurl + '/buser/saveregisterfile'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #Bapp获取指定客户的每月交易额210
    @staticmethod
    def financeGetcustmonthtradeamount(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        """确认并发送合同"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/getcustmonthtradeamount'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #临时大头照上传检查
    @staticmethod
    def buserCheckmugshotstatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        """确认并发送合同"""
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/checkmugshotstatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #刷脸结果check与保存
    @staticmethod
    def systemFacesignin(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,bucket,key,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['key']=key
        params['bucket']=bucket
        params['returnvalue']=returnvalue
        path=bappurl + '/system/facesignin'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #上传验证码
    @staticmethod
    def systemVerifycodesignin(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,verifyCode,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['verifyCode']=verifyCode
        params['returnvalue']=returnvalue
        path=bappurl + '/system/verifycodesignin'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #是否需要刷脸签到检查
    @staticmethod
    def systemCheckfacesignin(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/system/checkfacesignin'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #获取经纪人强制考试状态
    @staticmethod
    def systemCheckexamstatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/system/checkexamstatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #v2.4
    #期货居间人挂靠培训入口
    @staticmethod
    def jointtrainTrain(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,train_type,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['train_type']=train_type
        params['returnvalue']=returnvalue
        path=bappurl + '/jointtrain/train'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人培训做题
    @staticmethod
    def jointtrainDdoquestion(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,questionId,answer,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['questionId']=questionId
        params['answer']=answer
        params['returnvalue']=returnvalue
        path=bappurl + '/jointtrain/doquestion'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)

    #期货居间人培训显示题目列表
    @staticmethod
    def jointtrainShowquestion(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,chapterId,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['chapterId']=chapterId
        params['returnvalue']=returnvalue
        path=bappurl + '/jointtrain/showquestion'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人培训章节显示
    @staticmethod
    def jointtrainShowchapter(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,chapterId,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['chapterId']=chapterId
        params['returnvalue']=returnvalue
        path=bappurl + '/jointtrain/showchapter'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人培训章节显示
    @staticmethod
    def jointtrainShowchapter(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,chapterId,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['chapterId']=chapterId
        params['returnvalue']=returnvalue
        path=bappurl + '/jointtrain/showchapter'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人获取培训履历
    @staticmethod
    def bfutureuserGettrainhis(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/bfutureuser/gettrainhis'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人获取合同审核履历
    @staticmethod
    def bfutureuserGetcontractaudithis(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/bfutureuser/getcontractaudithis'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人获取SAC审核履历
    @staticmethod
    def bfutureuserGetsacaudithis(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/bfutureuser/getsacaudithis'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人单独发送合同
    @staticmethod
    def bfutureuserContractmail(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,mail,address,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['mail']=mail
        params['address']=address
        params['returnvalue']=returnvalue
        path=bappurl + '/bfutureuser/contractmail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #期货居间人客户管理
    @staticmethod
    def bfutureuserFinishaffiliated(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/bfutureuser/finishaffiliated'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #经纪人状态获取
    @staticmethod
    def buserGetuserstatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/getuserstatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        else:
            test.iterationTest(path, params)
    #经纪宝意见反馈
    @staticmethod
    def buserSendadvice(iteration,cappmobilephone,cappver,envType,token,deviceType,userId,deviceCode,appType,content,parent_adv_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone'] = cappmobilephone
        params['appVer']=cappver
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['content']=content
        params['parent_adv_id']=parent_adv_id
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/sendadvice'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #将合同发送至电子邮箱
    @staticmethod
    def buserContractmail(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,mail,futureSelected,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['mail']=mail
        params['futureSelected']=futureSelected
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/contractmail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #远程面谈刷脸验证
    @staticmethod
    def interviewFacevalidate(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/interview/facevalidate'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #远程面谈刷脸前检查是否满足条件
    @staticmethod
    def interviewFacecheck(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/interview/facecheck'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #远程面谈内容确认页
    @staticmethod
    def interviewRemotecontent(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/interview/remotecontent'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #合规面谈状态查询
    @staticmethod
    def interviewStatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['returnvalue']=returnvalue
        path=bappurl + '/interview/status'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #面谈成功接口
    @staticmethod
    def interviewSuccess(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,call_type,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['call_type']=call_type
        params['returnvalue']=returnvalue
        path=bappurl + '/interview/success'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #执业证书回执确认
    @staticmethod
    def buserConfirmsacreceive(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cust_client_id,call_type,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['cust_client_id']=cust_client_id
        params['call_type']=call_type
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/confirmsacreceive'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #经纪人位置信息上传接口
    @staticmethod
    def buserUploadposition(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,longitude,latitude,province,city,address,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['longitude']=longitude
        params['latitude']=latitude
        params['province']=province
        params['city']=city
        params['address']=address
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/uploadposition'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #经纪人同意或者拒绝团队长修改绩效提成比例
    @staticmethod
    def teamorderAgreeratio(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,teamorderid,isagree,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['teamorderid']=teamorderid
        params['isagree']=isagree
        params['returnvalue']=returnvalue
        path=bappurl + '/teamorder/agreeratio'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)
    #接受or拒绝团队长的邀请or踢出
    @staticmethod
    def teamorderAcceptinvite(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,teamorderid,accept,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['teamorderid']=teamorderid
        params['accept']=accept
        params['returnvalue']=returnvalue
        path=bappurl + '/teamorder/acceptinvite'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #经纪宝启动检查信息
    @staticmethod
    def messageGetdailymsg(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/message/getdailymsg'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #获取绩效提成比例状态信息
    @staticmethod
    def teamorderGetratiostatus(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,teamorderid,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['teamorderid']=teamorderid
        params['returnvalue']=returnvalue
        path=bappurl + '/teamorder/getratiostatus'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #114版获取历史业绩中的月收入详情
    @staticmethod
    def financeMonthearn114(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/monthearn114'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #bapp 检查是否已经月结
    @staticmethod
    def buserCheckmonthclear(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/buser/checkmonthclear'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #bapp 查询我的收入
    @staticmethod
    def financeMyearnings(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/myearnings'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #114版获取历史业绩中的客户交易额
    @staticmethod
    def financeGethiscustamt(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/gethiscustamt'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #114版获取历史业绩中的客户交易详情
    @staticmethod
    def financeGetcusttradedetail(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,date,page,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['date']=date
        params['page']=page
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/getcusttradedetail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #2.8版获取历史业绩中的客户交易额
    @staticmethod
    def financeGetcustamount(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/getcustamount'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)

    #经纪人本月业绩的客户交易额V2.8
    @staticmethod
    def financeGetmonthcusttradedetail(iteration,mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,date,page,returnvalue=None,inputp=None,outputp=None):
        params={}
        params['mobilephone']=mobilephone
        params['appVer']=appVer
        params['envType']=envType
        params['token']=token
        params['deviceType']=deviceType
        params['userId']=userId
        params['deviceCode']=deviceCode
        params['appType']=appType
        params['date']=date
        params['page']=page
        params['returnvalue']=returnvalue
        path=bappurl + '/finance/getmonthcusttradedetail'
        test=InterfaceTests()
        if iteration=="Nomal":
            test.interfaceTest(path,params)
        elif iteration=="Fault":
            test.iterationTest(path, params)
        else:
            test1=MainLogic()
            test1.scenelogicTest(path,params,inputp,outputp)