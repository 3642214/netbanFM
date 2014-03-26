#!/usr/bin/python
#-*-coding:utf-8-*-

import subprocess

from login import *
from song import *
from netSong import *

s = songs(login())
while(not s.song_lists.empty()):
    printNow(">>>>>>>>>>start")
    playSong = s.song_lists.get()
    #print playSong['title']
    #print playSong['albumtitle']
    #print playSong['artist']
    song = searchSong()
    url = song.searchSongFrom163(playSong['title'],playSong['artist'],playSong['album'])
    sid = playSong['sid']
    print url
    print type(url)
    if url:
        p = subprocess.Popen(['wget','-O',"/Users/zj/Music/"+playSong['title']+".mp3",url])
        returnCode = p.wait()
    #time.sleep(song.playTime + 1)
    #time.sleep(playSong['length']+1)
        print returnCode
    printNow("stop<<<<<<<<<<< ")
    if s.song_lists.qsize() < 2:
#        print 'empty'
        s.flushSongList(sid)      
    
