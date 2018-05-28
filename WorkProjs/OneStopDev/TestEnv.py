# encoding: utf-8

import os
from sqlite3 import connect

class TestAnalysis:
    def __init__(self, db_file):
        self.db_file = db_file
        self.f = open(self.db_file, "rb")
        self.stats = os.stat(self.db_file)
        self.filesize = self.stats.st_size
        self.f.seek(0)

    def db_header(self):
        head = self.f.read(100)
        print('头字符串 {}'.format(head[0:16].decode())) # 查看sqlite 头文件格式
        # 0000 53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33 00
        t = []
        for i in head[16:18]:
            t.append('{:02X}'.format(i))
        r = "".join(t)
        pagesize = int(r, 16) # 从16进制转换为整数
        print('页大小: {}'.format(pagesize))
        # 下面代码为上面代码的精简版
        print('页大小: {}'.format( int(''.join( ['{:02X}'.format(i) for i in head[16:18]] ), 16 )))

    def write_txt(self):
        with open('text.md', 'a') as fp:
            fp.write('这是一个测试文件')
        return 'OK'

def create_db():
    conn = connect('record.db')
    cursor = conn.cursor();
    cursor.execute("""
     create table book (
       Title  nvarchar(100),
       Author nvarchar(20),
       Price  numeric(8, 2),
       Preface nvarchar(200),
       Discontinued BOOLEAN DEFAULT 1,
       PubDate  DATETIME
     )
    """);
    conn.commit();


if __name__ == "__main__" :
    check_file = os.path.isfile('record.db');
    if check_file is False:
        create_db()

    try:
        analysis = TestAnalysis('record.db')
        analysis.db_header();
        analysis.write_txt();
    except Exception as e:
        print('{}, 报错！！！'.format(e))
    finally:
        a = lambda x:'它会执行的，你放心好了！'+x
        print('{}'.format(a('!')))
        assert 1 == 1
        print('上面的assert执行成功')
    sum = lambda x,y : x+y
    genA = [sum(i, i) for i in range(10)]
    sumAll = (i for i in range(10))
    # print(sumAll.__next__())  10 次
    for iter in sumAll:
        print(iter)
    #print('{}'.format(sum(i, i): for i in range(20)))



