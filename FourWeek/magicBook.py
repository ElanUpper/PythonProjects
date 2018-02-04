import os
import re
import time
import random

9/2 ;  # 4.5
9//2;  # 4
9%2 ;  # 1

# 字符串分片
str = 'hello world';
str_1 = str[0:5];
str_2 = str[-5:];
#print(str_1, str_2)

# 电话隐私替换
phone = '186-1263-4669'
phone_security = phone.replace(phone[0:3], '*'*3).replace(phone[4:8], '*'*4)
#print(phone_security)

input_num = '1263'
position_s = phone.find(input_num);
position_e = phone.find(input_num)+len(input_num);
#print('phone number:', phone, 'hightlight:', position_s, position_e)

#print('the first step is print {} {}'.format('hello', 'world'));
#print('the first step is print {two} {one}'.format(one='world',two='hello'));
#iwords = input('input your words: _')
#print('your type {}'.format(iwords))

def calc_area(para1, para2) :
  if type(para1) != type(1) or type(para2) != type(2):
    print('please input integer');
  return (int(para1) * int(para2)) / 2;

#print(calc_area(10, 1));

def personal_open(file_name, msg='') :
  if file_name == '' :
    print("the file name shouldn't be empty");
    return 0 ;
  elif file_name == '.md' :
    print('great choice');
  else:
    pass;
  file_full_name = 'C:\\Users\\Elaner\\Desktop\\' + file_name ;
  with open(file_full_name, 'w') as fp:
    fp.write(msg);

#personal_open('', msg = 'hello world');
save_list = ['user1', '#*']
def login_check() :
  password = input('please input your password:');
  success_flag = password == save_list[0];
  reset_flag = password == save_list[1];
  if success_flag:
    print('success login');
  elif reset_flag :
    reset_passwd = input('please reset your password:');
    save_list[0] = reset_passwd;
    print(save_list);
  else:
    print('failed');
    login_check();

#login_check();

def test_str_list_id():
  while True :
    str = 'hello world' ;
    lst = [];
    lst.append(str);
    print(id(str), id(lst), lst)

def rename_files(location, file_type='.py'):
  import platform
  if location == '' :
    location = os.getcwd();
  fd_list = [];

  for fd in os.listdir(os.getcwd()):
    print(fd, os.getcwd())
    if(re.search(file_type, fd)) :
      # get modified time
      if platform.system() == 'Windows' :
        md_time = time.ctime(os.path.getmtime(fd));
        ct_time = time.ctime(os.path.getctime(fd));
      else:
        return 'not support!'
      fd_list.append([fd, ct_time, md_time])
  return fd_list ;

#print(rename_files('', file_type='.*'))
def getRandomInteger(bet, money) :
  if money > 0 :
    rollList = [ random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7) ];
    if sum(rollList) >= 11 :
      result = 'big';
    else:
      result ="Small";
    print(sum(rollList), result);
    #print('your choice:', 'Winner' if result=='Big' else 'Loser');
    if result == bet :
      money += 100;
    else:
      money -= 100;
    print('currently your money {}'.format(money))
    bet = input('input your choice!!')
    getRandomInteger(bet, money);
  else:
    print('you have no money go on');
    return ;

#getRandomInteger('big',1000);
'''
list: 
     1. 元素可变(insert, append, del, remove)并且每个元素都有一个位置[x]访问
     2. 元素可以是任意类型
'''
list_temp = [
  1,
  1.0,
  "list",
  [1, "str"],
  (1, 2),
  {1:"val"},
  print(10)
];
#list_temp[6];
#del list_temp[0:2];

# 获取列表索引
#for index, val in enumerate(list_temp):
#  print(index, val)

# list comprehension
FList = [];
time_start = time.clock();
for i in range(1, 1000) :
  FList.append(i);
time_end_for = time.clock();
#print('it cost:', time_end_for - time_start)
FList[:] = '';
Flist = [i for i in range(10, 1000)]
#print('it cost:', time.clock() - time_end_for)
# 返回0-1000内偶数
list_odd = [i for i in range(0, 100) if i % 2 == 0]
# 返回小写字母
letter_lower = [letter.lower() for letter in 'ABCDefg']

'''
  dict:
     key:value key不可重复不可以修改，value可以重复以及可修改
         key   必须为不可以变元素 , tuple, const string
         value 可以是任意类型元素
'''
dict_temple = {
  'name': 'elan',
  ('gender', 'age'): ['man', 29],
  'salary': print('security')
};
dict_temple['hometown'] = 'Shannxi'
dict_temple.update({'married': 'No', 'skill':'python'});
del dict_temple['hometown'];
#print(dict_temple)

# set comprehension  会根据值得多少进行截取
dict_fast = {i:val.upper() for i, val in zip(range(0,10), 'Acd#$ThTTY')}
#print(dict_fast)

'''
  set: 无序，不重复，不能切片不能索引
'''
set_data = [1, 1, 2, 'elan', 10, 'elan', 30]
set_template = set(set_data);
set_data = set_template;  # 去重
set_template.add('add')
#print(set_data, set_template)
set_template.discard('add');
#print(set_data, set_template)

def count_words() :
  import string
  with open("Walden.txt", 'rb') as fp :
    # 先去除标点符号 然后在小写 去掉不必要的字符 最后分解字符串
    words = fp.read().decode('gbk', 'ignore').strip(string.punctuation).lower().replace('锘','').split();
  words_set = set(words);
  dict_words = {index:words.count(index) for index in words}

  for word in sorted(dict_words, key=lambda x:dict_words[x]) :
    print("{} appear {} times ".format(word, dict_words[word]))

count_words();