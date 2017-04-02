#!/usr/bin/env python
# coding=utf8

import http.client, urllib,random,threading

httpClient = None
class myThread(threading.Thread):
    def __init__(self,init_num):
        threading.Thread.__init__(self)
        self.init_num = init_num

    def run(self):
        counter = 0
        global step
        while (True):
            self.init_num = self.init_num + 1
            code = random.randint(1000, 9999)
            params = urllib.parse.urlencode({'num': self.init_num, 'code': code})
            headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
                , "Accept": "text/plain"}
            httpClient = http.client.HTTPConnection("www.magiclub.cn", 8080, timeout=3000)
            httpClient.request("POST", "/Share/sendData", params, headers)
            if self.init_num % 100 == 0:
                print(self.init_num)
            counter = counter + 1

base = 100000
step = 100000
for i in range(1,5):
    myThread(base + i * step).start()
    print(base + i * step)
    print('\n')

