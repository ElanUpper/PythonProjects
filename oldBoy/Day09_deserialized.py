# author: elan

import json
import pickle
#from Day09_serialized import *

def read_file_ex(file_name):
    with open(file_name, 'rb') as fp :
        ret_data = pickle.loads(fp.read())
    return ret_data;

# 直接对print_message函数进行改写
def print_message(x):
    for i in range(int(x)) :
        print(i)

if __name__ == '__main__' :

    # 解析函数 print_message
    # 如果这个文件中没有这个函数/或者自定义的 需要导入
    #  如果不愿意导入，可以在该文件中对function进行定义
    sav_data = read_file_ex('data_ex.md')
    print( type(sav_data), sav_data(3) )  # 这里返回了函数名称&参数列表&地址 ..



