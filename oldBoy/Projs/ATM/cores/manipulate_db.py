# author: elan

import sqlite3
from functools import reduce

class inter_db :

    def __init__(self, name):
        self.__conn = sqlite3.connect(name + '.db');

    def create_table(self, table_name, **kwargv):
        # build create table语句
        exec_sql = 'create table {} ( '.format(table_name) ;
        # 组合每一列字段
        sql_columns = '';
        for (key, val) in kwargv.get('kwargv').items() :
            if key != '*':
                # 解析 columns -->
                sql_columns = sql_columns + ' {} {} {}'.format(key, val, ',')
            else :
                # 解析 * --> primary key
                primary_keys = val
        else :
            sql_keys = ' primary key({}) '.format(primary_keys)
            exec_sql = exec_sql + sql_columns + sql_keys +  ')'

        # 打印并执行create 语句
        print(exec_sql)
        self.__conn.execute(exec_sql)
        self.__conn.commit()

    # drop table
    def drop_table(self, table_name):
        exec_sql = 'drop table {}'.format(table_name)
        try:
            self.__conn.execute(exec_sql)
            self.__conn.commit()
        except Exception as e:
            print(e)

    # insert data
    # 插入数据应该是list嵌套dict
    def insert_data(self, table_name, *argv):
        fields, values = '', ''
        for item in argv[0]: # 获取到字典
            # 利用reduce进行字符串合并  [1,2,3] -> '1, 2, 3'
            values = reduce(lambda x, y: x + ', ' + y, ["'" + x + "'" for x in item.values()])
            fields = reduce(lambda x, y: x + ', ' + y, [x for x in item.keys()])
            exec_sql = 'insert into {}({}) values ({})'.format(
                    table_name, fields, values)
            print(exec_sql)
            self.__conn.execute(exec_sql)
            self.__conn.commit();

    # 批量插入
    def batch_insert(self, table_name, *argv):

        key_list, placeholder_list, vals = '', '', []
        for item in argv[0]: # 获取到字典
            # 在第一次就打造fields list, 占位符
            if key_list == '' :
                # [key1, key2, key3] -> key1, key2, key3
                key_list = reduce(lambda x, y: x + ', ' + y, [key for key in item.keys()]);
                # 占位符
                placeholder_list = '?, ' * len(item.keys())
                # 字段列表
                fields = [field for field in item.keys()]
                print(key_list, placeholder_list, fields)
            # 每次都按照我们的key 顺序进行排序
            val = [ item.get(field) for field in fields ]
            vals.append(tuple(val))
        else:
            # 最后删除空格与,
            exec_sql = 'insert into {}({}) values ({})'.format(
                    table_name, key_list, placeholder_list[:-2])
            print(exec_sql, vals)
            self.__conn.executemany(exec_sql, vals)
            self.__conn.commit();

    # 清空table
    def delete_table(self, table_name):
        exec_sql = 'delete from {}'.format(table_name)
        try:
            self.__conn.execute(exec_sql)
            self.__conn.commit()
        except Exception as e:
            print(e)


    # 查询数据
    def fetch_data(self, table_name, columns):
        exec_sql = 'select {} from {}'.format(columns, table_name)
        results = [];
        cursor = self.__conn.cursor();
        # 一次性全部抓取
        # cursor.execute(exec_sql);
        # print(cursor.fetchall())
        for item in cursor.execute(exec_sql) :
            results.append(item)
        return results;


    def __del__(self):
        self.__conn.close()


if __name__ == '__main__':
    atm_db = inter_db('atm');
    stu_dict = {
        'name'  : 'text',
        'age'   : 'int' ,
        'gender': 'text',
        '*'     : 'name, gender' # * 代表主键
    }
    # 创建table
    atm_db.drop_table('stu')
    atm_db.create_table(table_name='stu', kwargv=stu_dict);
    stu_data = [
        {'name':'elan1', 'age':'31', 'gender':'man'},
        {'age':'32', 'name':'elan2', 'gender':'woman'},
        {'gender':'man', 'name':'elan3', 'age':'33' },
    ]
    # 插入测试
#    atm_db.insert_data('stu', stu_data)
    atm_db.batch_insert('stu', stu_data)
    atm_result = atm_db.fetch_data('stu', 'name, age, gender')
    print('before delete:', atm_result)
    # 删除测试
    atm_db.delete_table('stu')
    atm_result = atm_db.fetch_data('stu', 'name, age, gender')
    print('after delete:', atm_result)

