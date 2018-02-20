# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     FirstStep
   Description :
   Author :       elan
   date：          2/17/2018
-------------------------------------------------
   Change Activity:
                   2/17/2018:
-------------------------------------------------
"""

import time
import urllib
from selenium import webdriver
# pip install Pillow
from PIL import Image
from PIL import ImageChops
from selenium.webdriver.common.action_chains import ActionChains

sleep_time = 0.5

def input_by_id(driver, text=u'', element_id=''):
	input_element = driver.find_element_by_id(element_id)
	input_element.clear();
	input_element.send_keys(text);
	time.sleep(sleep_time);

def click_by_id(driver, element_id=''):
	search_element = driver.find_element_by_id(element_id);
	search_element.click();
	time.sleep(sleep_time);

def click_by_class(driver, element_class=''):
	search_element = driver.find_element_by_class_name(element_class);
	search_element.click();
	time.sleep(sleep_time);

def same_pixel_position(RGB1, RGB2):
	for cur_rgb in range(0, 3):
		print(RGB1[cur_rgb], RGB2[cur_rgb])
		if abs(RGB1[cur_rgb] - RGB2[cur_rgb]) >= 50 :
			return False
		return True

def diff_images_pixel(img1, img2):
	img1_width  = img1.size[0];
	img1_height = img1.size[1];
	img2_width = img2.size[0];
	img2_height = img2.size[1];
	RGB1 = img1.getpixel((20, 20));
	RGB2 = img2.getpixel((3, 5));
	same_pixel_position(RGB1, RGB2)
	# 一个点的RGB颜色一致

img1 = Image.open('C://Users//elan//Desktop//pic//1.jpg')
img2 = Image.open('C://Users//elan//Desktop//pic//2.jpg')
diff_images_pixel(img1.convert("RGBA"), img2.convert("RGBA"))

'''

options = webdriver.ChromeOptions();
options.add_argument('--window-position=0,0');
options.add_argument('--window-size=800,600');

driver = webdriver.Chrome(chrome_options=options);
driver.get('https://game.captcha.qq.com/hslj/html/hslj/')

input_by_id(driver, 'wadeyang', 'user-input');
input_by_id(driver, '914645774', 'qq-input');
click_by_id(driver, 'login-btn');
click_by_class(driver, 'hslj-game-btn');

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#转换 webdriver 的工作环境至子 iframe，通过 tag_name 查找网页元素
img1ele = driver.find_element_by_id("slideBlock") #获取缺块
img2ele = driver.find_element_by_id("slideBkg")   #获取整体图片
src1 = img1ele.get_attribute("src"); 	#得到原始 img 路径
src2 = img2ele.get_attribute("src"); 	#得到缺口 img 路径
driver.switch_to.default_content() 		#转换 webdriver 工作环境至默认
urlopen = urllib.request   #urllib 模块，可通过 pip 安装，import urllib 引用
fp = urlopen.urlopen(src1) #打开原始img路径
data1 = fp.read()  #读取数据
fp.close()
file = open('C://Users//elan//Desktop//pic//1.jpg', 'wb') #将原始img保存为 d://1.jpg
file.write(data1)
file.close()
fp = urlopen.urlopen(src2) #打开缺口 img 路径
data2 = fp.read()
fp.close()
file = open('C://Users//elan//Desktop//pic//2.jpg', 'wb') #将缺口 img 保存为 d://2.jpg
file.write(data2)
file.close()

img1 = Image.open('C://Users//elan//Desktop//pic//1.jpg');
img1_a = img1.convert('RGBA');
img1_a.save('C://Users//elan//Desktop//pic//1_a.png');
#print(img1.format, img1.size, img1.mode)

img2 = Image.open('C://Users//elan//Desktop//pic//2.jpg');
img2_a = img2.convert('RGBA');
img2_a.save('C://Users//elan//Desktop//pic//2_a.png');
#print(img2.format, img2.size, img2.mode)

img3 = ImageChops.difference(img1_a, img2_a);
img3.save('C://Users//elan//Desktop//pic//3.png')

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
dragger = driver.find_element_by_id("slideBlock")
action = ActionChains(driver)
action.click_and_hold(dragger).perform(); #鼠标左键按下不放
#action.reset_actions()
#time.sleep(sleep_time)
action.move_by_offset(100, 100).perform(); #移动到哪里
#action.reset_actions()
action.release().perform(); #鼠标左键松开
#action.reset_actions()
driver.switch_to.default_content()

'''