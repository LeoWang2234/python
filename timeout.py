import http.client

import datetime

#long running


conn = http.client.HTTPConnection("xg-pcd-shop-operation-service-1.elenet.me:8859")

payload = "{\n \"ver\":\"1.0\",\n \"soa\":{\n     \"rpc\":\"2\",\n     \"req\":\"2\"\n },\n \"iface\":\"me.ele.operation.xy.service.ITaskService\",\n \"method\":\"getTaskDetail\",\n \"args\":{\n  \"applyId\":949737,\n  \"type\": \"\\\"AUDIT\\\"\"\n },\n \"metas\":null\n}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "32fc92bd-7b22-c1cf-292a-c3c5e0d2ad21"
    }

starttime = datetime.datetime.now()
conn.request("POST", "/rpc", payload, headers)

res = conn.getresponse()
data = res.read()

endtime = datetime.datetime.now()
print (endtime - starttime)

print(data.decode("utf-8"))