# author: elan

g_name = 'elan'
g_arr = ['elan', 'jade']
g_set = {'elan', 'jade'}
g_dict = {'name':'elan', 'wife':'jade'}

# python函数 通用无法使用function直接修改global的变量
def fun_change_name():
    g_name = 'changed!'

# 强制修改global变量
def fun_change_name_ex():
    global g_name, g_age # age 内部定义外部可以使用
    g_name = 'changed!'
    g_age = 30
    # 修改 array set dict
    g_arr[0] = 'elan1'
    g_set.remove('elan')
    g_set.add('elan1')
    g_dict['name'] = 'elan1'

print('name = ', g_name)
fun_change_name()
print('name = ', g_name)
fun_change_name_ex()
print('name = ', g_name, ' age = ', g_age);
print('after change'.center(30, '-'));
print(g_arr, g_set, g_dict)

# 通过装饰器获取函数执行时间
# 装饰器 就是让使用者感觉它是透明的
#   1. 首先不改变使用者的调用方式以及参数
#   2. 其次不修改使用者的任何功能(源代码)，仅仅提供一个附件功能
import time
def timer(func):
    def wrapper(*args, **argv):
        start_time = time.time();
        func(*args);
        end_time = time.time();
        print('the function run time %s'%(end_time - start_time))
    return wrapper;

@timer
def calc(n):
    time.sleep(1)
    if(n/2 == 0):
        return
    print(n)
    n = int(n/2);
    return calc(n);


calc(10)
