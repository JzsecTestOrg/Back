#!/usr/bin/python
# coding:utf8

import re
import os
import sys
import time
import json
import redis
import socket
import pickle
import MySQLdb
import getpass
import requests
from pprint import pprint
from optparse import OptionParser

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class wechat():

    def __init__(self):

        self.dbhost         =   "10.10.186.133"
        self.redishost      =   "10.10.149.147"
        self.dbname         =   "wechat"
        self.tbuser         =   "users"
        self.tbgroup        =   "groups"
        self.tbrelations    =   "relations"
        self.tbtmpl         =   "template_message"
        self.tbhist         =   "notifications_history"
        self.dbuser         =   "wechatuser"
        self.dbpass         =   "We1xlnP@sS"
        self.template_id    =   "tA3e9KBMe5t6OutFxslbADt8tPohpwMdqBi94YVU3cY"

        self.params_list    =   {
            'OpenIDs'       :   [],
            'GroupIDs'      :   [],
            'UserNames'     :   [],
            'GroupNames'    :   [],
            'DeletedNames'  :   [],
            'first'         :   [],
            'remark'        :   [],
        }
        self.params_string  =   {
            'URL'           :   '',
            'keyword1'      :   '',
            'keyword2'      :   '',
            'ColorType'     :   '',
            'NotifyType'    :   '业务通知',
        }
        self.params_bool    =   {
            'UseProxy'      :   False,
            'RecordOnly'    :   False,
            'NotifyOnly'    :   False,
        }
        self.params_list    =   self.param_key_to_lower(self.params_list)
        self.params_string  =   self.param_key_to_lower(self.params_string)
        self.params_bool    =   self.param_key_to_lower(self.params_bool)

        self.default_params =   {}

        self.default_params.update(self.params_list)
        self.default_params.update(self.params_string)
        self.default_params.update(self.params_bool)

        self.ipaddress      =   self._get_local_ipaddress()

    def _get_local_ipaddress(self):
        try:
            ipaddress = socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
            ipaddress = socket.gethostname()
        finally:
            if ipaddress == "127.0.0.1":
                ipaddress = socket.gethostname()
            return ipaddress

    def __get_token(self):
        try:
            access_token = self.redis_client.get('wxed34696e59985ecf_access_token')
        except:
            access_token = "无法获取API Token，请检查数据设置"
            print access_token
        finally:
            return access_token

    def get_post_datas(self):

        color_dict    = { "OK" : "#00DD00", "WARNING" : "#FFCC00", "CRITICAL" : "#FF0000", "UNKNOWN" : "#FF0050", "PENDING" : "#A9A9A9", }

        color = color_dict[self.ColorType] if self.ColorType in color_dict else '#000000'

        data    =   {
            'template_id'   :   self.template_id,
            'data'          :   {
                    'first'     :   { 'value' : "\n".join(self.first),  'color' : color },
                    'keyword1'  :   { 'value' : self.keyword1,          'color' : color },
                    'keyword2'  :   { 'value' : self.keyword2,          'color' : color },
                    'remark'    :   { 'value' : "\n".join(self.remark), 'color' : color },
            },
        }

        if self.URL is not None and re.search("https?://", self.URL) != None:
            data['url'] = self.URL
        
        return data

    def send_msg_to_openid(self,openid):
        data = self.PostDatas
        data['touser'] = openid
        try:
            requests.post(self.PostURL,data=json.dumps(data),verify=False)
        except:
            return False
        else:
            return True

    def get_openid_list(self,mysql_command):
        retlist = []
        try:
            self.wechat_cursor.execute(mysql_command)
            for k in self.wechat_cursor.fetchall():
                retlist.extend(list(k))
        except:
            retlist = []
        finally:
            return retlist
    
    def get_openids_by_usernames(self,usernames):
        return self.get_openid_list("select openid from %s where realname in ('%s')" % (self.tbuser,"','".join(usernames))) if usernames != [] else []

    def get_openids_by_groupnames(self,groupnames):
        command = "select openid from %s where groupid in (select groupid from %s where groupname in ('%s'))" % (self.tbrelations,self.tbgroup,"','".join(groupnames))
        return self.get_openid_list(command) if groupnames != [] else []

    def get_openids_by_groupids(self,groupids):
        return self.get_openid_list("select openid from %s where groupid in ('%s')" % (self.tbrelations,"','".join(groupids))) if groupids != [] else []
        
    def get_post_url(self):
        return "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % self.__get_token()

    def get_final_openids(self):
        UserNames     =  set(self.get_openids_by_usernames( self.UserNames   ))
        GroupNames    =  set(self.get_openids_by_groupnames(self.GroupNames  ))
        GroupIDs      =  set(self.get_openids_by_groupids(  self.GroupIDs    ))
        DeletedNames  =  set(self.get_openids_by_usernames( self.DeletedNames))
        SumSet        =  UserNames.union(GroupNames).union(GroupIDs)
        if self.OpenIDs != []: SumSet = SumSet.union(set(self.OpenIDs))
        return list(SumSet-DeletedNames)

    def make_sure_list_type_is_a_list(self,key,value):
        if key not in self.params_list:
            return value
        else:
            if type(value) != type([]) and value is not None:
                return [value]
            else:
                return value

    def param_key_to_lower(self,params):
        for key in params:
            value = params[key]
            lowerkey = key.lower()
            del(params[key])
            params[lowerkey] = self.make_sure_list_type_is_a_list(lowerkey,value)
        return params

    def get_param(self,param):
        param = param.lower()
        if param in self.params:
            return self.params[param]
        else:
            return self.default_params[param]

    def save_notification_logs(self,final_openids):
        first     = self.PostDatas['data']['first']['value'];
        keyword1  = self.PostDatas['data']['keyword1']['value'];
        keyword2  = self.PostDatas['data']['keyword2']['value'];
        remark    = self.PostDatas['data']['remark']['value'];
        datetime  = time.strftime('%F %T')
        mysql_command  = "insert into %s (ipaddress,logname,openids,first,keyword1,keyword2,remark,datetime,type) values " % self.tbhist
        mysql_command += "('%s','%s'" % (self.ipaddress,getpass.getuser())
        mysql_command += ",'%s'" % ','.join(map(lambda x:x.encode('utf8'),final_openids))
        mysql_command += ",'%s','%s','%s','%s','%s','%s'" % (first,keyword1,keyword2,remark,datetime,self.NotifyType)
        mysql_command += ");";
        try:
            self.wechat_cursor.execute(mysql_command)
        except:
            pass

    def send(self, params):
        self.wechat_conn    =   MySQLdb.connect(host=self.dbhost,user=self.dbuser,passwd=self.dbpass,db=self.dbname,use_unicode=True,charset="utf8")
        self.wechat_cursor  =   self.wechat_conn.cursor()
        self.redis_client   =   redis.Redis(self.redishost)

        self.params         =   self.param_key_to_lower(params)
        if self.params == None: return False
        self.URL            =   self.get_param('URL')
        self.OpenIDs        =   self.get_param('OpenIDs')
        self.GroupIDs       =   self.get_param('GroupIDs')
        self.UserNames      =   self.get_param('UserNames')
        self.GroupNames     =   self.get_param('GroupNames')
        self.DeletedNames   =   self.get_param('DeletedNames')
        self.first          =   self.get_param('first')
        self.keyword1       =   self.get_param('keyword1')
        self.keyword2       =   self.get_param('keyword2')
        self.remark         =   self.get_param('remark')
        self.ColorType      =   self.get_param('ColorType')
        self.RecordOnly     =   self.get_param('RecordOnly')
        self.UseProxy       =   self.get_param('UseProxy')
        self.NotifyOnly     =   self.get_param('NotifyOnly')
        self.NotifyType     =   self.get_param('NotifyType')

        if self.keyword2 == '': self.keyword2 = time.strftime("%F %T")
        self.PostDatas      =   self.get_post_datas()
        self.PostURL        =   self.get_post_url()
        final_openids       =   self.get_final_openids()

        if final_openids == []:
            self.GroupNames =   ["运维"]
            final_openids   =   self.get_final_openids()
            self.PostDatas['data']['first']['value'] = "无法获取收件人列表，已发给运维组(默认)" + self.PostDatas['data']['first']['value']

        if not self.NotifyOnly:
            self.save_notification_logs(final_openids)

        success = True
        if not self.RecordOnly:
            if self.UseProxy:
                try:
                    rc = redis.Redis(self.redishost)
                    rc.rpush("wechat_message_queue_python",pickle.dumps(self.params))
                except:
                    success = False
            else:
                for openid in final_openids:
                    success = self.send_msg_to_openid(openid)

        self.wechat_conn.close()
        self.redis_client.connection.disconnect()
        return success

    


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print "Usage: %s --help" % sys.argv[0]
        sys.exit(1)

    current_time = time.strftime("%F %T")
    parser = OptionParser()
    parser.add_option("-l", "--link",          dest="url",          default=None,         metavar="http://address/path/to/file.extention", help=u"在通知中显示的链接地址。")
    parser.add_option("-o", "--openid",        dest="openids",      default=[],           metavar="OpenID1,OpenId2,OpenIDN",               help=u"用户的微信OpenID，仅供代码使用，不建议人员主动使用。")
    parser.add_option("-u", "--username",      dest="usernames",    default=[],           metavar="Name1,Name2,NameN",                     help=u"管理界面中填写的真实姓名，不支持微信昵称，逗号分隔。")
    parser.add_option("-g", "--groupname",     dest="groupnames",   default=[],           metavar="Name1,Name2,NameN",                     help=u"管理界面中设定的组名，逗号分隔。")
    parser.add_option("-G", "--groupid",       dest="groupids",     default=[],           metavar="GroupID1,GroupID2,GroupIDN",            help=u"唯一组ID，逗号分隔。")
    parser.add_option("-x", "--delete-user",   dest="deletednames", default=[],           metavar="Name1,Name2,NameN",                     help=u"要排除的用户名(管理界面中的真实姓名)列表，逗号分隔。")
    parser.add_option("-c",  "--color-type",   dest="colortype",    default=None,         metavar="OK/WARNING/CRITICAL/UNKNOWN/PENDING",   help=u"根据报警状态显示不同的颜色")
    parser.add_option("-1", "--error-level",   dest="keyword1",     default=None,         metavar="STRINGS",                               help=u"错误级别")
    parser.add_option("-2", "--error-message", dest="keyword2",     default=current_time, metavar="STRINGS",                               help=u"错误信息")
    parser.add_option("-f", "--first",         dest="first",        default=[],           metavar="FIRST",                                 help=u"自定义标题")
    parser.add_option("-r", "--remark",        dest="remark",       default=[],           metavar="REMARK",                                help=u"底部附加消息")
    parser.add_option("-T", "--notify-type",   dest="notifytype",   default="业务通知",   metavar="Notification Type",                     help=u"报警类型")
    parser.add_option("-p", "--use-proxy",     dest="useproxy",     default=False,        metavar="Use Proxy",       action="store_true",  help=u"使用代理发消息，不从本机发")
    parser.add_option("-R", "--record-only",   dest="recordonly",   default=False,        metavar="Record Only",     action="store_true",  help=u"只记录日志不发送通知")
    parser.add_option("-N", "--notify-only",   dest="notifyonly",   default=False,        metavar="Notify Only",     action="store_true",  help=u"只发送通知不记录日志")

    (options, args) = parser.parse_args()

    params = {
       'OpenIDs'       :   options.openids.split(',')      if options.openids      != [] else [],
       'GroupIDs'      :   options.groupids.split(',')     if options.groupids     != [] else [],
       'UserNames'     :   options.usernames.split(',')    if options.usernames    != [] else [],
       'GroupNames'    :   options.groupnames.split(',')   if options.groupnames   != [] else [],
       'DeletedNames'  :   options.deletednames.split(',') if options.deletednames != [] else [],
       'first'         :   options.first.split("\\n")      if options.first        != [] else [],
       'remark'        :   options.remark.split("\\n")     if options.remark       != [] else [],
       'URL'           :   options.url,
       'keyword1'      :   options.keyword1,
       'keyword2'      :   options.keyword2,
       'ColorType'     :   options.colortype,
       'NotifyType'    :   options.notifytype,
       'UseProxy'      :   options.useproxy,
       'RecordOnly'    :   options.recordonly,
       'NotifyOnly'    :   options.notifyonly,
    }

    wechat = wechat()

    wechat.send(params)