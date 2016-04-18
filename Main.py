__author__ = 'jinghua'
#!/usr/bin/python
# -*- coding: utf-8 -*-
from InterfaceTests import InterfaceTests
from BappBase import Bapp,Capp
#必填参数
iteration=False
#mobilephone = '15501253701'
#mobilephone = '18753610132'
mobilephone = '13200000000'
cappmobilephone='13300000009'
local_count='0'
userId='29ba9bcbb56494ec9d960b7590a17578'
product_id='2'
appVer='45'
cappver='32'
envType='0'
cenvType='0'
deviceType='Android'
deviceCode='python'
appType='1'
cappType='11'
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
customers='123'
client_id='123'
myClientId='kingbroker_74ce9daab55bfcd09392980e4ea89c4c'
fClientId='kingbroker_dafd0d230799780a8a6258948537238c'
fromtype='1'
targettype='1'
phone_book=[{"mobilephone":"15801205327"}]
date='201601'
kind='1000'
page='1'
pagesize='5'
verifyPassword='qaz123'
filePath="\/storage\/emulated\/0\/Broker\/icon_2c0931b782a3950c8b5c2bb8375aff30.jpg"
bucket="jingjibao"
authorization="UCloud ucloudchenbc@jzsec.com1442451271000655808565:nea2rKVorspqH5y3qulJ04GsmZI="
sysattachment_ucloudbapptoken='1'
title='上传'
cust_client_id='imaster_9'


#组合
symbols=["ABC888","YCF886"]
symbol='TQE888'
client_id='bgggggggggggggggggggggggggggggggg'
cash='100000'
rbs='jinghua'
stock_market='SH'
stock_symbol='600000'
stock_name='浦发'
prev_weight='0'
target_weight='0'
client_ids='[{"tuser_name":"张","tclient_id":"imaster_111","inv_reason":"加一下我的小号","t_user_type" :"1"}]'
tclient_ids='[{"tuser_name":"张","tclient_id":"imaster_111","inv_reason":"加一下我的小号","t_user_type" :"1"}]'
tclient_id='kingbroker_dafd0d230799780a8a6258948537238c'
bid="b241a8d3de4a8647bb258804c5305ef1"
fromid='kingbroker_dafd0d230799780a8a6258948537238c'
targetid='kingbroker_74ce9daab55bfcd09392980e4ea89c4c'
deletetype='1'
gid='123456'
user_name='zhangshan'
agree='1'
username='jinghua'
room_id='1'
content='欢迎您成为经纪宝最珍视的伙'
pid='123456'


#可选参数
returnvalue="SUCCESS"
chkmsg_message_messagelist="欢迎您成为经纪宝最珍视的伙伴"
chkmsg_follow_followlist="您的证件附件未上传或未提交"
chkmsg_buser_commissionhistory="成功"
chkmsg_buser_uploadconfirm="您上传的证件不全"
chkmsg_sysattachment_ucloudtoken="jingjibao"
chkmsg_followdone_followdones="无需更新"
chkmsg_syslink_getrecommend="我发现个好东西，股票经纪人专用神器"
#password='Jzzq87654321'
password='qaz123'


flag='1'
link_type='2'#1为分享到朋友圈 2为分享给微信好友

test=InterfaceTests()
#userId=test.get_login_userId()
returnparams=test.get_login_token('bapp')
print(returnparams)
bapptoken=returnparams['bapptoken']
client_id=test.returnparams['client_id']
userId=test.returnparams['userId']
returnparams=test.get_login_token('capp')
print(returnparams)
capptoken=returnparams['capptoken']
cappclient_id=returnparams['cappclient_id']
cappuserId=returnparams['cappuserId']

