# author: elan

import paramiko

host_name = '192.168.106.135';
port = 22;
user_name = 'root'
passwd = 'Wy880212'

# # 传递命令 接收结果
# ssh = paramiko.SSHClient();
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=host_name,
#                       port=port,
#                       username=user_name,
#                       password=passwd)
#
# stdin, stdout, stderr = ssh.exec_command('top');
# std_out, std_err = stdout.read().decode(), stderr.read().decode() ;
# print(std_out if std_out else std_err)
#
# ssh.close();


# 发送文件  一定要指定文件名
transport = paramiko.Transport((host_name, port));
transport.connect(username=user_name, password=passwd)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('Demo.py', '/home/elan/Demo.py')
# sftp.get('/home/elan/test.md', 'C:\\Users\\elan\\test.md' )
transport.close()
