# author: elan
# file

steps = [];
lines = [];

with open('yestorday.res', encoding="utf-8") as fp:
  readstr = fp.read(); # 一行全部读出

with open('yestorday.res', encoding="utf-8") as fp:
  lines = fp.readlines(); # 直接返回list

# 注意steps是一行字符串 需要切成数组
for item in readstr.split('\n')[0:2]:
  print(type(item), item)

# 打印前五行
for (number, item) in enumerate(lines[5:11])  : # 因为有\n 所以需要替换
  if(number+5 == 9) :
      print('line 10'.center(30, '-'))
  print(type(item), number, item.strip('\n'))


# 如果读取大数据量的文件
count = 0 ;
with open('yestorday.res', encoding="utf-8") as fp:
    for line in fp.read():
        # 打印读取了多少字符
        print(fp.tell()); # seek 跳转到哪里 0 开始
        print(line);
        count += 1 ;
        if count > 5 :
            break;


# 写文件
fp = open('write.md', 'w', encoding='utf-8');
fp.write('你好');
fp.close();
# 采用安全读写， 注意w方式会被覆盖
with open('write.md', 'w', encoding='utf-8') as fp:
    fp.write('hello，你好')
with open('write.md', 'a', encoding='utf-8') as fp:
    fp.write('\nhello，追加')
