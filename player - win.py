#!/usr/bin/python
#-*-coding:utf-8-*-

import subprocess

from login import *
from song import *
from netSong import *

s = songs(login())
#for song in s.getSongs():
#    print song['title']
#    sid =  song['sid']
#s.flushSongList(sid)
#for song in s.getSongs():
#    print song['title']
#    subprocess.call(['mplayer', search_song(song['title'],song['artist'],song['album'])])
while(not s.song_lists.empty()):
    printNow(">>>>>>>>>>start")
    playSong = s.song_lists.get()
    #print playSong['title']
    #print playSong['albumtitle']
    #print playSong['artist']
    song = searchSong()
    url = song.searchSongFrom163(playSong['title'],playSong['artist'],playSong['album'])
    #print playSong['length']
    p = subprocess.Popen(['vlc.exe',url])
    sid = playSong['sid']
    #returnCode = p.wait()
    time.sleep(song.playTime + 1)
    time.sleep(playSong['length']+1)
    p.kill()
    #print returnCode
    printNow("stop<<<<<<<<<<< ")
    if s.song_lists.qsize() < 2:
#        print 'empty'
        s.flushSongList(sid)      
    
