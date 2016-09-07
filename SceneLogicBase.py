"""CAPP"""
#注册
sendauthcodeinput={
    "mobilephone1":"15801205322",
    "mobilephone2":"",
    #"mobilephone3":"18788776756",
    "mobilephone4":"18010161483",
    #"verifyparam":"mobilephone"
    }
sendauthcodeoutput={
    "mobilephone1":"msg\": \"该手机号已被注册，请使用其它手机号",
    "mobilephone2":"手机号已被注册",
    "mobilephone3":"msg\": \"发送成功",
    "mobilephone4":"msg\": \"该手机号已被注册，请使用其它手机号"
    }
cuserregisterinput={
    "verifycode1":"$%^&*(&^%$%",
    "verifycode2":"1234567",
    "verifycode3":"123456",
    "nickName1":"*&……%&**…………&",
    #"verifyparam":"mobilephone"
    }
cuserregisteroutput={
    "verifycode1":"msg\": \"验证码不正确",
    "verifycode2":"msg\": \"验证码不正确",
    "verifycode3":"msg\": \"验证码不正确",
    "nickName1":"msg\": \"验证码不正确"
    }
#登录
cuserlogininput={
    "mobilephone1":"15801205322",
    "mobilephone2":"^&**^&*^12321",
    "mobilephone3":"18788776756",
    "mobilephone4":"18010161483",
    "password1":"",
    "password2":"qaz 123"
    }
cuserloginoutput={
    "mobilephone1":"msg\": \"登录成功",
    "mobilephone2":"msg\": \"您的帐号已被锁定",
    "mobilephone3":"msg\": \"用户未注册或已失效",
    "mobilephone4":"msg\": \"验证码不正确",
    "password1":"msg\":\"手机号或密码错误，您还有4次重试机会",
    "password2":"密码错误"
    }






"""BAPP"""
customers1=[{"customerExtend":{"add":[{"value":"15801208889","_id":44,"type":10,"bappceid":"b4691009650240e8beb66ae16de47dfb","status":2,"cid":"2c0931b782a3950c8b5c2bb8375aff307030307b0123423e9cadae9581c65a3b"}]}}]
customers2=[{"customerExtend":{"add":[{"value":"13300000002","_id":18,"type":10,"bappceid":"baab5c40f11244e6b4ec3b8fc50e05fc","status":2,"cid":"b290d1046e194a8b52dfbbd525edb47e3bc5ae33b51b48a0b0315612a77a7b28"},{"value":"发发他人","_id":19,"type":20,"bappceid":"ef49c746142545b485ef78356722d479","status":2,"cid":"b290d1046e194a8b52dfbbd525edb47e3bc5ae33b51b48a0b0315612a77a7b28"},{"value":"jinghuaj@126.com","_id":20,"type":40,"bappceid":"36bec6a891ea4d8c85afeae097173667","status":2,"cid":"b290d1046e194a8b52dfbbd525edb47e3bc5ae33b51b48a0b0315612a77a7b28"}],"deleted":""},"is_web_sync":0,"fromwhichsys":1020,"_id":18,"truename":"002","cid":"b290d1046e194a8b52dfbbd525edb47e3bc5ae33b51b48a0b0315612a77a7b28"}]
#注册
syssendauthcodeinput={
    "mobilephone1":"15801205322",
    "mobilephone2":"",
    #"mobilephone3":"18788776756",
    "mobilephone4":"18010161483",
    #"verifyparam":"mobilephone"
    }
syssendauthcodeoutput={
    "mobilephone1":"code\": -21",
    "mobilephone2":"手机号错误",
    "mobilephone3":"msg\": \"发送成功",
    "mobilephone4":"msg\": \"该手机号已经注册，请使用其它手机号"
    }
sysregisterinput={
    "verifycode1":"$%^&*(&^%$%",
    "verifycode2":"1234567",
    "verifycode3":"123456",
    "nickName1":"*&……%&**…………&",
    #"verifyparam":"mobilephone"
    }
sysregisteroutput={
    "verifycode1":"msg\": \"验证码不正确",
    "verifycode2":"msg\": \"验证码不正确",
    "verifycode3":"msg\": \"验证码不正确",
    "nickName1":"msg\": \"验证码不正确"
    }
#登录
systemlogininput={
    "mobilephone1":"15801205322",
    "mobilephone2":"^&**^&*^12321",
    "mobilephone3":"18788776756",
    "mobilephone4":"18010161483",
    "password1":"",
    "password2":"qaz 123"
    }
systemloginoutput={
    "mobilephone1":"msg\": \"登录成功",
    "mobilephone2":"msg\": \"您的帐号已被锁定",
    "mobilephone3":"msg\": \"用户未注册或已失效",
    "mobilephone4":"msg\": \"验证码不正确",
    "password1":"msg\":\"手机号或密码错误，您还有4次重试机会",
    "password2":"密码错误"
    }

#忘记密码
systemresetpassinput={
    "verifycode1":"$%^&*(&^%$%",
    "verifycode2":"1234567",
    "verifycode3":"123456",
    #"password1":"1234",
    #"verifyparam":"mobilephone"
    }
systemresetpassoutput={
    "verifycode1":"msg\": \"验证码不正确",
    "verifycode2":"msg\": \"验证码不正确",
    "verifycode3":"msg\": \"验证码不正确",
    #"password1":"1234",
    }


#意见反馈
busersendadviceinput={
    "content1":"$%^&12345a",
    "content2":"",
    "content3":"123456asdfghjkl",
    "content4":"36ae65b7e34cee90f910b110f242bed9c7bf04bdc060ff72a2c7a603d0b278f6b57434c414c253bfac6ced50ede1a14e76c86506e0f7e836881e409d454d98a1517928c3f802899f1b70e7d7ae3c69ca87f973c0a2723d75d6a06370ed1682b6555901307b2d2baf3c52693f0e8b2c922e3668bc79ebfe4a29a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c",
    "content5":"%……&**（*（（%……&**（*（（%……&**（*（（",
    "content6":"112332136ae65b7e34cee90f910b110f242bed9c7bf04bdc060ff72a2c7a603d0b278f6b57434c414c253bfac6ced50ede1a14e76c86506e0f7e836881e409d454d98a1517928c3f802899f1b70e7d7ae3c69ca87f973c0a2723d75d6a06370ed1682b6555901307b2d2baf3c52693f0e8b2c922e3668bc79ebfe4a29a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2c61929a7bf3f2csdfdsfdsdsdsafdsafdsafdsafdsafdsafdsfddsfds",
    }
busersendadviceoutput={
    "content1":"msg\": \"反馈内容字数限制为15-500字",
    "content2":"msg\": \"请输入反馈内容",
    "content3":"msg\": \"意见反馈成功",
    "content4":"msg\": \"意见反馈成功",
    "content5":"msg\": \"意见反馈成功",
    "content6":"msg\": \"反馈内容字数限制为15-500字",
    }

#手动添加联系人
modifycustomersinput={
    "customers1":customers1,
    "customers2":customers2,
    "customers3":customers2,
    }
modifycustomersoutput={
    "customers1":"value\": \"15801208889",
    "customers2":"_id\": 19",
    "customers3":"value\": \"jinghuaj@126.com",

    }