Capp.cuserSearchbroker(iteration,cappmobilephone,cappver,envType,capptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Capp.sysstaticGetonepage(iteration,cappmobilephone,cappver,envType,capptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Capp.cuserGetcustid(iteration,cappmobilephone,cappver,envType,capptoken,deviceType,userId,deviceCode,appType,returnvalue=None)


"""BAPP"""
"""
#Bapp.syssharelinkShowstatistics(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
#Bapp.bcustomer_getcuserbymobilephones(mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,customerMobilephones,returnvalue=None)
#Bapp.bcustomer_modifycustomers(mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,customers,returnvalue=None)
#Bapp.finance_thismonthperf(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,date=1,kind=1,page=1,pagesize=1,returnvalue=None)
Bapp.syssharelinkShowstatistics(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.bcustomer_getcuserbymobilephones(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,customerMobilephones,returnvalue=None)
Bapp.bcustomer_modifycustomers(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,customers,returnvalue=None)
Bapp.bcustomer_syncnew (iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.bcustomer_syncnewnotice (iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,cid,returnvalue=None)
Bapp.follow_followlist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None,flag=None)
Bapp.message_messagelist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,flag,returnvalue=None)
Bapp.followdone_followdones(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,flag,returnvalue=None)
Bapp.buser_changeinfo(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,value,appType,key,returnvalue=None)
Bapp.buser_getuserstatus(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.sysattachment_ucloudtoken(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.buser_uploadconfirm(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.system_editinfo(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,sex,issue_authority,identityNum,validity,name,returnvalue=None)
Bapp.buser_uploadconfirm(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,mail,address,contractLimit,roleId,returnvalue=None)
#Bapp.buser_uploadconfirm(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.train_train(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.bcustomer_getbrokerageresults(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.sysstatic_getonepage(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,title,returnvalue=None)
Bapp.finance_monthearn(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,date,returnvalue=None)
Bapp.finance_mywithdraw(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,date,returnvalue=None)
Bapp.finance_withdraw(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.system_resetpass(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,password,verifyPassword,returnvalue=None)
Bapp.system_resetpass(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,password,verifyPassword,returnvalue=None)
Bapp.bcustomer_getmycusers115(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,customerMobilephones,returnvalue=None)
Bapp.syssharelink_getproduct(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.syssharelink_showstatistics(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.syssharelink_showsrecomdetails(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,kind,returnvalue=None)
Bapp.bkpi_gethistorykpi(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.bkpi_getkpibymonth(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.buser_getbuserinfo(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.buser_getuserstatus(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.bcustomer_getbrokerageresults(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.system_getinvitecode(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.buser_saveavater(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,filePath,bucket,authorization,key,url,returnvalue=None)
Bapp.buser_changeinfo(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,key,value,returnvalue=None)
Bapp.buser_getlastexpress(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,returnvalue=None)
Bapp.buser_contractmail(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,mail,returnvalue=None)
"""
Bapp.financeThismonthperf201(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,date,kind,page,returnvalue=None)
Bapp.financeGetcustmonthtradedetailhperf201(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,date,cust_client_id,returnvalue=None)
Bapp.financeGetcustmonthtradeamount(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,cust_client_id,returnvalue=None)


"""IM"""
"""
Bapp.friendConfirmfriend(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,myClientId,fClientId,returnvalue=None)
Bapp.friendFriendapply(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,myClientId,fClientId,fromtype,targettype,returnvalue=None)
Bapp.namelistGetfriendlist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,myClientId,returnvalue=None)
Bapp.namelistGetfriendlist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,'imaster_1',returnvalue=None)
Bapp.namelistGetimuserdetail(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,fClientId,returnvalue=None)
Bapp.namelistGetimphonebook(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,phone_book,returnvalue=None)
Bapp.namelistInvmelist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,returnvalue=None)
Bapp.namelistGetconvlist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,returnvalue=None)
Bapp.friendFrienddelete(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,fromid,targetid,deletetype,returnvalue=None)
Bapp.groupAddmember(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,tclient_ids,gid,user_name,returnvalue=None)
Bapp.groupUserconfirm(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,gid,agree,returnvalue=None)
Bapp.groupManagerconfirm(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,gid,agree,tclient_id,returnvalue=None)
Bapp.groupCreategroup(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,client_ids,returnvalue=None)
Bapp.namelistGroupfriendlist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,client_ids,returnvalue=None)
Bapp.namelistPersondetail(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,room_id,returnvalue=None)
Bapp.groupCreatedefaultgroup(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,bid,returnvalue=None)
Bapp.groupJoindefaultgroup(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,bid,returnvalue=None)
Bapp.groupMemberportfolios(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,gid,returnvalue=None)
Bapp.groupGroupinvlist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,username,returnvalue=None)
Bapp.groupGrouplist(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,returnvalue=None)
Bapp.groupGetfolio(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,gid,returnvalue=None)
Bapp.groupUpdategroup(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,gid,content,type,returnvalue=None)
Bapp.androidGetnodisturblistmember(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,returnvalue=None)
Bapp.groupBuseron(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,bid,returnvalue=None)
"""
Bapp.groupGuerystatus(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,returnvalue=None)
Bapp.groupSetmuteall(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,"0",returnvalue=None)
Bapp.friendSfbyphone(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,"18010161483",returnvalue=None)
Bapp.groupSetmuteone(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,"0",gid,returnvalue=None)
Bapp.groupQuerystatusone(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,gid,returnvalue=None)
Bapp.systemChecktoken(iteration,mobilephone,appVer,envType,bapptoken,deviceType,userId,deviceCode,appType,client_id,returnvalue=None)





"""CAPP组合"""
"""
print(mobilephone)
Capp.portfolioListholdings(iteration,mobilephone,appVer,envType,capptoken,cappclient_id,deviceType,userId,deviceCode,appType,symbols,returnvalue=None)
Capp.portfolioListmine(iteration,mobilephone,appVer,envType,capptoken,deviceType,userId,deviceCode,appType,cappclient_id,returnvalue=None)
Capp.portfolioAddcomment(iteration,mobilephone,appVer,envType,capptoken,cappclient_id,deviceType,userId,deviceCode,appType,symbol,content,returnvalue=None)
Capp.portfolioListfavourites(iteration,mobilephone,appVer,envType,capptoken,deviceType,userId,deviceCode,appType,symbol,client_id,"bgggggggggggggggggggggggggggggggg",returnvalue=None)
Capp.portfolioCreate(iteration,mobilephone,appVer,envType,capptoken,cappclient_id,deviceType,userId,deviceCode,appType,name,cash,rbs,stock_market,stock_symbol,stock_name,prev_weight,target_weight,returnvalue=None)
Capp.portfolioListcomments(iteration,mobilephone,appVer,envType,capptoken,cappclient_id,deviceType,userId,deviceCode,appType,symbol,returnvalue=None)
Capp.portfolioAddfavourite(iteration,mobilephone,appVer,envType,capptoken,deviceType,userId,deviceCode,appType,symbol,client_id,returnvalue=None)
Capp.portfolioDeletefavourite(iteration,mobilephone,appVer,envType,capptoken,deviceType,userId,deviceCode,appType,symbol,client_id,returnvalue=None)
Capp.portfolioDetails(iteration,mobilephone,appVer,envType,capptoken,deviceType,userId,deviceCode,appType,symbol,client_id,returnvalue=None)
Capp.portfolioRebalance(iteration,mobilephone,appVer,envType,capptoken,cappclient_id,deviceType,userId,deviceCode,appType,name,cash,rbs,stock_market,stock_symbol,stock_name,prev_weight,target_weight,returnvalue=None)
Capp.portfolioListall(iteration,cappmobilephone,appVer,cenvType,capptoken,deviceType,cappuserId,deviceCode,cappType,cappclient_id,returnvalue=None)
Capp.portfolioRebalancinghistories(iteration,cappmobilephone,appVer,cenvType,capptoken,cappclient_id,deviceType,cappuserId,deviceCode,cappType,symbol,returnvalue=None)
"""

