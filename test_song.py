#!/usr/bin/python
#-*-coding:utf-8-*-

import httplib,urllib,json,os,Queue,time;  #加载模块

from login import *
from pub import *
from song import *

s = songs(login())
#测试打印歌单
print s.song_lists.qsize()
while not s.song_lists.empty():
    song = s.song_lists.get()
    print song['title'],song['like']
    sid = song['sid']
    if s.song_lists.qsize() < 1:
        s.flushSongList(sid) 
