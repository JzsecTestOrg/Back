__author__ = 'jinghua'
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
import datetime
import time
import json

url='http://123.59.70.148:8090/servlet/json'
param='funcNo=200003&stock_code=000555&market=SZ'
response = requests.post(url, data=json.dumps(param), timeout=10)
print('\nHTTP %d' % response.status_code)
print(response.text)
