# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Request_test
   Description :
   Author :       elan
   date：          2/19/2018
-------------------------------------------------
   Change Activity:
                   2/19/2018:
-------------------------------------------------
"""

import requests

def test_requests_sampel(flag):
	response = requests.get('http://www.baidu.com')
	print(type(response), type(response.status_code), type(response.text), type(response.cookies), sep='\t')
	print(response.status_code, response.text, response.cookies, sep='\n')

