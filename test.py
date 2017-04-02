#
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
#
# import http.client,urllib
import http.client
FILE_PATH = '/Users/leo/PycharmProjects/splitstring/not_found.txt'
# FILE_PATH = '/Users/leo/PycharmProjects/splitstring/productnotfound.txt'

failed = open('responses.txt','w')
def main():
    with open(FILE_PATH, 'r') as f:
        for num in f:
            # first = line.split(":")[0]
            # num = first[1:-1]
            num = num[0:-1]
            print(type(num))
            conn = http.client.HTTPConnection("xg-payservice-spark-1.elenet.me:7210")

            payload = "{\n\"ver\": \"1.0\",\n\"soa\": {\"req\":\"12345\",\"rpc\":\"1.4.5.2\"},\n\"iface\": \"me.ele.napos.payservice.srv.spark.descriptor.service.TaskService\",\n\"method\": \"checkAndSync\",\n\"args\": {\n \"shopIds\":\"["+num+"]\",\n \"flag\":\"true\"\n},\n\"metas\": {}\n}"

            # print(payload)
            headers = {
                'content-type': "application/json",
                'cache-control': "no-cache",
                'postman-token': "41ca6966-bf08-587a-d9dd-1dda3adeea3e"
            }

            conn.request("POST", "/rpc", payload, headers)

            res = conn.getresponse()
            data = res.read()

            # if "获取标品失败" in data.encode(encoding='utf-8'):

            # failed.write('------------------------------------')
            # data.decode("utf-8")
            failed.write('\n')
            failed.write(str(num))
            failed.write('\n')
            failed.write(str(data))
            failed.write('\n')
            # failed.write('------------------------------------')

            print(data.decode("utf-8"))

if __name__ == '__main__':
        main()
