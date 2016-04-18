"""
Created on Fri Jul 17 11:38:25 2015

@author: jinghua
"""
from interfaceTests import InterfaceTests
from BappBase import *
#必填参数
mobilephone = '13200000001'
local_count='0'
product_id='2'
appVer='22'
envType='1'
deviceType='Android'
deviceCode='python'
appType='1'
customerMobilephones=["13693041119","18611709562","13716589866","18910872989","13253187816","13521971576","13811137798","13081891258","15811208179","13120216066","18910872978","13810676772","18810366398","13426292084","15101539472","13366037316","18764180529","18801107659","15531466865","18910872583","18510310571","15011355230","18233899755","18903241008","15910678078","13311517930","13333148543","15801035693","13911627636","18730476499","13811943930","15010515796","13439219793","18610497399","18601229750","13910528861","18910873995","18611816512","13021278014","13693177397","13261389682","18911702978","13581615823","18810762976","18001353625","18500193163","15233438356","18611239320","13718313959","15652122753","13311277736","18001155319","18515588903","18612006722","13261389682","13333148543","13366037316","13426292084","13439219793","13581615823","13716589866","13718313959","13910528861","15011355230","15233438356","15811208179","18611816512","18801107659","18910872583","18910872978","13811977448"]
cid=[]
url='http:\/\/w.url.cn\/s\/ALpa9Bo'
value='风风光光呵呵'
key="address"
mail="jinghuaj@126.com"
address="ggcvgg刚刚古古怪怪哈哈还差长发好年纪"
contractLimit="0"
roleId='5'
title="sign_contract"
sex="1"
issue_authority="湘潭市公安局雨湖分局"
identityNum="362103198308130210"
id_address="湖南嶺湘渾框雨攤区石多头2号附1号"
validity="2006.10.01-2016.10.01"
name="赖玉旺"
invite_code='h9e5xn'
select_recommend="投资大师，开户交易一体化，给您一站式流畅体验，告别两个app的繁琐时代！"
getmycusers_customerMobilephones=["13210872456"]


#可选参数
returnvalue="SUCCESS"
chkmsg_message_messagelist="欢迎您成为经纪宝最珍视的伙伴"
chkmsg_follow_followlist="您的证件附件未上传或未提交"
chkmsg_buser_commissionhistory="成功"
chkmsg_buser_uploadconfirm="您上传的证件不全"
chkmsg_sysattachment_ucloudtoken="jingjibao"
chkmsg_followdone_followdones="无需更新"
chkmsg_syslink_getrecommend="我发现个好东西，股票经纪人专用神器"
password='123456'
flag='1'
link_type='2'#1为分享到朋友圈 2为分享给微信好友

test=InterfaceTests()
userId=test.get_login_userId(mobilephone,password)
token=test.get_login_token(mobilephone,password)
print(token)
print(userId)


def bcustomerGetallcustomerbybuser():
		"""获取最新的推荐结果"""
		params = {}
		params['mobilephone']=mobilephone
		params['appVer']=appVer
		params['envType']=envType
		params['token']=token
		params['deviceType']=deviceType
		params['userId']=userId
		params['deviceCode']=deviceCode
		params['appType']=appType
		#params['id']="123456"
		#params['date']="2015-08-24 16:54:08"

		params['returnvalue']=returnvalue
		path='bcustomer/getallcustomerbybuser'
		test=InterfaceTests()
		test.batch_interface_test(path, params)

def financemywithdraw():
		"""获取最新的推荐结果"""
		params={}
		params['mobilephone']=mobilephone
		params['appVer']=appVer
		params['envType']=envType
		params['token']=token
		params['deviceType']=deviceType
		params['userId']=userId
		params['deviceCode']=deviceCode
		params['appType']=appType
		params['id']="123456"
		params['date']="2015-08-24 16:54:08"

		params['returnvalue']=returnvalue
		path='finance/mywithdraw'
		test=InterfaceTests()
		test.batch_interface_test(path, params)

def bcustomergetmycusers():
		"""获取最新的推荐结果"""
		params={}
		params['mobilephone']="13200000001"
		params['appVer']=appVer
		params['envType']=envType
		params['token']=token
		params['deviceType']=deviceType
		params['userId']=userId
		params['deviceCode']=deviceCode
		params['appType']=appType
		params['bucket']="jpg"
		params['mail']="jinghua@126.com"
		params['key']="jinghua"
		params['inviteCode']="123456"

		params['returnvalue']=returnvalue
		#path='syslink/showstatistics'
		path='buser/saveinvitecode'
		test=InterfaceTests()
		test.batch_interface_test(path, params)

#bcustomerGetallcustomerbybuser()

#bcustomergetmycusers()

def capp():
		"capp interfaceTests"
		params={}
		params['mobilephone']="11000000008"
		params['appVer']="14"
		params['envType']="1"
		params['token']=token
		params['deviceType']=deviceType
		params['userId']=userId
		params['deviceCode']=deviceCode
		params['appType']="1"
		params['password']="123456"

		params['returnvalue']=returnvalue
		#path='syslink/showstatistics'
		path='cuser/login'
		test=InterfaceTests()
		test.batch_interface_test(path, params)
#capp()
bcustomergetmycusers()
#客户
#BappBase.bcustomer_getcuserbymobilephones(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,customerMobilephones,chkmsg_buser_commissionhistory)
"""
BappBase.bcustomer_syncnew (mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,returnvalue)
BappBase.bcustomer_syncnewnotice (mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,cid,returnvalue)
####BappBase.bcustomer_getmycusers(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,getmycusers_customerMobilephones,returnvalue)
#代办
BappBase.follow_followlist(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,chkmsg_follow_followlist,flag)
BappBase.message_messagelist(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,flag,chkmsg_message_messagelist)
BappBase.followdone_followdones(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,flag,chkmsg_followdone_followdones)
#推荐
####BappBase.syslink_showstatistics(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType)

BappBase.syslink_getrecommend(mobilephone,local_count,invite_code,product_id,appVer,envType,token,deviceType,userId,deviceCode,appType,select_recommend,chkmsg_syslink_getrecommend)
#个人中心
BappBase.buser_getfundinfo(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType)
BappBase.buser_commissionhistory(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,chkmsg_buser_commissionhistory)
BappBase.buser_changeinfo(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,value,appType,key)
BappBase.buser_getuserstatus(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,chkmsg_buser_commissionhistory)
BappBase.sysattachment_ucloudtoken(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,chkmsg_sysattachment_ucloudtoken)
BappBase.buser_uploadconfirm(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,title,chkmsg_buser_uploadconfirm)
####BappBase.train_train(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType)
BappBase.bcustomer_getbrokerageresults(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType)
####BappBase.sysstatic_getonepage(mobilephone,appVer,envType,token,deviceType,userId,deviceCode,appType,title)
"""


