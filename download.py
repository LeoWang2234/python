import shutil
import requests

res = requests.get('http://oc.xjtu.edu.cn:80/upload/77/8.flv')

f = open('/Users/leo/Desktop/course_video/a.flv','wb')
shutil.copyfileobj(res.raw,f)
f.close();