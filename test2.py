import http.client

conn = http.client.HTTPConnection("xg-payservice-spark-1.elenet.me:7210")

payload = "{\n\"ver\": \"1.0\",\n\"soa\": {\"req\":\"12345\",\"rpc\":\"1.4.5.2\"},\n\"iface\": \"me.ele.napos.payservice.srv.spark.descriptor.service.TaskService\",\n\"method\": \"checkAndSync\",\n\"args\": {\n \"shopIds\":\"["+str(123)+"]\",\n \"flag\":\"true\"\n},\n\"metas\": {}\n}"

print(payload)
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "a8f0ad1d-75e9-869b-63ef-e80995f1f440"
    }

conn.request("POST", "/rpc", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))