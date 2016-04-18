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