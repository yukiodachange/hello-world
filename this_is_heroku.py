# -*- coding: utf-8 -*-
"""
Heroku返答用webアプリ
"""

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

#from urllib.parse import urlparse, urlencode
#from urllib.request import urlopen, Request
#from urllib.error import HTTPError

#import json
import os
#import datetime

from flask import Flask
from flask import request
from flask import make_response, jsonify
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials


# Flask app should start in global layout
app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    req = request.get_json(silent=True, force=True)
    result = req.get('comment')
    if 'Good morning' in result:
        comment = result
    else:
        comment = 'こんにちはHEROKUです。'
    
    r = make_response(jsonify({'response':comment}))
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
