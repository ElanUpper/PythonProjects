# author: elan

import json
import pickle

def print_message(x):
    return 'function called {}'.format(x) ;

def fun_data_serial(x):
   return {
        '1': x ,
        '2': str(x) + '_2',
        '3': print_message  # 这里仅仅可以存放function的地址
         # AttributeError: Can't pickle local object 'fun_data_serial.<locals>.<lambda >'
         # lambda x:'function called {}'.format(x)
    }.get(x)

def save_file(file_name, data):
    with open(file_name, 'w') as fp:
        fp.write(json.dumps(data))

def read_file(file_name):
    with open(file_name, 'r') as fp :
        ret_data = json.loads(fp.read())
    return ret_data;

def save_file_ex(file_name, data):
    with open(file_name, 'wb') as fp:
        #fp.write(pickle.dumps(data))
        pickle.dump(data, fp) # 当同于上句

def read_file_ex(file_name):
    with open(file_name, 'rb') as fp :
        #ret_data = pickle.loads(fp.read())
        ret_data = pickle.load(fp) # 当同于上句
    return ret_data;

if __name__ == '__main__' :

    set_data = {
        'name':'elan',
        'age':22
    };

    save_file('data.md', set_data);
    sav_data = read_file('data.md')
    print(type(sav_data), sav_data)

    # print(fun_data_serial('3')(3))
    # json存储函数
    # Object of type 'function' is not JSON serializable
    #save_file('data.md', fun_data_serial('3'));
    #sav_data = read_file('data.md')
    #print(type(sav_data), sav_data)

    # pickle:解决上述问题
    save_file_ex('data_ex.md', fun_data_serial('3'));
    sav_data = read_file_ex('data_ex.md')
    print(type(sav_data), sav_data(3))



