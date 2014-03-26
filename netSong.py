#!/usr/bin/python
#-*-coding:utf-8-*-

import httplib,urllib,json,os,urllib2,random,subprocess 

cookie_opener = urllib2.build_opener()
cookie_opener.addheaders.append(('Cookie', 'appver=1.5.2'))
urllib2.install_opener(cookie_opener)


from pub import *

class searchSong:
    url = ''
    playTime = ''

    def searchSongFrom163(self,songname,artist,album):
        print u"歌曲名：",songname
        print u"艺术家：",artist
        print u"专辑名：",album
        search_url = 'http://music.163.com/api/search/get'
        params = {
                's': songname.encode('utf-8') ,
                'type': 1,
                'offset': 0,
                'sub': 'false',
                'limit': 50
        }
        params = urllib.urlencode(params)
        resp = urllib2.urlopen(search_url, params)
        resp_js = json.loads(resp.read())
        if resp_js['code'] == 200 and resp_js['result']['songCount'] > 0:
            result = resp_js['result']
            song_id = result['songs'][0]['id']
            print u"搜索到个数:",result['songCount']
            if result['songCount'] > 1:
                id = self.filte_with_artist(result['songs'],artist,album)
                if not id:
                    print 'not found then use album to search ...'
                    id = self.filte_with_album(result['songs'],artist,album)
                    if not id:
                        print 'not found song:%s\tartist:%s\talbum:%s' % (songname,artist,album)
                else:
                    song_id = id
            return self.songID2url(song_id)
        else:
            return None

    def songID2url(self,song_id):
        detail_url = 'http://music.163.com/api/song/detail?ids=[%d]' % song_id
        resp = urllib2.urlopen(detail_url)
        song_js = json.loads(resp.read())
        songRealID = song_js['songs'][0]['bMusic']['dfsId']
        self.url = 'http://m%d.music.126.net/%s/%s.mp3' % (random.randrange(1, 3), encrypted_id(songRealID), songRealID)
        return self.url

    def filte_with_artist(self,song_list,artist,album):
        for i in range(len(song_list)):
            song = song_list[i]
            print u"歌单,第%d个：艺术家：%s,专辑名：%s" % (i,song['artists'][0]['name'],song['album']['name'])
            if cmpArtist(song['artists'][0]['name'],artist) and cmpAlbum(song['album']['name'],album):
                print "--------->> found it <<-----------"
                self.playTime = song_list[i]['duration']
                return song_list[i]['id']
                break
            else:
                print '<<<< next >>>>'
                if i == len(song_list) - 1:
                    print '----<<<< no more >>>>----'
                    return None

    def filte_with_album(self,song_list,artist,album):
        for i in range(len(song_list)):
            song = song_list[i]
            if cmpAlbum(song['album']['name'],album):
                print "--------->> found it <<-----------"
                print u"艺术家：%s,专辑名：%s" % (song['artists'][0]['name'],song['album']['name'])
                self.playTime = song_list[i]['duration']
                return song_list[i]['id']
                break
            else:
                if i == len(song_list) - 1:
                    return None
