# -*- coding: utf-8 -*-
"""
Herukuｎリクエストを投げる
"""

import urllib.request
import json

url = 'https://this-is-heroku.herokuapp.com/hello'
method = 'POST'
headers = {'Content-Type' : 'application/json'}

# PythonオブジェクトをJSONに変換する
comment = input('Input comment to heroku > ')
obj = {'comment' : comment} 
json_data = json.dumps(obj).encode("utf-8")

req = urllib.request.Request(url, data=json_data, method=method, headers=headers)

try:
    with urllib.request.urlopen(req) as res:
        body = res.read().decode('utf-8')
except urllib.error.HTTPError as err:
    print(err.code)
except urllib.error.URLError as err:
    print(err.reason)

result_objs = json.loads(body.split('\n')[0])
print (result_objs['response'])
