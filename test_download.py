#!/usr/bin/python
#-*-coding:utf-8-*-

import subprocess

from login import *
from song import *
from netSong import *

s = searchSong()
url = s.searchSongFrom163(u"Sweeter Than Fiction",u"Taylor Swift",u"I Knew You Were Trouble")
print url
