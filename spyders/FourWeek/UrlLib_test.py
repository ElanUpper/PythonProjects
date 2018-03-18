# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     UrlLib_test
   Description :
   Author :       elan
   date：          2/18/2018
-------------------------------------------------
   Change Activity:
                   2/18/2018:
-------------------------------------------------
"""

import urllib.request, urllib.error, urllib.parse, socket

url = 'http://httpbin.org/'

# get
def test_get_method():
	response = urllib.request.urlopen(url+'ip');
	print(type(response)) # <class 'http.client.HTTPResponse'>
	print(response.status, response.getheaders(), response.getheader('Content-Type'))
	print(response.read().decode('utf-8'));


# post
def test_post_method():
	input_data = bytes(urllib.parse.urlencode({"origin": "113.200.173.137"}), encoding='utf-8');
	response = urllib.request.urlopen(url+'post', data=input_data);
	print(response.read().decode('utf-8'))


# timeout
def test_timeout():
	try:
		response = urllib.request.urlopen(url+'get', timeout=0.1);
		print(response.read().decode('utf-8'));
	except urllib.error.URLError as e:
		if isinstance(e.reason, socket.timeout):
			print('time out')


# user-defined header
def test_add_headers():
	request_header = {
		'Host' : 'httpbin.org',
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
	};
	#req_get = urllib.request.Request(url=url+'ip', data=input_data, headers=request_header, method='GET');
	req_post = urllib.request.Request(url=url+'post', data=input_data, headers=request_header, method='POST');
	req_post.add_header('test_key', 'test_value') # 可以一条一条header的添加
	response = urllib.request.urlopen(req_post);
	print(response.read().decode('utf-8'))

# 添加代理
def test_add_proxy():
	proxy_handler = urllib.request.ProxyHandler({
		'http':'104.129.202.53:8800',
		'https':'47.89.251.46:3128'
	});
	opener = urllib.request.build_opener(proxy_handler);
	response = opener.open(fullurl=url+'ip');
	print(response.read().decode('utf-8'));


# cookie
def test_add_cookie(flag): # flag 1:display  2:save to file 3. load cookie from file
	import http.cookiejar
	fileName = 'Cookie.txt';
	if flag == 1 :
		cookie = http.cookiejar.CookieJar();
	elif flag == 2 :
		cookie = http.cookiejar.MozillaCookieJar(fileName);
	elif flag == 3 :
		cookie = http.cookiejar.MozillaCookieJar();
		cookie.load(fileName, ignore_discard=True, ignore_expires=True)
		for item in cookie :
			print(item.name + '=' + item.value);
	cookie_handler = urllib.request.HTTPCookieProcessor(cookie);
	opener = urllib.request.build_opener(cookie_handler);
	response = opener.open('https://www.baidu.com');
	if flag == 1:
		for item in cookie:
			print(item.name + '=' + item.value);
	elif flag == 2:
		cookie.save(ignore_discard=True, ignore_expires=True)

#test_add_cookie(3);

# 异常处理
def test_err_handler():
	try:
		response = urllib.request.urlopen('http://www.directlygowrong.com');
	except urllib.error.HTTPError as e:
		print(e.reason, e.code, e.headers, sep=' ');
	except urllib.error.URLError as e: # HTTPError是URLError的子类
		print(e.reason);
	else:
		print(response.read().decode('utf-8'))


def test_url_parse(url):
	default_schema = 'https' ;
	result = urllib.parse.urlparse(url, scheme=default_schema); # fragment 就是锚点
	print(result);

def test_url_deparse() :
	url_list = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
	url = urllib.parse.urlunparse(url_list)
	print(url);

#test_url_parse('https://www.baidu.com/index.html;user,name,password?rsv_idx=1&tn=baidu#comment')
#test_url_parse('www.baidu.com/index.html;user,name,password?rsv_idx=1&tn=baidu#comment') # 注意第二个参数netloc
#test_url_deparse()

# 可以将字典格式直接提供给url使用
def test_url_encode():
	params = {
		'name':'elan',
		'age':30
	};
	base_url='http://www.test.com?';
	url=base_url + urllib.parse.urlencode(params);
	print(url);

test_url_encode()