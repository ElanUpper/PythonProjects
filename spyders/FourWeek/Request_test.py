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

import requests, json

url = 'http://httpbin.org/';

data = {
	'name': 'elan',
	'age': 24
}

request_header = {
	'Host': 'httpbin.org',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
};

# flag 1:get 2:post 3:delete 4:put 5:head 6:options
def test_requests_sampel(flag):
	if flag == 1:
		response = requests.get(url+'get', headers = request_header);
		#print(type(response), type(response.status_code), type(response.text), type(response.cookies), sep='\t')
		print(response.url, response.status_code, response.headers, response.history,
					response.text, response.cookies, sep='\n')
		if response.status_code == requests.codes.ok :
			print('access successfully')
			#print(json.load(response.text))
			#print(response.json())
	elif flag == 2:
		response = requests.post(url+'post', data=data, header = request_header);
		print(response.text);
	elif flag == 3:
		response = requests.delete(url+'delete');
		print(response.text);
	elif flag == 4:
		response = requests.put(url+'put');
		print(response.text);
	elif flag == 5:
		response = requests.head(url+'head');
		print(response.text);
	elif flag == 6:
		response = requests.options(url+'options');
		print(response.text);

#test_requests_sampel(1);

# 上传文件
def test_upload_file():
	files={
		'file': open('favicon.ico', 'rb')
	}
	response = requests.post(url+'post', files=files)
	print(response.text)

# 获取cookies
def test_get_cookie():
	response = requests.get(url);
	for (key, value) in response.cookies.items():
		print(key + ':' + value);

# 会话维持
def test_keep_session():
	cur_session = requests.Session();
	response = cur_session.get(url+'cookies/set/number/1234');
	print(response.text)
	response = cur_session.get(url+'cookies');
	print(response.text)
#test_keep_session();

# 代理
def test_proxy():
	proxies = {
		'http': '104.129.202.53:8800',
		'https': '47.89.251.46:3128'
	  # 'http': 'http://user:password@172.192.3.3:8000'
	};
	# socks
	# pip install 'requests[socks]'
	proxies_socks = {
		'http': 'socks5://104.129.202.53:8800',
		'https': 'socks5://47.89.251.46:3128'
	}

	response = requests.get(url, proxies=proxies);
	print(response.status_code);

# timeout setting
def test_timeout():
	from requests.exceptions import ReadTimeout, ConnectionError, HTTPError, RequestException
	try:
		response = requests.get(url, timeout=1);
		print(response.status_code);
	except ReadTimeout:
		print('Timeout');
	except ConnectionError:
		print('Connection Error');
	except HTTPError:
		print('Http Error');
	except RequestException :
		print('Request Error');

#test_timeout();

# 证书验证
def test_verify_cert():
	# 防止warning显示
	from requests.packages import urllib3
	urllib3.disable_warnings();
	#response = requests.get('https://12306.cn')
	response = requests.get('https://12306.cn', verify=False)
	print(response.status_code)

# 证书设置
def test_use_cert():
	url = '120.27.34.24:9001';
	from requests.auth import HTTPBasicAuth
	response = requests.get(url, auth=HTTPBasicAuth('user', '123'))
	#response = requests.get(url, auth=('user', '123'))
	print(response.status_code)