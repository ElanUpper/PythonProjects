#-*- coding: gbk -*-
# author: elan

# python3字符编码是unicode 上面coding的仅仅是文件编码
# 首先我们转换成utf-8
# 完成后我们转换为gb2312

str = '你好'
str_bytes = str.encode('gbk'); # 从unicode -> gbk
str_utf = str_bytes.decode('gbk').encode('utf-8') # gbk -> utf-8
print(str_utf.decode('utf-8'))
str_gb2312 = str_utf.decode('utf-8').encode('gb2312') # utf-8 -> gb2312
print(str_gb2312.decode('gb2312'))