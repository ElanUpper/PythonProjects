#-*- coding: gbk -*-
# author: elan

# python3�ַ�������unicode ����coding�Ľ������ļ�����
# ��������ת����utf-8
# ��ɺ�����ת��Ϊgb2312

str = '���'
str_bytes = str.encode('gbk'); # ��unicode -> gbk
str_utf = str_bytes.decode('gbk').encode('utf-8') # gbk -> utf-8
print(str_utf.decode('utf-8'))
str_gb2312 = str_utf.decode('utf-8').encode('gb2312') # utf-8 -> gb2312
print(str_gb2312.decode('gb2312'))