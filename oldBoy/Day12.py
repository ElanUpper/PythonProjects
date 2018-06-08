# author: elan

import os, time, sys

# os
print(os.getcwd()) # 获取当前工作目录 python的工作路径
# 切换工作目录
os.chdir(r'C:\Users\Administrator\PycharmProjects\tf\src')
#os.chdir("C:\\Users\\Administrator\\PycharmProjects\\tf\\src\\")
print(os.getcwd())
# 返回当前目录
print(os.curdir) # windows返回.
# 返回当前目录的父目录字符串
print(os.pardir)  # windows返回..
# 递归创建目录
#os.makedirs(r"c:\a\b\c")
# 递归删除目录  仅仅删除c:\a\b\c  a&b还存在
#os.makedirs(r"c:\a\b\e")
#os.makedirs(r"c:\a\e")
#os.removedirs(r"c:\a\b\c")

# 遍历文件夹下文件 包含隐藏文件
#print(os.listdir("C:\\"))   # . ..

# 删除文件 首先需要切换到某个目录+删除(批量) 或者直接删除
#os.chdir("C:/Users/Administrator/PycharmProjects/tf/src/oldBoy/")
#os.remove("write.md")

# 获取文件/目录的信息
print(os.stat(r'C:\Users\Administrator\PycharmProjects\tf\src\oldBoy\Day12.py'))

# 跨系统(系统路径分隔符，换行，
# os.name 系统平台
# os.sep 文件路径分隔符 c:\aa\bb  /usr/bin/xx
# os.linesep  换行符
print('%s: 文件路径分隔符 %s, 换行符 %s '%(os.name, os.sep, repr(os.linesep)))
print(os.environ.get('PATH').split(os.pathsep))  # 打印环境变量, os.pathsep: path环境变量的分隔符
print(os.system("dir")) # 执行系统命令 执行中文会乱码


file = r'readme.md'
# 获取一个文件的绝对路径  比如在当前文件夹下创建一个目录
abs_file = os.path.abspath(file)
# 分割绝对文件名->文件夹+路径
(file_dir, file) = os.path.split(abs_file)
file_dir = file_dir
# 判断是否path属于绝对路径
print('{} is absolute path? {}'.format(abs_file, os.path.isabs(abs_file)));
# 判断是否是文件
print('{} is a file? {}'.format(abs_file, os.path.isfile(abs_file)));
# 判断文件路径是否存在
print('{} is a exist? {}'.format(abs_file, os.path.exists(abs_file)));
# 判断是否是文件夹
print('{} is a directory? {}'.format(file_dir, os.path.isdir(file_dir)));
# 将list组合成绝对路径 目录需要带\\
print(repr(os.path.join('c:\\', 'a', 'b')))
# 获取文件的存取时间 修改时间
file = r'C:\Users\Administrator\PycharmProjects\tf\src\oldBoy\Day12.py'
print('{} \n create time {} \n access time {} \n modify time {} \n size {}'.format(
   file, time.ctime(os.path.getctime(file)),
         time.ctime(os.path.getatime(file)),
         time.ctime(os.path.getmtime(file)),
         str(round(int(os.path.getsize(file))/1024, 2)) + 'kb'
));


# sys.argv 调用python时候传入的参数 默认argv[0]是python路径地址
print('the called parameters', sys.argv)
# sys.exit 退出程序
#sys.exit(0)
# 打印python version
print(sys.version)
# 打印最大int
#print(sys.maxunicode, sys.maxsize)
# 操作系统平台
print(sys.platform)
# write data into stdin, read data from stdout
sys.stdout.write(input());
print(sys.stdin.readline()[:-1])
# sys.stdout.flush();

# 利用屏幕演示flush效果
for i in range(20):
    sys.stdout.write('#');
    sys.stdout.flush();
    time.sleep(0.1)