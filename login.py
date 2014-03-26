#!/usr/bin/python
#-*-coding:utf-8-*-

import httplib,urllib,json,os;  #加载模块

sessionFile = 'session'

from pub import *

class login:
    __user_id = ''
    __token = ''
    __expire = ''
    def __init__(self):
        if not isFileExist(sessionFile) or isFileEmpyty(sessionFile):
            email = raw_input('Enter email: ')
            password = raw_input('Enter password:')
            params = urllib.urlencode({'email':email,
                        			   'password':password,
                           			   'app_name':'radio_desktop_win',
                        			   'version':100})
            conn = httplib.HTTPConnection("www.douban.com")
            conn.request("POST","/j/app/login",params,header)
            response = json.load(conn.getresponse())
            conn.close()
            if response['r']!=0:
                print "error ",response["err"]
                quit()
            wFileHandle = open(sessionFile,'w')
            wFileHandle.write(response['user_id']+'\r\n')
            wFileHandle.write(response['token']+'\r\n')
            wFileHandle.write(response['expire'])
            wFileHandle.close()
        rFileHandle = open(sessionFile,'r')
        self.user_id = rFileHandle.readline().strip('\r\n')
        self.token = rFileHandle.readline().strip('\r\n')
        self.expire = rFileHandle.readline()
    def getUserID(self):
        return self.user_id 
    def getToken(self):
        return self.token
    def getExpire(self):
        return self.expire
