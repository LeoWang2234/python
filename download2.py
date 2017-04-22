#!/usr/bin/python
#encoding:utf-8
import urllib.request
import os





def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print ('第 ' + str(pageNum)+' 个已下载'+' %.2f% %' % per)



for pageNum in [53]:
    url = 'http://oc.xjtu.edu.cn:80/upload/77/'+ str(pageNum) +'.flv'
    # url = "http://oc.xjtu.edu.cn:80/conver/flv/vod2/gkk/fengboqin1-1.flv"
    print(url)
    local = url.split('/')[-1]
    local = os.path.join('/Users/leo/Desktop/course_video',local)

    urllib.request.urlretrieve(url,local,Schedule)

