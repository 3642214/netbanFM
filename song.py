#!/usr/bin/python
#-*-coding:utf-8-*-

import httplib,urllib,json,os,Queue,time;  #加载模块

from login import *
from pub import *

class songs:
    song_lists = Queue.Queue(maxsize = 100)
    __sid = 0
    __user_id = ''
    __token = ''
    __expire = ''
    channel_no = '-3'
    
    def __init__(self,login):
        self.user_id = login.getUserID()
        self.token = login.getToken()
        self.expire = login.getExpire()
        self.initSongList()

    def initSongList(self):
        conn = httplib.HTTPConnection("www.douban.com")
        conn.request("POST","/j/app/radio/people",self.urlEncode('n',self.channel_no,None),header)
        response = json.loads(conn.getresponse().read())
        conn.close()
        #print response
        self.createSongList(response["song"])

    def flushSongList(self,sid):
        try:
            conn = httplib.HTTPConnection("www.douban.com")
            conn.request("POST","/j/app/radio/people",self.urlEncode('p',self.channel_no,sid),header)
            response = json.loads(conn.getresponse().read())
            conn.close()
            #print response
            self.updateSongList(response["song"])
        except:
            print '----------------try again------------:'
            time.sleep(1)
            self.flushSongList(sid)

    def nextSong(self,sid):
        conn = httplib.HTTPConnection("www.douban.com")
        conn.request("POST","/j/app/radio/people",self.urlEncode('s',self.channel_no,sid),header)
        response = json.loads(conn.getresponse().read())
        conn.close()
        self.createSongList(response["song"])

    def createSongList(self,songsResponse):
        for songResponse in songsResponse:
            self.song_lists.put(self.getSongInfo(songResponse))

    def updateSongList(self,songsResponse):
        newlist = Queue.Queue(maxsize = 100)
        for songResponse in songsResponse:
            newlist.put(self.getSongInfo(songResponse))
        self.song_lists = newlist
        
    def getSongInfo(self,songRsp):
        return {'title':songRsp['title'],
                'artist':songRsp['artist'],
                'album':songRsp['albumtitle'],
                'sid':songRsp['sid'],
                'url':songRsp['url'],
                'length':songRsp['length'],
                'like':songRsp['like']}

    def urlEncode(self,type,channel,sid):
        params = {'user_id':self.user_id,
                  'token':self.token,
                  'expire':self.expire,
                  'channel':'0',
                  'type':type,
                  'sid':sid,
                  'app_name':'radio_desktop_win',
                  'version':100}
        if channel:
            params['channel'] = channel
        if sid:
            params['sid'] = sid
        return urllib.urlencode(params)

