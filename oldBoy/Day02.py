# author: elan

# 格式化打印
name = 'elalnln'
nam1 = 'jade'
### 补齐集合
print(name.center(20, '-')) # 打印20个字符 不够就用-补齐
print(name.ljust(40, '*'))  # 左对齐后续补齐*
print(name.rjust(40, '*'))  # 右对齐后续补齐*
print('4200000'.zfill(20))  # 补0操作
# 判断字符串是否已xx结尾
print(name.endswith('an'))
# 替换\t为多少个空格
    # 如果format没有带具体参数名称，那么后面替换placeholder就依次进行替换
print('hello\t{} {}'.format(name, nam1).expandtabs(20))
    # 如果format带具体参数名称，那么后面替换placeholder必须添加参数名称=替换值
print('hello\t{name} {name1}'.format(name=name, name1=nam1).expandtabs(20))

print(('hello\t%s'% name).expandtabs(20))
# 查找字符串位置 0开始
print('find l lowest index is ' + str(name.find('l')) )  # 找第一个
print('find l highest index is ' + str(name.rfind('l')) ) # 找最后一个

welWord = 'hello, {name}'
print(welWord.format(name='elan'))
print(welWord.format_map({'name':'elan'}))

print('10'.isalpha())
print('10'.isdigit())
print('10'.isdecimal())  # 返回是否是十进制
print('aa'.isidentifier()) # 判断是否是一个合法的变量名称

strList=['\n','a',1,2,3,4,'A' ]
# 因为''.jon([list]) list必须是字符串类型 如果是integer那么会报错
# 所以我们这里需要先将integer转换为string
afterProcess = ','.join([str(i) for i in strList])
print(afterProcess.lower(), '\n', afterProcess.upper())
print(afterProcess, afterProcess.strip())

# python 加密 解密
pKey = str.maketrans('habefl', '~@!&8%')
rKey = str.maketrans('~@!&8%', 'habefl')
print(type(pKey), pKey)
print('hello, elan'.translate(pKey)) # 加密
print('hello, elan'.translate(pKey).translate(rKey)) # 解密

# 替换
print('hello, kit'.replace('l', 'L')) # 默认替换全部
print('hello, kit'.replace('l', 'L', 1)) # 制定替换多少个

# 提取数字
print('1+2+3+4'.split('+'))
print('1\n2\n3\n'.splitlines()) # 按照换行分割字符
print('Hello,eLAN'.swapcase()) # 反转大小写