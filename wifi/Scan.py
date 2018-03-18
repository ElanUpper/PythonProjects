# -*- coding: utf-8 -*-

from access_points import get_scanner
from functools import reduce

# 返回需要wifi信息
def parse_wifiInfo(ap):
	return (ap['quality'], ap['ssid'], ap['bssid'])

# 加工返回wifi信息为需要信息
def summary_wifiName(a1, a2):
	if(type(a1) == tuple) :
		a1 = a1[1]
	if (type(a2) == tuple):
		a2 = a2[1]
	return str(a1) + ',' + str(a2)

if __name__ == '__main__':
	wifi_scanner = get_scanner()
	# ssid=baby, bssid=b8:08:d7:65:30:28, quality=99, security=WPA2-Personal
	wifi_aps = wifi_scanner.get_access_points()
	wifi_infos = map(parse_wifiInfo, wifi_aps)
	wifi_name = reduce(summary_wifiName, wifi_infos)
	wifis =  wifi_name.split(',')
	print(wifis)