#!/usr/bin/python
#-*-coding:utf-8-*-

import httplib,urllib,json,os,hashlib,time; 

sessionFile = 'session'

header = {"Content-Type":"application/x-www-form-urlencoded"}


def printNow(str):
    print time.strftime("%x %X",time.localtime(time.time())),str

def cmpArtist(str1,str2):
#    for str in str2.split(' / '):
#        if cmp(str1.lower(),str.lower()) == 0:
    if str1.lower().find(str2.lower()) >= 0 or str2.lower().find(str1.lower()) >=0: 
            return True
    return False

def cmpAlbum(str1,str2):
    if cmp("".join(str1.lower().split(' '))[:13],"".join(str2.lower().split(' '))[:13]) == 0:
        return True
    else:
        return False

def isFileEmpyty(filePath):
	if os.stat(filePath).st_size == 0:
		return True
	else:
		return False

def isFileExist(filePath):
	if os.path.isfile(filePath):
		return True
	else:
		return False

def encrypted_id(song_dfsId):
        byte1 = bytearray('3go8&$8*3*3h0k(2)2')
        byte2 = bytearray(str(song_dfsId))
        byte1_len = len(byte1)
        for i in xrange(len(byte2)):
            byte2[i] = byte2[i] ^ byte1[i % byte1_len]
        m = hashlib.md5()
        m.update(byte2.decode("utf-8"))
        result = m.digest().encode('base64')[:-1]
        result = result.replace('/', '_')
        result = result.replace('+', '-')
        return result

