# -*- coding: utf-8 -*-
"""
Herukuｎリクエストを投げる
"""

import requests
import json

url = 'https://this-is-heroku.herokuapp.com/hello'
method = 'POST'
headers = {'Content-Type' : 'application/json'}

# PythonオブジェクトをJSONに変換する
comment = input('Input comment to heroku > ')
obj = {'comment' : comment} 
json_data = json.dumps(obj).encode("utf-8")

req = requests.post(url, data=json_data)

# エラー処理
req.raise_for_status

result_objs = req.json()
print (result_objs['response'])
