# coding:utf-8
__author__ = 'zhongyaqi'

import requests
import json,time
#help(requests)
# r=requests.get("https://python.org")
# print r.status_code
# #print r.json()
# print r.content
# print r.text

# payload=dict(key1='value1',key2='value2')
# r=requests.post("http://httpbin.org/post",data=payload)
# print(r.text)

payload={"yoyo":"hello",
    "python":'8888888'
}
#转换成json格式
data_json=json.dumps(payload)
r=requests.post("http://httpbin.org/post",data=data_json)
print(r.text)
time.time()
print time.time()