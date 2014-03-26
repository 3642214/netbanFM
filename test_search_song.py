#!/usr/bin/python
#-*-coding:utf-8-*-

import httplib,urllib,json,os,Queue,time;  #加载模块

from login import *
from pub import *
from netSong import *

s = searchSong()
#测试同名歌曲非第一首筛选
url = s.searchSongFrom163(u"陪我看日出",u"蔡淳佳",u"日出")
assert "1006053139423018.mp3" == os.path.basename(url)
#测试豆瓣歌手2名，网易歌手1名时查询问题
url = s.searchSongFrom163(u"Safe & Sound",u"The Civil Wars / Taylor Swift",u"The Hunger Games:...")
assert "1886761953293607.mp3" == os.path.basename(url)
#测试艺术家不同，歌名、专辑名相同问题
url = s.searchSongFrom163(u"爱要坦荡荡",u"萧希榆",u"Beautiful Angel")
assert "1117103813834573.mp3" == os.path.basename(url)
#测试没有的歌曲
assert None == s.searchSongFrom163(u"When You're Gone",u"Avril Lavigne",u"The Best Damn Thing")
#测试专辑名含空格
url = s.searchSongFrom163(u"问",u"梁静茹",u"理性与感性作品音乐会")
assert "5776834092362461.mp3" == os.path.basename(url)
