# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RegularTest
   Description :
   Author :       elan
   date：          2/21/2018
-------------------------------------------------
   Change Activity:
                   2/21/2018:
-------------------------------------------------
"""

# tool.oschina.net/regex/#

import re

str1 = 'Hello 123 456 World_This is a Regex Demo';
str2 = '''Hello 123 
			 456 World_This is a Regex Demo''';
str3 = 'the price is $5.0';

###------------------------- match ---------------------------
# 需要整体匹配 否则返回None

def test_common_regex():
	result = re.match('^\w{5}\s\d{3}\s\d{3}\s$', str1)
	if result == None :
		print(result)
	else :
		print(result.group(), result.span())

def test_extensive_regex():
	result = re.match('^Hello.*Demo$', str1)
	print(result.group())

# 抓取123 456
def test_specified_target():
	result = re.match('^Hello\s(\d{3}\s\d{3}).*$', str1)
	print(result.group(1))

# 贪婪匹配
# Hello.*(\d+)  .*会尽可能多的匹配结果 导致\d仅仅返回1个数字尽管可以返回3个
def test_greed_match():
	result = re.match('^Hello.*(\d+\s\d{3}).*$', str1)
	print(result.group(1))

# 'Hello.*?(\d+)' .*?会尽可能多的匹配结果
def test_ungreed_match():
	result = re.match('^Hello.*?(\d+\s\d{3}).*$', str1)
	print(result.group(1))

# 特殊字符匹配
def test_special_chars():
	# 匹配str2中的123456
	#result = re.match('^.*(\d{3}\s*\d{3}).*Demo$', str2, re.DOTALL)
	result = re.match('^.*(\d{3}.*\d{3}).*Demo$', str2, re.DOTALL)
	print(result.group(1))


# 匹配转义字符
# 匹配出字符$5.0
def test_escape_chars():
	result = re.match('^.*($\d.\d)$', str3)
	print(result.group(1))


###------------------------- search ---------------------------
# 扫描整体字符串 返回第一个
html = '''<div id="songs-list">
		<h2 class="title">经典老歌</h2>
		<p class="introduction">
				经典老歌列表
		</p>
		<ul id="list" class="list-group">
				<li data-view="2">一路上有你</li>
				<li data-view="7">
						<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
				</li>
				<li data-view="4" class="active">
						<a href="/3.mp3" singer="齐秦">往事随风</a>
				</li>
				<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
				<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
				<li data-view="5">
						<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
				</li>
		</ul>
</div>'''

def sample_search():
	# <class '_sre.SRE_Match'>
  result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.DOTALL);
  if result :
    print(type(result), result.group(1), result.group(2));

###------------------------- search ---------------------------
# 扫描整体字符串 返回查找到的全部

def sample_findall():
	# <class 'list'>
	result = re.findall('<li.*?singer="(.*?)">(.*?)</a>', html, re.DOTALL);
	for item in result :
		print('singer:{0}, song:{1}'.format(item[0], item[1]))

def sample_full_findall():
	# <class 'list'>  |(.*?)
	result = re.findall('<li.*?>.*?<a href="(.*?)".*?singer="(.*?)">(.*?)</a>.*?</li>', html, re.DOTALL);
	#result.append(re.findall('<li.*?>(.*?)</li>', html, re.DOTALL))
	for item in result :
		print('mp3:{0}, singer:{1}, song:{2}'.format(item[0], item[1], item[2]))

sample_full_findall()
