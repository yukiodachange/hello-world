# -*- coding: utf-8 -*-
"""
Herukuｎリクエストを投げる
"""

import requests
#import json

url = 'https://this-is-heroku.herokuapp.com/hello'
url = 'http://localhost:5000/hello'

method = 'POST'
headers = {'Content-Type' : 'application/json'}

# PythonオブジェクトをJSONに変換する
comment = input('Input comment to heroku > ')
obj = {'comment' : comment} 
#json_data = json.dumps(obj)

# req = requests.post(url, headers=headers, data=json_data)
req = requests.post(url, headers=headers, json=obj)

# エラー処理
req.raise_for_status

result_objs = req.json()
print (result_objs['response'])
