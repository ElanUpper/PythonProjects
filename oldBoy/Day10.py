# author: elan

import time

# time.sleep(1) # 休眠1秒
print(time.time()/3600/24/365+1970)  # 返回从19700101到现在的时间戳
print(time.gmtime())    # UTC 时间
print(time.localtime()) # 本地时间

# 获取struct_time
curr_time_struct = time.localtime();
print('current local struct time: ', curr_time_struct)
# struct_time -> 时间戳
curr_timestamp = time.mktime(curr_time_struct)
print('current local timestamp: ', curr_timestamp)
# struct_time -> 格式化time
curr_format_time  = time.strftime("%Y/%m/%d %H:%M:%S", curr_time_struct) ;
print('current format time: ', curr_format_time)

# 格式化time -> struct_time
curr_time_struct1 = time.strptime(curr_format_time, "%Y/%m/%d %H:%M:%S") ;
print('current local struct time1: ', curr_time_struct1)

# 时间戳 -> struct_time
curr_time_struct2 = time.localtime(curr_timestamp);  # local time
# curr_time_struct3 = time.gmtime(curr_timestamp);  # utc
print('current local struct time2: ', curr_time_struct2 )



#-------------- 格式化字符串输出  Sun May 27 23:00:37 2018
print('时间格式化输出'.center(30, '-'));
# structure time -> 格式化输出
print('before conversion: ', curr_time_struct2, '\nafter conversion: ', time.asctime(curr_time_struct2))

# 时间戳 -> 格式化输出
print('before conversion: ', curr_timestamp, '\nafter conversion: ', time.ctime(curr_timestamp))


# datetime
print('datetime 模块'.center(30, '-'));
import datetime as dt
print('当前时间: ', dt.datetime.now())
print(type(dt.datetime.now()), type(dt.timedelta(3)))
print('三天后时间: ', (dt.datetime.now() + dt.timedelta(3)))
print('三小时前时间: ', (dt.datetime.now() + dt.timedelta(hours=-3)))
print('替换后时间: ', ( dt.datetime.now().replace(year=3000, hour=2, minute=2)) )


