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